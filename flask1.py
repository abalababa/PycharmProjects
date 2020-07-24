from flask import Flask

import requests
from json import loads

bot_server = Flask(__name__)

@bot_server.route('/api/message',methods=['POST'])
#路径是你在酷Q配置文件里自定义的
def server():
    data = requests.request.get_data().decode('utf-8')
    data = loads(data)
    print(data)
    return ''

if __name__ == '__main__':
    bot_server.run(port=5701)
    #端口也是你在酷Q配置文件里自定义的
