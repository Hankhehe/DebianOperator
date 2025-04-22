import paramiko,csv

def sshClient(ProbeIP,account,pwd, sourceIP,cmd) -> None:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ProbeIP, username= account,password= pwd)

            shell = ssh.invoke_shell()
            shell.send(cmd + '\n')
            print(f'{sourceIP} : has enabled port')
            # stdin, stdout, stderr =  ssh.exec_command(cmd)
            # ssh.close()

        except Exception as e :
            print(f'{ProbeIP} : {str(e)}')
        
if __name__ == "__main__":
    SSHAcc = input('SSH Acc: ')
    SSHPwd = input('SSH Pwd: ')
    EnablePort = int(input('Listen Port Number: '))
    ProbeDaemonIPs = []
    print('load data IPlist.csv')
    with open('IPlist.csv',mode = 'r',encoding='utf-8') as f:
        tempdataDaemon = csv.reader(f)
        next(tempdataDaemon)
        ProbeDaemonIPs = list(tempdataDaemon)
    for ip in ProbeDaemonIPs :
        resultbyssh = sshClient(ProbeIP=ip[0],account= SSHAcc, pwd= SSHPwd,sourceIP= ip[1] , cmd=f"nc -l -p {EnablePort} -s {ip[1]} &")
    input('key any key to exit')




