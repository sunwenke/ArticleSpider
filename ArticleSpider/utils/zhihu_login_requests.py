import requests
try:
    import cookielib  #py2
except:
    import http.cookiejar as cookielib    #py3

import re

agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0"
header = {
    "HOST":"www.zhihu.com",
    "Referer":"https://www.zhihu.com",
    "User-Agent": agent
}
def get_xsrf():
    #获取xsrf code
    response = requests.get("https://www.zhihu.com", headers = header)
    print (response.text)
    text= '<input type="hidden" name="_xsrf" value="e697e3b6d7dcbb80616c14e95eda94fd"/>'
    match_obj = re.match('.*name="_xsrf" value="(.*?)"',text)
    if match_obj:
        print(match_obj.group(1))
    else:
        return ""


    # with open("index_page.html", "wb") as f:
    #     f.write(response.text.encode("utf-8"))
    # print ("ok")

def zhihu_login(account, password):
    #知乎登录
    if re.match("^1\d{10}",account):
        print ("手机号码登录")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf": get_xsrf(),
            "phone_num": account,
            "password": password
        }

        requests.post(post_url, date=post_data, headers=header)

    else:
        if "@" in account:
            #判断用户名是否为邮箱
            print("邮箱方式登录")
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": get_xsrf(),
                "email": account,
                "password": password
            }

get_xsrf()
