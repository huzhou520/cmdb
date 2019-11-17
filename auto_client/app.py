import paramiko
import settings
import requests
from concurrent.futures import ThreadPoolExecutor
from libs.plugins import get_server_info


def ssh(hostname, command):
    # private_key = paramiko.RSAKey.from_private_key_file(r'C:/Users/86185/.ssh/id_rsa')
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
    # stdin, stdout, stderr = ssh.exec_command(command)
    # result = stdout.read()
    # ssh.close()
    # return result.decode('utf-8')





    private_key = paramiko.RSAKey.from_private_key_file(r'C:/Users/86185/.ssh/id_rsa')

    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER,
                pkey=private_key)

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    # 获取命令结果
    result = stdout.read()

    # 关闭连接
    ssh.close()

    data = result.decode('utf-8')
    # print(data)
    return data


def task(hostname):
    ret_info = get_server_info(hostname, ssh)
    print(ret_info)
    requests.post(url="http://127.0.0.1:8000/api/v1/server/",
                  json={"hostname": hostname, "info": ret_info})


def run():
    response = requests.get(url="http://127.0.0.1:8000/api/v1/server/")
    # print(response.text, type(response))
    host_list = response.json()
    # print(host_list, type(host_list))
    pool = ThreadPoolExecutor(settings.THREAD_POOL_SIZE)
    for host in host_list:
        # 方法一：
        # ret = get_server_info(host, ssh)
        # requests.post(url="http://127.0.0.1:8000/api/v1/server/",
        #               json=ret)

        # 可以通过线程池来实现，实现高并发
        # 方法二：
        print(host)

        pool.submit(task, host)


if __name__ == "__main__":
    # print("__name__的值是：%s" % __name__)
    run()