from django.apps import AppConfig

class RemoteOperationConfig(AppConfig):
    name = 'remote_operation'

    def ready(self):
        from remote_operation import upd_service_thread