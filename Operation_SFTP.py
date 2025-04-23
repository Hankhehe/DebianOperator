import paramiko,csv,os

def UploadFolder_by_SFTP(ProbeIP,account,pwd,Local_Path,Remote_Path) -> None:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ProbeIP, username= account,password= pwd)
            sftp = ssh.open_sftp()
            ssh.exec_command(f'rm -rf {Remote_Path}') #預先刪除遠端的資料夾，以免重複
            if os.path.isdir(Local_Path):
                sftp.mkdir(Remote_Path)
                for item in os.listdir(Local_Path):
                    sftp.put(localpath=f'{Local_Path}\\{item}',remotepath=f'{Remote_Path}/{item}')
            else:
                 sftp.put(Local_Path,Remote_Path)
            ssh.close()
            print(f'{ProbeIP} has been finished to upload')

        except Exception as e :
            print(f'{ProbeIP} : {str(e)}')
        
if __name__ == "__main__":
    '''根據 IPlist.csv 裡的 IP_1 上傳或下載檔案透過 SFTP'''

    SShacc = input('SSH Account: ')
    SSHpwd = input('SSH Password: ')
    local_path = input('Please type localPath: ')
    remote_path = input('Please type RemotePath: ')
    ProbeDaemonIPs = []
    print('load data IPlist.csv')
    with open('IPlist.csv',mode = 'r',encoding='utf-8') as f:
        tempdataDaemon = csv.reader(f)
        next(tempdataDaemon)
        ProbeDaemonIPs = list(tempdataDaemon)
    for ip in ProbeDaemonIPs :
        UploadFolder_by_SFTP(ProbeIP=ip[0],account=SShacc,pwd=SSHpwd,Local_Path=local_path,Remote_Path=remote_path)
    input('key any key to exit')
