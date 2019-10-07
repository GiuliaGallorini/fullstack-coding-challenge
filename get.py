from flask import Flask, render_template, request
import time
import json
import requests


def make_get(uid):
    UNBABEL_USERNAME = "fullstack-challenge"
    UNBABEL_API_KEY = "9db71b322d43a6ac0f681784ebdcc6409bb83359"

    headers = {
        "Authorization": "ApiKey {}:{}".format(UNBABEL_USERNAME, UNBABEL_API_KEY),
        'Content-Type': 'application/json',
    }

    response = requests.get(
        'https://sandbox.unbabel.com/tapi/v2/translation/' + uid + '/', headers=headers)

    while 'status' not in response.json():
        time.sleep(1)
        response = requests.get(
            'https://sandbox.unbabel.com/tapi/v2/translation/' + uid + '/', headers=headers)

    while response.json()['status'] != "completed":
        time.sleep(1)
        # print('I AM CALLING')
        # GET a translation
        response = requests.get(
            'https://sandbox.unbabel.com/tapi/v2/translation/' + uid + '/', headers=headers)

    # print(f'GET A DICT: {response.json()}')
    return response.json()
