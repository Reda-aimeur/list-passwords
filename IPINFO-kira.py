import sys
try:
    import requests
except:
    from os import system as sh
    sh('pip install requests')
def ipssl(ip):
    print('set search in [ ', ip, ' ] for info')
    urlG = str('http://ipinfo.io/' + ip)
    re = requests.get(urlG)
    print(re.text)
def nocon():
        print(' You Can Use >>> $IPINFO-kira.py {ip} or {my}')
        ip = input(' ipv4]} ')
        if '.' in ip:
            ipssl(ip=ip)
        else:
            if ip == 'my':
                ipssl(ip='')
            else:
                print('This is{',ip ,'}not ip addras  quit(0110010)')
try:
    yip = str(sys.argv[1])
except:
    nocon()
    exit()
if '.' in yip:
    ipssl(ip=yip)
else:
    if '--help' in yip:
        print ("""
        -help '--help'   -This help print page
        -order '-A'        -print information of maker this tool and support also help page

                python3 __main__ 1.1.1.1 -f flarip.json 
            to use The script try:
                run it dirc
                run like this '' python3 IPINFO-kira.py <IP>''
            except:
                you cat select more then 2 option
            and enjoy ... 
        """)
    else:
        if '-A' in yip:
            print("""
             make this tool to be frindData reder and option
                This tool use http://ipinfo.io/ for more of this
                    request from facebook accont or call me 
                        Licenc Enterprise Edition.
            """)
        else:
if '-f' in sys.argv[2]:
    yip = str(sys.argv[3])
    print('}  ',yip ,' crate file')
    fileip = open(yip, "a")
    fileip.write(nocon(ip=sys.arg[1]))
    fileip.close()
if '-r' in sys.argv[4]:
    yip = str(sys.argv[5])
    print(yip)