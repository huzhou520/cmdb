from api import models

class Memory(object):
    def process(self, host_obj, memory):
        memory_data = memory['data']
        old_memory_queryset = models.Memory.objects.filter(memory_host_id=host_obj.id)
        old_memory_obj = {obj.slot: obj for obj in old_memory_queryset}
        old_memory_set = set(old_memory_obj.keys())
        new_memory_set = set(memory_data.keys())
        # print(old_memory_set, new_memory_set)

        record_msg_list = []
        # 增加数据
        append_memory_set = new_memory_set - old_memory_set
        # print(append_memory_set)
        creat_obj_list = []
        for slot_num in append_memory_set:
            slot_dict = memory_data[slot_num]
            # 方式一增加数据
            # models.memory.objects.create(**slot_dict, memory_host_id=host_obj.id)

            # 方式二增加数据bulk_create
            memory_obj = models.Memory(**slot_dict, memory_host_id=host_obj.id)
            creat_obj_list.append(memory_obj)

        if creat_obj_list:
            models.Memory.objects.bulk_create(creat_obj_list, batch_size=10)
            append_msg = '在%s槽位新增内存' % (slot_num)
            record_msg_list.append(append_msg)

        # 删除内存
        delete_memory_set = old_memory_set - new_memory_set
        # print(delete_memory_set)
        models.Memory.objects.filter(slot__in=delete_memory_set).delete()
        if delete_memory_set:
            delete_msg = '在%s槽位删除内存' % ','.join(delete_memory_set)
            record_msg_list.append(delete_msg)

        # 更新数据
        update_memory_set = new_memory_set & old_memory_set
        print('update_memory_set: %s' % update_memory_set)
        for slot in update_memory_set:
            old_memory_row_obj = old_memory_obj[slot]  # 磁盘表对应行的对象
            new_memory_row_dict = memory_data[slot]  # {'slot': '4', 'pd_type': 'SATA', 'caity': '479', 'model': 'NSA'}
            for k, v in new_memory_row_dict.items():
                # 判断每个新获取的字段值是否和老表里的值相等，不相等就更新
                if v != getattr(old_memory_row_obj, k):
                    update_msg = '%s由%s变成了%s' % (k, getattr(old_memory_row_obj, k), v)
                    msg = '内存槽位%s: %s' % (slot, update_msg)
                    print(getattr(old_memory_row_obj, k))
                    record_msg_list.append(msg)
                    setattr(old_memory_row_obj, k, v)

            old_memory_row_obj.save()
        # for k, v in memory_data.items():
        #     print(k, v)
        #     models.memory.objects.create(**v, memory_host_id=1)
        # for memory_k, memory_v in v.items():
        #     print(memory_k, memory_v)
        # pass
        # models.memory.objects.create()

        if record_msg_list:
            print(record_msg_list)
            models.Record.objects.create(record_host_id=host_obj.id,
                                         content='\n'.join(record_msg_list))
