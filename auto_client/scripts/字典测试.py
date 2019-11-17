cpu_data = {'status': True, 'data': {'processor': ' 0', 'vendor_id': ' GenuineIntel', 'cpu family': ' 6', 'model': ' 158'},
         'error': None}

dic_data = cpu_data['data']
# dic_data['cpu_family'] = getattr(dic_data, 'cpu family')
dic_data['cpu_family'] = dic_data['cpu family']
print(dic_data)
# dic_data.remove('cpu family')
dic_data.pop('cpu family')
print(dic_data)