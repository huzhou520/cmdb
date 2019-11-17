from api import models


class Cpu(object):
    def process(self, host_obj, cpu):
        # cpu: {'status': True, 'data': {'processor': ' 0', 'vendor_id': ' GenuineIntel', 'cpu family': ' 6', 'model': ' 158'}, 'error': None}
        cpu_data = cpu['data']
        record_msg_list = []
        cpu_obj = models.Cpu.objects.filter(cpu_host=host_obj).first()

        # 最开始cpu信息采集
        cpu_data['cpu_family'] = cpu_data['cpu family']
        cpu_data.pop('cpu family')
        if not cpu_obj:
            models.Cpu.objects.create(**cpu_data, cpu_host=host_obj)
            return '添加成功'
            # exit(10)

        # cpu改

        for k, v in cpu_data.items():
            if v != getattr(cpu_obj, k):
                cpu_update_msg = '%s的%s,变更成%s' % (k, getattr(cpu_obj, k), v)
                record_msg_list.append(cpu_update_msg)
                setattr(cpu_obj, k, v)

        if record_msg_list:
            cpu_obj.save()
            models.Record.objects.create(record_host=host_obj, content='\n'.join(record_msg_list))
