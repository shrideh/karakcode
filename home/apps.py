import os
import sys
import time
import tempfile
from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'home'
    
    
    def ready(self):
        is_server_command = (
            'runserver' in sys.argv or 
            'uwsgi' in sys.argv[0] or 
            'gunicorn' in sys.argv[0]
        )
        
        if not is_server_command:
            return


        if 'runserver' in sys.argv and os.environ.get('RUN_MAIN') != 'true':
            return


        if 'uwsgi' in sys.argv[0]:
            master_pid = os.environ.get('UWSGI_MASTER_PID')
            if master_pid and str(os.getpid()) != master_pid:
                return


        lock_file = os.path.join(tempfile.gettempdir(), 'karak_banner.lock')
        if os.path.exists(lock_file):
            if time.time() - os.path.getmtime(lock_file) < 2:
                return
        
        with open(lock_file, 'w') as f:
            f.write("1")
        try:
            from karakcode import banner
            print(banner.ASCII_BANNER)
        except ImportError:
            pass


        
 



