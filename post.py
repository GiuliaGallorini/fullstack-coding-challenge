from flask import Flask, render_template, request
import json
import requests


def make_post(data):
    UNBABEL_USERNAME = "fullstack-challenge"
    UNBABEL_API_KEY = "9db71b322d43a6ac0f681784ebdcc6409bb83359"

    headers = {
        "Authorization": "ApiKey {}:{}".format(UNBABEL_USERNAME, UNBABEL_API_KEY),
        'Content-Type': 'application/json',
    }

    data = json.dumps(data)
    print(f'DATA: {data}')

    resTrans = requests.post(
        'https://sandbox.unbabel.com/tapi/v2/translation/', headers=headers, data=data)
    return resTrans.json()

# print(f'POST resTrans: {resTrans}')
