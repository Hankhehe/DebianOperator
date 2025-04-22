import hashlib,paramiko,struct,sys

def get_probe_id(mac) -> int:
    h = 0
    mac = str.upper(mac).replace(' ','').replace(':','').replace('-','').replace('.','')
    buffer = hashlib.md5(mac.encode('utf-16le')).digest()

    for i in range(4):
        h += struct.unpack('<I', buffer[i * 4 : (i + 1) * 4])[0]

    return h

def sshClient(ProbeIP,account,pwd,cmd) -> str:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ProbeIP, username= account,password= pwd)
            stdin, stdout, stderr =  ssh.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            mac_address = output.replace('\n','')
            ssh.close()
            return str(mac_address)
        except Exception as e :
            print(str(e))
            input('key any key to exit')
            sys.exit()
        
if __name__ == "__main__":
    id = get_probe_id('AB0000000000')
    print(id)
    pass

    optioncode = input('1=auto , 2=specific IP :')
    if optioncode == '1':
        eth0_mac = sshClient(ProbeIP='1.1.1.1',account='root',pwd='1111',cmd="ifconfig eth0 | awk '/ether/ {print $2}'")
        print(f'ProbeID : {get_probe_id(eth0_mac)}')
        input('key any key to exit')

    elif optioncode == '2':
        Probe_IP = input('Probe IP :')
        SSH_Account = input('SSH Account :')
        SSH_Pwd = input('SSH PWD :')
        eth0_mac = sshClient(ProbeIP=Probe_IP,account=SSH_Account,pwd=SSH_Pwd,cmd="ifconfig eth0 | awk '/ether/ {print $2}'")
        print(f'ProbeID : {get_probe_id(eth0_mac)}')
        input('key any key to exit')

    else :
         print('option not found')
         input('key any key to exit')
