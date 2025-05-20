import paramiko

class Client:
    def __init__(self, host, username, password, port):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=host, port=port, username=username, password=password, look_for_keys=False)
        self.ftp = self.client.open_sftp()
        print('connection established successfully')

    def __del__(self):
        self.client.close()


# # create client
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname=host,port=port,username=username,password=password, look_for_keys=False)
# ftp = client.open_sftp()

# print('connection established successfully')

