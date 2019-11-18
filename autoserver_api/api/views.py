from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from api import models
from rest_framework import serializers
from api.plugins.disk import Disk
from api.plugins import process_server_info
# Create your views here.


class ServerView(APIView):
    def get(self, request, *args, **kwargs):
        # host_list = ['192.168.16.158']
        host_list = []
        host_queryset = models.Host.objects.all()
        for obj in host_queryset:
            if obj.status == 1:
                host_list.append(obj.hostname)
        return Response(host_list)

    def post(self, request, *args, **kwargs):

        result = request.data
        """
        通过集合的交并差方式实现磁盘的增删改查
        """
        # 获取数据库磁盘数据和新传过来的磁盘数据进行处理
        hostname = result['hostname']
        host_obj = models.Host.objects.filter(hostname=hostname).first()
        if not host_obj:
            return Response('主机不存在')

        # disk_data = result['info']['disk']['data']
        # obj = Disk()
        # obj.process(host_obj, disk_data)

        retrieve_data = result['info']
        print(retrieve_data)
        process_server_info(host_obj, retrieve_data)

        return Response('发送成功')


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        str1 = 'Hello Darkness, my old friend.'
        return Response(str1)