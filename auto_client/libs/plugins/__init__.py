from settings import PLUGIN_DICT


def get_server_info(hostname, ssh_func):
    """

    :param hostname: 要操作的远程主机
    :param ssh_func: 要执行的方法
    :return:
    """
    info_dict = {}
    for key, path in PLUGIN_DICT.items():
        # 1.切割settings文件中的字典
        """
        例：libs.plugins.board.Board，切割settings文件中的values切成如下：
        key：libs.plugins.board(模块路径)    value: Board（对应模块下面的方法）
        """
        module_name, class_name = path.rsplit('.', maxsplit=1)

        # 2.以字符串的方式加载模块
        import importlib
        module = importlib.import_module(module_name)
        # print(module_name,class_name)
        # 3.通过反射找模块下面的方法
        cls = getattr(module, class_name)
        # print(module_name, class_name)

        # 4.实例化对象
        obj = cls()

        # 5.执行对象的process方法
        ret = obj.process(hostname, ssh_func)
        info_dict[key] = ret
    # print(info_dict)
    return info_dict
