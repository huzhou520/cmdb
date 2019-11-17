from django.conf import settings
import importlib


def process_server_info(host_obj, disk_data):
    for key, path in settings.CMDB_PLUGIN_DICT.items():
        module_path, class_name = path.rsplit('.', maxsplit=1)
        module = importlib.import_module(module_path)
        obj = getattr(module, class_name)()
        obj.process(host_obj, disk_data[key])
