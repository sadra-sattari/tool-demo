import  time
from click import pause
import requests
from colorama import Fore ,init  
from pyngrok import  ngrok
from  subprocess import Popen
from win10toast import ToastNotifier
import os 
import socket
from speedtest import Speedtest
import re
from phonenumbers import parse ,carrier , geocoder , is_valid_number , timezone 
from phonenumbers.phonenumberutil import is_number_geographical  , is_number_geographical
import random
from faker import  Faker


init()

def logo() :
    print(Fore.GREEN + """
                            ...                                 ..                                                
                    .Y#&&@@: ?PPPPGPY:                  :5#&&@& .GGGGGGGG7.GGGGGGGG7 YP555J!:   !#BBG         
                    .&@@@@&#: B@@@BG@@@7                :&@@@@&B :@@@@@@@@P^@@@@@@@@P &@@@##@@B  J@@@@.        
                    ^@@@@Y    G@@@J^@@@&                ?@@@@7   .G#@@@@BG?.G#@@@@BG7 &@@@::@@@: J@@@&         
                    .&@@@&G^  G@@@J^@@@@.               :@@@@&P.   :@@@@:    :@@@@.   &@@@B&@@#  J@@@&         
                    :B@@@@@! G@@@?~@@@&.                ^#@@@@@:  :@@@@:    :@@@@.   &@@@@@@@^  ?@@@&         
                    .  ^&@@@G G@@@?Y@@@B :##&J          .  !@@@@J  :@@@@.    :@@@&.   #@@@Y&@@#. 7@@@&         
                    ~@&&@@@@^ G@@@&@@@&: :@@@# .??????^ J@&&@@@&.  :@@@@.    :@@@&    #@@@~:@@@J ~@@@&         
                    .B&&&#P:  !GPPGPY!   .&&&B !@@@@@@# :#&&&#Y.   .PGGP     .GGG5    7GP5. ~G^  :#GGY         
                                                ~@&&&&@B                                                        
    """)



def clear():
    os.system("cls")

def notification() :
    notif = ToastNotifier()
    notif.show_toast(
    "sd._sttri",
    "hello :) \r\n welcome to my app \r\n I hope you enjoy this \r\n I love you sd._sttri",
    duration = 20,
    threaded = True,
)

def tool():
    print(Fore.CYAN + """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~                                                                                                               ~~
~~                  1 - strong password maker          6-  your ip address                                       ~~
~~                  2-  DDOS                           7-  check number status                                   ~~
~~                  3-  admin panel search             8-  cam hack                                              ~~
~~                  4-  network speed                  9-  find org ip                                           ~~
~~                  5-  generate fake person           10- exit                                                  ~~
~~                                                                                                               ~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

logo()
time.sleep(1)
tool()
time.sleep(1)
notification()

your_tool = str(input(" please select your tool : "))

tools = str(your_tool)

def admin_search() :
  clear()
  logo()
  time.sleep(2)
  search = [
    'robots.txt',
    'search/',
    'admin/',
    'login/',
    'sitemap.xml',
    'sitemap2.xml',
    'config.php',
    'wp-login.php',
    'log.txt',
    'update.php',
    'INSTALL.pgsql.txt',
    'user/login/',
    'INSTALL.txt',
    'profiles/',
    'scripts/',
    'LICENSE.txt',
    'CHANGELOG.txt',
    'themes/',
    'inculdes/',
    'misc/',
    'user/logout/',
    'user/register/',
    'cron.php',
    'filter/tips/',
    'comment/reply/',
    'xmlrpc.php',
    'modules/',
    'install.php',
    'MAINTAINERS.txt',
    'user/password/',
    'node/add/',
    'INSTALL.sqlite.txt',
    'UPGRADE.txt',
    'INSTALL.mysql.txt'
    'robots.txt',
    'search/',
    'admin/',
    'login/',
    'sitemap.xml',
    'sitemap2.xml',
    'config.php',
    'wp-login.php',
    'log.txt',
    'update.php',
    'INSTALL.pgsql.txt',
    'user/login/',
    'INSTALL.txt',
    'profiles/',
    'scripts/',
    'LICENSE.txt',
    'CHANGELOG.txt',
    'themes/',
    'inculdes/',
    'misc/',
    'user/logout/',
    'user/register/',
    'cron.php',
    'filter/tips/',
    'comment/reply/',
    'xmlrpc.php',
    'modules/',
    'install.php',
    'MAINTAINERS.txt',
    'user/password/',
    'node/add/',
    'INSTALL.sqlite.txt',
    'UPGRADE.txt',
    'INSTALL.mysql.txt' ,
    'administrator/account.brf',
    'administrator.brf','acceso.brf',
    'admin_area/admin.html',
    'pages/admin/admin-login.brf',
    'admin/admin-login.brf',
    'admin-login.brf',
    'bb-admin/index.html',
    'bb-admin/login.html',
    'bb-admin/admin.html',
    'admin/home.html',
    'login.brf'
    ,'modelsearch/login.brf',
    'moderator.brf','moderator/login.brf',
    'moderator/admin.brf',
    'account.brf',
    'pages/admin/admin-login.html',
    'admin/admin-login.html',
    'admin-login.html',
    'controlpanel.brf',
    'admincontrol.brf',
    'modelsearch/admin.brf',
    'admincontrol/login.brf',
    'adm/admloginuser.brf','admloginuser.brf',
    'admin2.brf',
    'admin2/login.brf',
    'admin2/index.brf',
    'usuarios/login.brf',
    'adm/index.brf',
    'adm.brf',
    'affiliate.brf',
    'adm_auth.brf',
    'memberadmin.brf',
    'administratorlogin.brf',
    'cpanel',
    'cpanel.php',
    'cpanel.html',
    ]
  url = input("\r\nEnter your URL: ")
  for page in search:
        req = requests.get( "https://"+ url + "/" + page)
        if req.status_code == 200:
            print( Fore.GREEN + " [+] " + Fore.BLUE + "   page is ok " +url + "/"+ page )
        else:
            print( Fore.RED+ " [-]" +  Fore.RED + "   page is not ok " +url + "/" + page )

def device_ip() :
    clear()
    logo()
    time.sleep(2)
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    time.sleep(2)
    print(Fore.RED + "Please wait....")
    print(Fore.BLUE + " [ ~ ] Your ip is : " + Fore.RED +  str(ip))

def DDOS() :
  clear()
  logo()
  time,time.sleep(2)
  print(Fore.WHITE +"""
      --------------------------------------------------------------------------------------------------------------------------

   -t             Ping the specified host until stopped.
                   To see statistics and continue - type Control-Break;
                   To stop - type Control-C.
    -a             Resolve addresses to hostnames.
    -n count       Number of echo requests to send.
    -l size        Send buffer size.
    -f             Set Don't Fragment flag in packet (IPv4-only).
    -i TTL         Time To Live.
    -v TOS         Type Of Service (IPv4-only. This setting has been deprecated
                   and has no effect on the type of service field in the IP
                   Header).
    -r count       Record route for count hops (IPv4-only).
    -s count       Timestamp for count hops (IPv4-only).
    -j host-list   Loose source route along host-list (IPv4-only).
    -k host-list   Strict source route along host-list (IPv4-only).
    -w timeout     Timeout in milliseconds to wait for each reply.
    -R             Use routing header to test reverse route also (IPv6-only).
                   Per RFC 5095 the use of this routing header has been
                   deprecated. Some systems may drop echo requests if
                   this header is used.
    -S srcaddr     Source address to use.
    -c compartment Routing compartment identifier.
    -p             Ping a Hyper-V Network Virtualization provider address.
    -4             Force using IPv4.
    -6             Force using IPv6.


          --------------------------------------------------------------------------------------------------------------------------

  """)
  Target = str(input(" please Enter your taget: "))
  target_url = "ping" + " " + Target
  time.sleep(2)
  print(Fore.RED + " for cancle press CTRL + c")
  print("-----------------------------------")
  time.sleep(1)
  print(Fore.GREEN + "Attack started - target is:" + " " + Target)
  print("\r\n")
  while 1 > 0 :
    os.system(target_url)

def speed_test() :
  clear()
  logo()
  time.sleep(2)
  obj=Speedtest()
  print(Fore.BLUE  + f"download speed: {obj.download()}")
  print(Fore.YELLOW + f"upload speed: {obj.upload()}")
  os.system("pause")

def cctv_hack() :
    clear()
    logo()
    time.sleep(2)
    print(Fore.MAGENTA + """
        \033[1;31m1) \033[1;37mUnited States                \033[1;31m31) \033[1;37mMexico                \033[1;31m61) \033[1;37mMoldova
        \033[1;31m2) \033[1;37mJapan                        \033[1;31m32) \033[1;37mFinland               \033[1;31m62) \033[1;37mNicaragua
        \033[1;31m3) \033[1;37mItaly                        \033[1;31m33) \033[1;37mChina                 \033[1;31m63) \033[1;37mMalta
        \033[1;31m4) \033[1;37mKorea                        \033[1;31m34) \033[1;37mChile                 \033[1;31m64) \033[1;37mTrinidad And Tobago
        \033[1;31m5) \033[1;37mFrance                       \033[1;31m35) \033[1;37mSouth Africa          \033[1;31m65) \033[1;37mSoudi Arabia
        \033[1;31m6) \033[1;37mGermany                      \033[1;31m36) \033[1;37mSlovakia              \033[1;31m66) \033[1;37mCroatia
        \033[1;31m7) \033[1;37mTaiwan                       \033[1;31m37) \033[1;37mHungary               \033[1;31m67) \033[1;37mCyprus
        \033[1;31m8) \033[1;37mRussian Federation           \033[1;31m38) \033[1;37mIreland               \033[1;31m68) \033[1;37mPakistan
        \033[1;31m9) \033[1;37mUnited Kingdom               \033[1;31m39) \033[1;37mEgypt                 \033[1;31m69) \033[1;37mUnited Arab Emirates
        \033[1;31m10) \033[1;37mNetherlands                 \033[1;31m40) \033[1;37mThailand              \033[1;31m70) \033[1;37mKazakhstan
        \033[1;31m11) \033[1;37mCzech Republic              \033[1;31m41) \033[1;37mUkraine               \033[1;31m71) \033[1;37mKuwait
        \033[1;31m12) \033[1;37mTurkey                      \033[1;31m42) \033[1;37mSerbia                \033[1;31m72) \033[1;37mVenezuela
        \033[1;31m13) \033[1;37mAustria                     \033[1;31m43) \033[1;37mHong Kong             \033[1;31m73) \033[1;37mGeorgia
        \033[1;31m14) \033[1;37mSwitzerland                 \033[1;31m44) \033[1;37mGreece                \033[1;31m74) \033[1;37mMontenegro
        \033[1;31m15) \033[1;37mSpain                       \033[1;31m45) \033[1;37mPortugal              \033[1;31m75) \033[1;37mEl Salvador
        \033[1;31m16) \033[1;37mCanada                      \033[1;31m46) \033[1;37mLatvia                \033[1;31m76) \033[1;37mLuxembourg
        \033[1;31m17) \033[1;37mSweden                      \033[1;31m47) \033[1;37mSingapore             \033[1;31m77) \033[1;37mCuracao
        \033[1;31m18) \033[1;37mIsrael                      \033[1;31m48) \033[1;37mIceland               \033[1;31m78) \033[1;37mPuerto Rico
        \033[1;31m19) \033[1;37mIran                        \033[1;31m49) \033[1;37mMalaysia              \033[1;31m79) \033[1;37mCosta Rica
        \033[1;31m20) \033[1;37mPoland                      \033[1;31m50) \033[1;37mColombia              \033[1;31m80) \033[1;37mBelarus
        \033[1;31m21) \033[1;37mIndia                       \033[1;31m51) \033[1;37mTunisia               \033[1;31m81) \033[1;37mAlbania
        \033[1;31m22) \033[1;37mNorway                      \033[1;31m52) \033[1;37mEstonia               \033[1;31m82) \033[1;37mLiechtenstein
        \033[1;31m23) \033[1;37mRomania                     \033[1;31m53) \033[1;37mDominican Republic    \033[1;31m83) \033[1;37mBosnia And Herzegovia
        \033[1;31m24) \033[1;37mViet Nam                    \033[1;31m54) \033[1;37mSloveania             \033[1;31m84) \033[1;37mParaguay
        \033[1;31m25) \033[1;37mBelgium                     \033[1;31m55) \033[1;37mEcuador               \033[1;31m85) \033[1;37mPhilippines
        \033[1;31m26) \033[1;37mBrazil                      \033[1;31m56) \033[1;37mLithuania             \033[1;31m86) \033[1;37mFaroe Islands
        \033[1;31m27) \033[1;37mBulgaria                    \033[1;31m57) \033[1;37mPalestinian           \033[1;31m87) \033[1;37mGuatemala
        \033[1;31m28) \033[1;37mIndonesia                   \033[1;31m58) \033[1;37mNew Zealand           \033[1;31m88) \033[1;37mNepal
        \033[1;31m29) \033[1;37mDenmark                     \033[1;31m59) \033[1;37mBangladeh             \033[1;31m89) \033[1;37mPeru
        \033[1;31m30) \033[1;37mArgentina                   \033[1;31m60) \033[1;37mPanama                \033[1;31m90) \033[1;37mUruguay
                                                                \033[1;31m91) \033[1;37mExtra
    """)
        
    try:
        print()
        countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                    "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                    "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                    "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                    "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                    "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                    "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                    "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                    "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                    "-"]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75"}

        num = int(input("OPTIONS : "))
        if num not in range(1, 91+1):
            raise IndexError

        country = countries[num-1]
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}", headers=headers
        )
        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

        for page in range(int(last_page)):
            res = requests.get(
                f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
                headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
            for ip in find_ip:
                print("\033[1;31m", ip)
                f = open('cam-ip.txt' ,'w')
                f.write(ip + "\r\n")
    except:
        pass
    finally:
        print("\033[1;37m")

def check_number() :
    clear()
    logo()
    time.sleep(2)
    x = parse(input(Fore.GREEN +"what is your number? "))
    x= int(x)
    timezone = timezone.time_zones_for_number(x)
    print("\r\n")

    print(Fore .RED + " ur opration is:  " + Fore.GREEN +  carrier.name_for_number(x,lang="en"))
    # print(Fore .RED + " ur country is:   " + Fore.GREEN +  carrier.name_for_valid_number(x,lang="en"))  =>  opation
    print(Fore .RED + " ur country is:   " + Fore.GREEN +  geocoder.description_for_number(x,lang="en"))
    # print(Fore .RED + " ur country is:   " + Fore.GREEN +  geocoder.country_name_for_number(x,lang="en"))  => country

    print(Fore.WHITE + "##################################################################################################")
    print(Fore.WHITE)
    print( f"validation: {is_valid_number(x)} ")
    print(timezone)

def server():
    clear()
    logo()
    time.sleep(2)
    print("")

def pass_maker():
    clear()
    logo()
    time.sleep(2)
    Aleph = "abcdefghijklmnpqrstuvwxyz"
    U_Aleph = "ABCDEFGHIJKLMNPQRSTUVWXYZ"
    Num = "1234567890"
    sign = "!@#$%^&*(){}[]"
    
    f = open('result-pass.txt','a')
    x = Aleph + U_Aleph + Num + sign
    len = input("yourpassword lenght: ")
    result = "".join(random.sample(x , int(len)))

    time.sleep(5)
    print(Fore.YELLOW + "----------------------------------------------------")
    print(Fore.GREEN +  result)
    print(Fore.YELLOW + "----------------------------------------------------")
    f.write(result + "\r\n")
    os.system("pause")

def fake() :
    clear()
    print(Fore.LIGHTGREEN_EX + """
                    ...                                 ..                                                
            .Y#&&@@: ?PPPPGPY:                  :5#&&@& .GGGGGGGG7.GGGGGGGG7 YP555J!:   !#BBG         
            .&@@@@&#: B@@@BG@@@7                :&@@@@&B :@@@@@@@@P^@@@@@@@@P &@@@##@@B  J@@@@.        
            ^@@@@Y    G@@@J^@@@&                ?@@@@7   .G#@@@@BG?.G#@@@@BG7 &@@@::@@@: J@@@&         
            .&@@@&G^  G@@@J^@@@@.               :@@@@&P.   :@@@@:    :@@@@.   &@@@B&@@#  J@@@&         
            :B@@@@@! G@@@?~@@@&.                ^#@@@@@:  :@@@@:    :@@@@.   &@@@@@@@^  ?@@@&         
            .  ^&@@@G G@@@?Y@@@B :##&J          .  !@@@@J  :@@@@.    :@@@&.   #@@@Y&@@#. 7@@@&         
            ~@&&@@@@^ G@@@&@@@&: :@@@# .??????^ J@&&@@@&.  :@@@@.    :@@@&    #@@@~:@@@J ~@@@&         
            .B&&&#P:  !GPPGPY!   .&&&B !@@@@@@# :#&&&#Y.   .PGGP     .GGG5    7GP5. ~G^  :#GGY         
                                        ~@&&&&@B                                                        

    """ + Fore.RESET)
    fake = Faker()
    F_name = fake.first_name()
    L_name = fake.last_name()
    city = fake.city()
    street = fake.street_name()
    bulding_num = fake.building_number()
    email = fake.ascii_email()
    phone = fake.msisdn()
    contry =  fake.country()
    current_contry = fake.current_country()
    postcode = fake.postcode()
    compony = fake.company()
    phone_contry_code = fake.country_calling_code()
    credit_expire = fake.credit_card_expire()
    credit_number = fake.credit_card_number()
    credit_provider  =   fake.credit_card_provider()
    credit_pass =  fake.credit_card_security_code()
    job = fake.job()
    windows = fake.windows_platform_token() 
    linux = fake.linux_platform_token()
    ios  =  fake.ios_platform_token()
    mac =  fake.mac_platform_token()
    android = fake.android_platform_token()
    print(Fore.GREEN +  " [ + ] " + Fore.YELLOW + "your request was sumbit...! \r\n")
    time.sleep(1)
    print(Fore.GREEN +  " [ + ] " + Fore.YELLOW + "generate information.... \r\n")
    time.sleep(2)
    print(Fore.GREEN +  " [ + ] " + Fore.YELLOW + "please wait ... \r\n")
    time.sleep(4)
    print(Fore.LIGHTYELLOW_EX + """
                        ########################################################################
                                                instagram : sd._sttri       
                        ########################################################################


    """)
    print(Fore.YELLOW + " [  ]  first name: " + Fore.CYAN + F_name)
    print(Fore.YELLOW + " [ + ]  last name: " + Fore.CYAN + L_name)
    print(Fore.YELLOW + " [ + ]  email: " + Fore.CYAN + email)
    print(Fore.YELLOW + " [ + ]  phone number: " + Fore.CYAN + phone)
    print(Fore.YELLOW + " [ + ]  email: " + Fore.CYAN + phone_contry_code)
    print(Fore.YELLOW + " [ + ]  contry: " + Fore.CYAN + contry)
    print(Fore.YELLOW + " [ + ]  current contry: " + Fore.CYAN + current_contry)
    print(Fore.YELLOW + " [ + ]  city: " + Fore.CYAN + city)
    print(Fore.YELLOW + " [ + ]  street: " + Fore.CYAN + street)
    print(Fore.YELLOW + " [ + ]  bulding number: " + Fore.CYAN + bulding_num)
    print(Fore.YELLOW + " [ + ]  post code: " + Fore.CYAN + postcode)
    print(Fore.YELLOW + " [ + ]  compony: " + Fore.CYAN + compony)
    print(Fore.YELLOW + " [ + ]  job: " + Fore.CYAN + job)
    print(Fore.YELLOW + " [ + ]  credit provider: " + Fore.CYAN + credit_provider)
    print(Fore.YELLOW + " [ + ]  credit number: " + Fore.CYAN + credit_number)
    print(Fore.YELLOW + " [ + ]  credit expire: " + Fore.CYAN + credit_expire)
    print(Fore.YELLOW + " [ + ]  credit password: " + Fore.CYAN + credit_pass)
    print(Fore.YELLOW + " [ + ]  windows: " + Fore.CYAN + windows)
    print(Fore.YELLOW + " [ + ]  mac version: " + Fore.CYAN + mac)
    print(Fore.YELLOW + " [ + ]  ios version: " + Fore.CYAN + ios)
    print(Fore.YELLOW + " [ + ]  linux version: " + Fore.CYAN + linux)

def about_me() :
    clear()
    logo()
    time.sleep(2)
    print("")

def exit():
    clear()
    logo()
    time.sleep(2)
    print(Fore.CYAN + """
                    ...................................................................


                                        THANKS FOR USING MY TOOL :) 

                                        HOPE TO SEE YOU AGAIN ; )

                                        
                    ...................................................................

    """)
    time.sleep(2)
    os.system("exit")

if ( tools == "1" ) :
    pass_maker()
elif  ( tools == "2" ) :
    DDOS()
elif  ( tools == "3" ) :
    admin_search()
elif  ( tools == "4" ) :
    speed_test()
elif  ( tools == "5" ) :
    fake()
    os.system("pause")
elif  ( tools == "6" ) :
    device_ip()
elif  ( tools == "7" ) :
    print(Fore.BLUE + " we update this tool sonn .")
    # check_number()
elif  ( tools == "8" ) :
    # cctv_hack()
    print(Fore.BLUE + " we update this tool sonn .")

elif  ( tools == "9" ) :
    print(Fore.BLUE + " we update this tool sonn .")
    # server()
elif  ( tools == "10" ) :
    exit()
else: 
    print(Fore.RED + "ERROR!!!!")

