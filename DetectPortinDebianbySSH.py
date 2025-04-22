import paramiko,csv

def sshClient(ProbeIP,account,pwd,cmd,sourceIP) -> None:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ProbeIP, username= account,password= pwd)
            stdin, stdout, stderr =  ssh.exec_command(cmd)
            print(f'{sourceIP} : {stderr.read()}')

            ssh.close()

        except Exception as e :
            print(f'{ProbeIP} : {str(e)}')
        
if __name__ == "__main__":
    SSHAcc = input('SSH Acc: ')
    SSHPwd = input('SSH Pwd: ')
    LocalPort = input('LocalPort number: ')
    RemoteIP = input('RemoteIP: ')
    RemotePort = input('RemotePort: ')
    ProbeDaemonIPs = []
    print('load data IPlist.csv')
    with open('IPlist.csv',mode = 'r',encoding='utf-8') as f:
        tempdataDaemon = csv.reader(f)
        next(tempdataDaemon)
        ProbeDaemonIPs = list(tempdataDaemon)
    for ip in ProbeDaemonIPs :
        resultbyssh = sshClient(ProbeIP=ip[0],account= SSHAcc,pwd= SSHPwd, sourceIP=ip[1] ,cmd=f'nc -s {ip[1]} -p {LocalPort} -zv {RemoteIP} {RemotePort} -w 5')
    input('key any key to exit')




