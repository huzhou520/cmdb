from django.db import models

# Create your models here.


class Host(models.Model):
    hostname = models.CharField(verbose_name='主机ip', max_length=32)


class Disk(models.Model):
    slot = models.CharField(verbose_name='槽位', max_length=10)
    pd_type = models.CharField(verbose_name='磁盘类型', max_length=12)
    capacity = models.CharField(verbose_name='磁盘容量', max_length=12)
    model = models.CharField(verbose_name='磁盘模式', max_length=12)
    disk_host = models.ForeignKey(verbose_name='磁盘对应的主机', to='Host', null=False)


class Memory(models.Model):
    capacity = models.CharField(verbose_name='内存大小', max_length=12)
    slot = models.CharField(verbose_name='内存槽位', max_length=10)
    model = models.CharField(verbose_name='内存模式', max_length=12)
    speed = models.CharField(verbose_name='内存速率', max_length=12)
    manufacturer = models.CharField(verbose_name='内存生产商', max_length=12)
    sn = models.CharField(verbose_name='内存序号', max_length=12)
    memory_host = models.ForeignKey(verbose_name='内存对应的主机', to='Host')


class Nic(models.Model):
    up = models.CharField(verbose_name='网卡是否开启', max_length=12)
    hwaddr = models.CharField(verbose_name='Mac地址', max_length=12)
    address = models.CharField(verbose_name='ip地址', max_length=12)
    netmask = models.CharField(verbose_name='子网掩码', max_length=12)
    broadcast = models.CharField(verbose_name='广播地址', max_length=12)
    nic_host = models.ForeignKey(verbose_name='网卡对应的主机', to='Host')


class Cpu(models.Model):
    processor = models.CharField(verbose_name='处理器', max_length=12)
    vendor_id = models.CharField(verbose_name='厂商名字', max_length=12)
    cpu_family = models.CharField(verbose_name='cpu核数', max_length=12)
    model = models.CharField(verbose_name='cpu模式', max_length=12)
    cpu_host = models.OneToOneField(verbose_name='CPU对应的主机', to='Host')


class Record(models.Model):
    record_host = models.ForeignKey(verbose_name='服务器', to='Host')
    content = models.TextField(verbose_name='变更信息')
    date = models.DateTimeField(verbose_name='变更时间', auto_now_add=True)