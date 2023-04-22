Black="\033[1;30m"       # Black
Red="\033[1;31m"         # Red
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White
import requests 
rs=requests.session()
from time import sleep  

def slep(s,done,error,privet):
	for i in range(s):
			v=s-i
			sleep(1)
			print(White+f'\r done{White}[{Green}{done}{White}] error[{Red}{error}{White}] privet[{Yellow}{privet}{White}] sleep[{v}]    ',end='')
#done[0] error [0] privet[0] sleep[0]

done,error,privet=0,0,0

def followers():
    done,error,privet=0,0,0
    ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={u}'
    header={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
    }
    req=requests.get(ur,headers=header)
    Id = str(req.json()['data']['user']['id'])
    



    url=f'https://i.instagram.com/api/v1/friendships/{Id}/followers/?count=1000'

    
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
    }
    req=requests.get(url,headers=headers)
    r=req.text
    print('\n'*3)
    print('   ====== started ======')
    print('\n'*3)

    for i in range(1,1000):
            global s
            slep(s,done,error,privet)
            sleep(s)
            a=r.split('"username"')[i]
            b=a.split('","')[0]
            c=b.split(':"')[1]
            
            
            ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={c}'
            header={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
            'x-frame-options': 'SAMEORIGIN'
            }
            req=requests.get(ur,headers=header)
            Id = str(req.json()['data']['user']['id'])
            if req.json()['data']['user']['is_private']==True:
            	privet=privet+1
    
            url = f'https://i.instagram.com/api/v1/web/friendships/{Id}/follow/'
            headers={
                'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length':'0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
            'x-asbd-id': '198387',
            'x-csrftoken': 'gmzL59SsdohJitq78RKPRimb9CirRCAV',
            'x-frame-options': 'SAMEORIGIN',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaJfy',
            'x-instagram-ajax': '1006124192'
            }
            
            a=requests.post(url,headers=headers).text
            
            if 'ok' in a:
                done=done+1
                s=j
            else:
                s=1000
                error=error+1






def following():
    done,error,privet=0,0,0
    ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={u}'
    header={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
    }
    req=requests.get(ur,headers=header)
    Id = str(req.json()['data']['user']['id'])
    



    url=f'https://i.instagram.com/api/v1/friendships/{Id}/followers/?count=1000'

    
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
    }
    req=requests.get(url,headers=headers)
    r=req.text
    print('\n'*3)
    print('   ====== started ======')
    print('\n'*3)

    for i in range(1,1000):
        
            a=r.split('"username"')[i]
            b=a.split('","')[0]
            c=b.split(':"')[1]
            
            
            global s
            slep(s,done,error,privet)
            sleep(s)
            
            
            ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={c}'
            header={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
            'x-frame-options': 'SAMEORIGIN'
            }
            req=requests.get(ur,headers=header)
            Id = str(req.json()['data']['user']['id'])
            if req.json()['data']['user']['is_private']==True:
            	privet=privet+1
    
            url = f'https://i.instagram.com/api/v1/web/friendships/{Id}/follow/'
            headers={
                'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length':'0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
            'x-asbd-id': '198387',
            'x-csrftoken': 'gmzL59SsdohJitq78RKPRimb9CirRCAV',
            'x-frame-options': 'SAMEORIGIN',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaJfy',
            'x-instagram-ajax': '1006124192'
            }
            
            a=requests.post(url,headers=headers).text
            
            if 'ok' in a:
                done=done+1
                s=j
            else:
                s=1000
                error=error+1
            
            












def unfollow_all():
    done,error,privet=0,0,0
    ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
    header={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
    }
    req=requests.get(ur,headers=header)
    Id = str(req.json()['data']['user']['id'])
    



    url=f'https://i.instagram.com/api/v1/friendships/{Id}/following/?count=1000'

    
    headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
    'x-frame-options': 'SAMEORIGIN'
    }
    req=requests.get(url,headers=headers)
    r=req.text
    print('\n'*3)
    print('   ====== started ======')
    print('\n'*3)

    for i in range(1,1000):
        
            a=r.split('"username"')[i]
            b=a.split('","')[0]
            c=b.split(':"')[1]
            
            
            global s
            slep(s,done,error,privet)
            
            sleep(s)
            
            ur=f'https://i.instagram.com/api/v1/users/web_profile_info/?username={c}'
            header={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
            'x-frame-options': 'SAMEORIGIN'
            }
            req=requests.get(ur,headers=header)
            Id = str(req.json()['data']['user']['id'])
            if req.json()['data']['user']['is_private']==True:
            	privet=privet+1
            
            url = f'https://i.instagram.com/api/v1/web/friendships/{Id}/unfollow/'
            headers={
                'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length':'0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'ig_did=8F988947-3014-45AD-BC93-30013743D49E; ig_nrcb=1; dpr=3; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; datr=CetDZOq-Gu_3Pkwj-JUmrG2a; csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ds_user_id=3244392844; shbid="6103\0543244392844\0541713708833:01f714d561fab88a59e651c1b4558c12129b9fe7ccb258557cab2c2cfae6eaaa2d5030ff"; shbts="1682172833\0543244392844\0541713708833:01f7051a2cc196c907e932f1222ef40f85b2028ecba30dc002425b63d43fce0607aa530b"; sessionid=3244392844%3APXGMWRWCeunTaM%3A15%3AAYdknLTQ989A5nli3aRXABcrtKvyBkx3FpFNcQzHpg; rur="EAG\0543244392844\0541713708868:01f7c7ec8a80d53017b70e90ba6fe5856faa635eb2bb589af33df54aa434e309cb204e17"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 231.0.0.18.113',
            'x-asbd-id': '198387',
            'x-csrftoken': 'gmzL59SsdohJitq78RKPRimb9CirRCAV',
            'x-frame-options': 'SAMEORIGIN',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0CTssDFfvaLymrF2w77U_v94Xm9xDN1zVkcHJhaK2vaJfy',
            'x-instagram-ajax': '1006124192'
            }
            
            a=requests.post(url,headers=headers).text
           
            if 'ok' in a:
                done=done+1
                s=j
            else:
                s=1000
                error=error+1
            
            
            



print(Red+f'''
{Yellow}
Github {Purple}: TahaluIndo{Yellow}
Team {Purple}: LulzGhost-Team
{Red}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠙⠻⢶⣄⡀⠀⠀⠀⢀⣤⠶⠛⠛⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⣙⣿⣦⣤⣴⣿⣁⠀⠀⣸⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣿⣿⣿⣿⣿⣷⣌⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡈⢻⣿⡟⢁⣠⣾⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠘⣿⠃⣿⣿⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠛⣰⠿⣆⠛⠁⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣦⠀⠘⠛⠋⠀⣴⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠾⢿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠟⠋⣁⣠⣤⣤⡶⠶⠶⣤⣄⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⣿⣿⣮⣉⣉⣉⣤⣴⣶⣿⣿⣋⡥⠄⠀⠀⠀⠀⠉⢻⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣁⣤⣀⣀⣤⣤⣤⣤⣄⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


{Red}[{White}1{Red}]{Yellow} - Of Followers 🚀
{Red}[{White}2{Red}]{Yellow} - Of Following 🤗
{Red}[{White}3{Red}]{Yellow} - Unfollow All 👊
{White}[{Red}99{White}]{Yellow} - Exit 💩
''')
print(White+f'\n\n= = = = = ={Yellow}  Choose  {White}= = = = = = ')
try :
	c=int(input(f'{Red}[{Yellow}+{Red}]{White} Choose : {White}'))
except :
	print('enter numper ! ')
	exit()
if c == 99:
	exit()
print(White+f'\n\n= = = = = ={Yellow}  Login Your Acc  {White}= = = = = = ')
username = input(f'{Red}[{Yellow}+{Red}]{White} Your  Username : {White}')
password = input(f'{Red}[{Yellow}+{Red}]{White} Your  Password : {White}')
s=int(input(f'{Red}[{Yellow}+{Red}]{White} Sleep : {White} '))
j=s
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=AmyABd91qyGnbFG2hHknp5Fvbjhfelnr; ig_did=3244392844; mid=ZEPrDQABAAEPmpwawFLPkiktsPey; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
    }
data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
    }    
r = rs.post(url, headers=headers, data=data)
if  'authenticated":true' in r.text or 'userId' in r.text:
    csrftoken=r.cookies['csrftoken']
    si=r.cookies['sessionid']
    id=r.cookies['ds_user_id']
if c == 1:
	print(White+f'\n\n= = = = = ={Yellow}  Username  {White}= = = = = = ')
	u=input(f'{Red}[{Yellow}+{Red}]{White} Username : {White}')
	followers()
elif c == 2 :
	print('\n\n= = = = = =  Username  = = = = = = ')
	u=input(f'{Red}[{Yellow}+{Red}]{White} Username : {White}')
	following()
elif c == 3 :
	unfollow_all()
