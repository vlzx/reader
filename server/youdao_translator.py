import os
import uuid
import httpx
import hashlib
import time

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = os.getenv('YOUDAO_APPID')
APP_SECRET = os.getenv('YOUDAO_SECRET')


def encrypt(sign: str):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(sign.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q: str):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


async def translate(text: str):
    salt = str(uuid.uuid4())
    curtime = str(int(time.time()))
    signStr = APP_KEY + truncate(text) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)

    payload = {
        'q': text,
        'from': 'auto',
        'to': 'zh-CHS',
        'appKey': APP_KEY,
        'salt': salt,
        'sign': sign,
        'signType': 'v3',
        'curtime': curtime
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    async with httpx.AsyncClient() as client:
        response = await client.post(YOUDAO_URL, data=payload, headers=headers)
    # print(response.json())
    result = response.json()
    translation = []
    if result['errorCode'] == '0':
        translation = result['translation']
    return {'code': result['errorCode'], 'translation': translation}


if __name__ == '__main__':
    print(translate('寿司を食べたい'))
