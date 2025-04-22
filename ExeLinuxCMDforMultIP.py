import paramiko,csv

def sshClient(ProbeIP,account,pwd,cmd) -> None:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ProbeIP, username= account,password= pwd)
            stdin, stdout, stderr =  ssh.exec_command(cmd)
            print(f'{ProbeIP} : {stdout.read()}')

            ssh.close()

        except Exception as e :
            print(f'{ProbeIP} : {str(e)}')
        
if __name__ == "__main__":
    '''根據 IPlist 裡的 IP_1 批次執行 cmd 指令'''

    SShacc = input('SSH Account: ')
    SSHpwd = input('SSH Password: ')
    inputcmd = input('Please type cmd: ')
    ProbeDaemonIPs = []
    print('load data IPlist.csv')
    with open('IPlist.csv',mode = 'r',encoding='utf-8') as f:
        tempdataDaemon = csv.reader(f)
        next(tempdataDaemon)
        ProbeDaemonIPs = list(tempdataDaemon)
    for ip in ProbeDaemonIPs :
        resultbyssh = sshClient(ProbeIP=ip[0],account=SShacc,pwd=SSHpwd,cmd= inputcmd)
    input('key any key to exit')




