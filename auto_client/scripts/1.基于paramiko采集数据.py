import paramiko

private_key = paramiko.RSAKey.from_private_key_file(r'C:/Users/86185/.ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.16.158', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()

data = result.decode('utf-8')
print(data)
# print(result)



###########3
# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
#
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# # 连接服务器
# ssh.connect(hostname='192.168.16.158', port=22, username='root', password='default')
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# # 关闭连接
# ssh.close()
# data = result.decode('utf-8')[0:10]
# print(data)
# # print(result.decode('utf-8'))
#
# import requests
#
# requests.post(
#     url="http://127.0.0.1:8000/api/v1/server/",
#     json={"server": data, "host": "192.168.16.158"}
# )