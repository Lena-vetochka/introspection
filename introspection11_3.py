import inspect
from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    #Получаем модуль, к которому принадлежит объект
    obj_module = obj.__class__.__module__

    info_obj = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info_obj


number_info = introspection_info(42)
#print(number_info)
pprint(number_info, width = 1, sort_dicts= False)



