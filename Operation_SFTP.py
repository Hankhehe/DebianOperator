import paramiko,csv
from scp import SCPClient

def UploadFolder_by_SFTP(ProbeIP,account,pwd,local_folder,remote_folder) -> None:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ProbeIP, username= account,password= pwd)
            with SCPClient(ssh.get_transport()) as scp:
                scp.put(local_folder, recursive=True, remote_path=remote_folder)
            ssh.close()
            print(f'{ProbeIP} has been finished to upload')

        except Exception as e :
            print(f'{ProbeIP} : {str(e)}')
        
if __name__ == "__main__":
    '''根據 IPlist.csv 裡的 IP_1 上傳或下載檔案透過 SFTP'''

    SShacc = input('SSH Account: ')
    SSHpwd = input('SSH Password: ')
    local_folder = input('Please type localPath: ')
    remote_folder = input('Please type RemotePath: ')
    ProbeDaemonIPs = []
    print('load data IPlist.csv')
    with open('IPlist.csv',mode = 'r',encoding='utf-8') as f:
        tempdataDaemon = csv.reader(f)
        next(tempdataDaemon)
        ProbeDaemonIPs = list(tempdataDaemon)
    for ip in ProbeDaemonIPs :
        UploadFolder_by_SFTP(ProbeIP=ip[0],account=SShacc,pwd=SSHpwd,local_folder=local_folder,remote_folder=remote_folder)
    input('key any key to exit')
