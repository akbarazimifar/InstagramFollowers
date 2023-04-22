from time import sleep
import requests,random,string
token = input ("Token : ")
id = input (" id tele : ")

class AbdullahIG():
    def __init__(self) -> None:
        self.hosturl = "https://www.instagram.com/"
        self.createurl = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
        self.ageurl = "https://www.instagram.com/web/consent/check_age_eligibility/"
        self.sendurl = "https://i.instagram.com/api/v1/accounts/send_verify_email/"
        self.checkcodeurl = "https://i.instagram.com/api/v1/accounts/check_confirmation_code/"
        self.createacc = "https://www.instagram.com/accounts/web_create_ajax/"
        self.session = requests.Session()
        self.session.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36', 'Referer': self.hosturl}
        self.session.proxies = {'http': requests.get("https://gimmeproxy.com/api/getProxy").json()['curl']}
        self.password = "King@kong"+str(random.randint(0,20))
        self.name = "Abdullah Coder"
        self.register()
    def register(self):
        self.reqB = self.session.get(self.hosturl)
        self.session.headers.update({'X-CSRFToken': self.reqB.cookies['csrftoken']})
        self.mail = self.getmail()
        self.mailss = self.mail[1]
        self.maile = self.mail[0]
        self.user = self.user_generator()
        self.data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:&:'+self.password,'email':self.maile,'username':self.user,'first_name':self.name,'client_id':'','seamless_login_enabled':'1','opt_into_one_tap':'false',}
        self.reg1 = self.session.post(url=self.createurl,data=self.data,allow_redirects=True)
        if(self.reg1.json()['status'] == 'ok'):
            print("Done send data")
        else:
            print("Error")
            exit("")
        self.data2 = {'day':'2','month':'2','year':'1983',}
        self.reqA = self.session.post(url=self.ageurl,data=self.data2,allow_redirects=True)
        if(self.reqA.json()['status'] == 'ok'):
            print("Done send date")
        else:
            print("Error")
            exit("")
        self.sendcode = self.session.post(url=self.sendurl,data={'device_id': '','email': self.maile},allow_redirects=True)
        if(self.sendcode.json()['status'] == 'ok'):
            print("Done send code")
        else:
            print("Error")
            exit("")
        while 1:
            self.inbox = self.getindox(self.mailss)
            if "Instagram" in self.inbox:
                code = self.inbox.split(" is")[0]
                print("Done Get Code : "+code)
                break     
            else:
                print("Getting a code ..")
                sleep(10)
                continue
        self.confirmation = self.session.post(url=self.checkcodeurl,data={'code': code,'device_id': '','email': self.maile})
        if self.confirmation.json()['status'] == "ok":
            signup_code = self.confirmation.json()['signup_code']
            print("Done Get signup code : "+signup_code)
            self.create = self.session.post(
                url=self.createacc,
                data={
'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+self.password,
'email': self.maile,
'username': self.user,
'first_name': self.name,
'month': '4',
'day': '4',
'year': '1963',
'client_id': '',
'seamless_login_enabled': '1',
'tos_version': 'row',
'force_sign_up_code': signup_code})
            if '"account_created": false' in self.create.text:
                print("There was a problem while creating the account")
            else:
                print(f"username : {self.user}\npassword : {self.password}\nEmail : {self.maile}")
                aboody = (f"""
                Hello Dear New instgram!
                === === === ===
                - He Username : {self.user}
                 -  He Password : {self.password}
                 - He Meile : {self.maile}
                 === === === ===
                 By : @anonsecteam
                 """)
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=\n {aboody}"
                i = requests.post(tlg)
        else:
            print("There was a problem while Getting signup code")
            exit("")
    def getmail(self):
        self.rem = requests.get("https://10minutemail.net/address.api.php")
        print("Done Get Email : "+self.rem.json()['mail_get_mail'])
        return self.rem.json()['mail_get_mail'],self.rem.cookies['PHPSESSID']
    def getindox(self,sessionid):
        self.rei = requests.get("https://10minutemail.net/address.api.php",cookies={"PHPSESSID":sessionid})
        return self.rei.json()['mail_list'][0]['subject']
    def user_generator(self):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
  
        
AbdullahIG()
