from api import models


def process_disk(host_obj, disk_data):
    old_disk_queryset = models.Disk.objects.filter(disk_host_id=host_obj.id)
    old_disk_obj = {obj.slot: obj for obj in old_disk_queryset}
    old_disk_set = set(old_disk_obj.keys())
    new_disk_set = set(disk_data.keys())
    print(old_disk_set, new_disk_set)

    record_msg_list = []
    # 增加数据
    append_disk_set = new_disk_set - old_disk_set
    print(append_disk_set)
    creat_obj_list = []
    for slot_num in append_disk_set:
        slot_dict = disk_data[slot_num]
        # 方式一增加数据
        # models.Disk.objects.create(**slot_dict, disk_host_id=host_obj.id)

        # 方式二增加数据bulk_create
        disk_obj = models.Disk(**slot_dict, disk_host_id=host_obj.id)
        creat_obj_list.append(disk_obj)

    if creat_obj_list:
        models.Disk.objects.bulk_create(creat_obj_list, batch_size=10)
        append_msg = '在%s槽位新增硬盘' % (slot_num)
        record_msg_list.append(append_msg)

    # 删除硬盘
    delete_disk_set = old_disk_set - new_disk_set
    print(delete_disk_set)
    models.Disk.objects.filter(slot__in=delete_disk_set).delete()
    if delete_disk_set:
        delete_msg = '在%s槽位删除硬盘' % ','.join(delete_disk_set)
        record_msg_list.append(delete_msg)

    # 更新数据
    update_disk_set = new_disk_set & old_disk_set
    print(update_disk_set)
    for slot in update_disk_set:
        old_disk_row_obj = old_disk_obj[slot]  # 磁盘表对应行的对象
        new_disk_row_dict = disk_data[slot]  # {'slot': '4', 'pd_type': 'SATA', 'caity': '479', 'model': 'NSA'}
        for k, v in new_disk_row_dict.items():
            # 判断每个新获取的字段值是否和老表里的值相等，不相等就更新
            if v != getattr(old_disk_row_obj, k):
                update_msg = '%s由%s变成了%s' % (k, getattr(old_disk_row_obj, k), v)
                msg = '槽位%s: %s' % (slot, update_msg)
                print(getattr(old_disk_row_obj, k))
                record_msg_list.append(msg)
                setattr(old_disk_row_obj, k, v)

        old_disk_row_obj.save()
    # for k, v in disk_data.items():
    #     print(k, v)
    #     models.Disk.objects.create(**v, disk_host_id=1)
    # for disk_k, disk_v in v.items():
    #     print(disk_k, disk_v)
    # pass
    # models.Disk.objects.create()

    if record_msg_list:
        print(record_msg_list)
        models.Record.objects.create(record_host_id=host_obj.id,
                                     content='\n'.join(record_msg_list))


class Disk(object):

    def process(self, host_obj, disk):
        disk_data = disk['data']
        old_disk_queryset = models.Disk.objects.filter(disk_host_id=host_obj.id)
        old_disk_obj = {obj.slot: obj for obj in old_disk_queryset}
        old_disk_set = set(old_disk_obj.keys())
        new_disk_set = set(disk_data.keys())
        # print(old_disk_set, new_disk_set)

        record_msg_list = []
        # 增加数据
        append_disk_set = new_disk_set - old_disk_set
        # print(append_disk_set)
        creat_obj_list = []
        for slot_num in append_disk_set:
            slot_dict = disk_data[slot_num]
            # 方式一增加数据
            # models.Disk.objects.create(**slot_dict, disk_host_id=host_obj.id)

            # 方式二增加数据bulk_create
            disk_obj = models.Disk(**slot_dict, disk_host_id=host_obj.id)
            creat_obj_list.append(disk_obj)

        if creat_obj_list:
            models.Disk.objects.bulk_create(creat_obj_list, batch_size=10)
            append_msg = '在%s槽位新增硬盘' % (slot_num)
            record_msg_list.append(append_msg)

        # 删除硬盘
        delete_disk_set = old_disk_set - new_disk_set
        # print(delete_disk_set)
        models.Disk.objects.filter(slot__in=delete_disk_set).delete()
        if delete_disk_set:
            delete_msg = '在%s槽位删除硬盘' % ','.join(delete_disk_set)
            record_msg_list.append(delete_msg)

        # 更新数据
        update_disk_set = new_disk_set & old_disk_set
        print('update_disk_set: %s' % update_disk_set)
        for slot in update_disk_set:
            old_disk_row_obj = old_disk_obj[slot]  # 磁盘表对应行的对象
            new_disk_row_dict = disk_data[slot]  # {'slot': '4', 'pd_type': 'SATA', 'caity': '479', 'model': 'NSA'}
            for k, v in new_disk_row_dict.items():
                # 判断每个新获取的字段值是否和老表里的值相等，不相等就更新
                if v != getattr(old_disk_row_obj, k):
                    update_msg = '%s由%s变成了%s' % (k, getattr(old_disk_row_obj, k), v)
                    msg = '槽位%s: %s' % (slot, update_msg)
                    print(getattr(old_disk_row_obj, k))
                    record_msg_list.append(msg)
                    setattr(old_disk_row_obj, k, v)

            old_disk_row_obj.save()
        # for k, v in disk_data.items():
        #     print(k, v)
        #     models.Disk.objects.create(**v, disk_host_id=1)
        # for disk_k, disk_v in v.items():
        #     print(disk_k, disk_v)
        # pass
        # models.Disk.objects.create()

        if record_msg_list:
            print(record_msg_list)
            models.Record.objects.create(record_host_id=host_obj.id,
                                         content='\n'.join(record_msg_list))