import requests
import time
import json

headers = {
    'authority': 'baapi.nexon.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': '_gcl_au=1.1.1351697741.1687684482; _ga_T3QDF31F6C=GS1.1.1687684685.1.1.1687684725.20.0.0; _ga_099BZY6PMG=GS1.1.1687684685.1.1.1687684725.20.0.0; _ga=GA1.1.1647369321.1687684483; _ga_LEF7KNZLYK=GS1.1.1689930306.1.0.1689930306.60.0.0',
    'dnt': '1',
    'origin': 'https://bluearchive.nexon.com',
    'pragma': 'no-cache',
    'referer': 'https://bluearchive.nexon.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'macOS',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

data = {"n8Count": 1000}

while True:
    response = requests.post('https://baapi.nexon.com/api/events/2023/Event017/clicks', headers=headers, data=json.dumps(data))
    print(response.content) # print the response from the server
    time.sleep(1) # delay for 1 second
