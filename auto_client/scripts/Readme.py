"""
目前CMDB有三个组件：
数据采集端(auto_client)：
    1.主要负责数据的收集，传给api端（autoserver_api）
    2.对收集的数据进行处理

api端（autoserver_api）:
    A.向数据采集端提供要采集的ip地址
    B.接受采集端的数据并做处理，然后存入数据库后台管理：数据的可视化查看


"""

dic1 = {}
dic1['name  '] = "test"
print(dic1)