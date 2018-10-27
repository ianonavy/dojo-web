import asyncio
import asyncio.subprocess
import json
import os
import tempfile

from channels.generic.websocket import AsyncWebsocketConsumer


class SessionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.room_group_name = 'chat_%s' % self.session_id

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )

    # Receive message from room group
    async def code_change(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))

    async def run(self, event):
        if not asyncio.get_event_loop():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        asyncio.get_event_loop().create_task(self.do_command(event))

    async def do_command(self, event):
        with tempfile.TemporaryDirectory() as tmpdirname:
            os.chdir(tmpdirname)
            with open('test_code.py', 'w+') as test_file:
                test_file.write(event['tests'])
            with open('dojo_code.py', 'w+') as test_file:
                test_file.write(event['code'])

            create = asyncio.create_subprocess_exec(
                'pytest', '-v',
                stdout=asyncio.subprocess.PIPE,
            )
            proc = await create

            output = {
                "type": "new-output",
            }
            await self.send(text_data=json.dumps(output))

            while True:
                line = await proc.stdout.read(1)
                if not line:
                    break
                output = {
                    "type": "output",
                    "content": line.decode('utf-8'),
                }
                await self.send(text_data=json.dumps(output))

            await proc.wait()

            output = {
                "type": "test-error-code",
                "code": proc.returncode,
            }
            await self.send(text_data=json.dumps(output))
