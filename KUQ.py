import requests
data = {
    'user_id':1292175248,
    'message':'我是一个可爱的小机器人喵~',
    'auto_escape':False
}

api_url = 'http://127.0.0.1:12801/send_private_msg'
#酷Q运行在本地，端口为5700，所以server地址是127.0.0.1:5700

r = requests.post(api_url,data=data)
print(r.text)