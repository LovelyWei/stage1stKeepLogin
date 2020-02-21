import requests
import time
import random


error=0
while 1:
    cookie = {
    'B7Y9_2132_auth':'This is your auth',
    'B7Y9_2132_saltkey':'This is your slatkey'
}
    try:
        res = requests.get('https://bbs.saraba1st.com/2b/forum-75-1.html',cookies=cookie)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    except:
        time.sleep(60)
    if res.text.find('Test') != -1: # 替换成你的用户名
        print('['+now+'] '+'Logined')
        time.sleep(random.randint(120,480))
        if error!=0:
            error=0
    else:
        print('['+now+'] '+'Login failed!')
        error=error+1
        time.sleep(300)
        if error>=3:
            break
