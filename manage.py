#!/usr/bin/env python
import os
import sys
import threading
from remote_operation.udp_service import udp_server
# from remote_operation.views import udp_handler

if __name__ == '__main__':
    # upd_service_thread = threading.Thread(target=udp_server.main)
    # upd_service_thread = threading.Thread(target=udp_server.udp_handler)
    # upd_service_thread.setDaemon(True)
    # upd_service_thread.start()
    # print('UDP SERVICE START')
    # print('--------------------------------------------')
    # print()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarthome_1809142054.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

