import paramiko

def sshclient_execmd(host, port, username, password, cmd):
    """
    定义执行命令方法cmd为执行命令参数
    host：ssh主机名或ip地址
    port：ssh主机名或ip地址端口
    username：用户名
    password：密码
    cmd：cmd命令

    """
    """建立远程连接SSH"""
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    """允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面"""
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    """连接远程服务器"""
    client.connect(host, port, username, password)
    """建立一个会话"""
    session = client._transport.open_session()
    """执行命令"""
    session.exec_command(cmd)
    """建立读文件流"""
    stdout = session.makefile('rb')
    """输出所有执行命令后的信息list型"""
    result = stdout.readlines()
    return result


def select(sql, dbip, dbusername, dbpwd, dbinstance, host, port, username, password):
    """

    sql: 需查询的sql语句
    dbip: 数据库的主机名或ip地址
    dbusername: 数据库连接的用户名
    dbpwd: 数据库连接的密码
    dbinstance: 需查询的数据库名称

    """
    cmd = 'mysql -h ' + dbip + ' -u' + dbusername + ' -p' + dbpwd + ' ' + dbinstance + ' -e "' + sql + '"'
    collection = sshclient_execmd(host, port, username, password, cmd)
    header = collection[0].decode('utf-8').strip('\n').split('\t')
    """获取行数"""
    row_num = len(collection)
    data_list = []
    """读取行"""
    for i in range(1, row_num):
        row_data = collection[i].decode('utf-8').strip('\n').split('\t')
        """读取行中的每一列的值"""
        d = dict(zip(header, row_data))
        data_list.append(d)
    return data_list


# select('select Id, Version from CompanyRealNameAuthenticate where CompanyBusinessNo="987654686451405112" order by UpdateTime desc limit 1',
#        '172.60.0.78', 'platform', 'platform', 'kpay_backend',
#        '172.16.100.40', 22, 'devops', 'OGU2NWIxYmIw')

