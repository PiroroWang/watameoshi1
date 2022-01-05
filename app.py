# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:05:00 2020

@author: peishuo
"""

import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import QA_Col
import random

app = Flask(__name__)


line_bot_api = LineBotApi('xsJdbSEB9Xb6aL+/UHEjqK/EkIvOnZ4IIJXQ7zbne5uJw4v6pVF8zXI80Nunf1XrQAJZ7sZsYhvGKr7kdidH3UMWtNXi3r0aE+T3TsPFNT7ekppRzOycrVbE6189L8se3bzHY248syY8ilILP/ByZAdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('522aa923d6da396c664d6220a2020f7c')

line_bot_api.push_message('', TextSendMessage(text='系統測試中，若您覺得訊息干擾到您，您可以將聊天室設為靜音，謝謝喔！'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
