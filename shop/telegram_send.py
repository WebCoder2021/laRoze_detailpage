import requests
token='5767239118:AAGdU1nyf9OIhT-X0keRz-EV5DslQKKhro4'
chat_id='-1001554357416'


def send_order(text,img=None):
    if img:
        resp = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&text={text}&parse_mode=html',files=img)
    else: resp = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}&parse_mode=html')
    print(text)
    print(resp)
    return resp
    