#!/usr/bin/env python
import os
import sys
import asyncio

if __name__ == '__main__':
    # Add so we can use subprocess in consumers
    asyncio.get_child_watcher()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eq_dojo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
