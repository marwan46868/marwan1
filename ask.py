
from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    try:
        data = request.json()
        mess = data.get('message', '')

        headers = {
            'authority': 'www.blackbox.ai',
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.blackbox.ai',
            'pragma': 'no-cache',
            'referer': 'https://www.blackbox.ai',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': ua.random,
        }

        cookies = {
            'sessionId': '0b7edce6-c44b-45d2-8215-378b7679081d',
            'render_app_version_affinity': 'dep-d02fksadbo4c73ept6lg',
            '__Host-authjs.csrf-token': 'dummy-token',
            '__Secure-authjs.callback-url': 'https%3A%2F%2Fwww.blackbox.ai',
        }

        json_data = {
            'messages': [{'id': 'kwlV6l6','content': mess,'role': 'user'}],
            'id': 'kwlV6l6',
            'codeModelMode': True,
            'imageGenerationMode': True,
            'validated': '00f37b34-a166-4efb-bce5-1312d87f2f94',
        }

        res = requests.post('https://www.blackbox.ai/api/chat', headers=headers, cookies=cookies, json=json_data)
        return {
            "statusCode": 200,
            "body": res.text
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
