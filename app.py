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


line_bot_api = LineBotApi('gNvjfPRl6ab4VN6Y6lvYmS9emyJsHsqxKBh2GVASLcyZ5ZVbRavTt8kfzPTwJtIdQAJZ7sZsYhvGKr7kdidH3UMWtNXi3r0aE+T3TsPFNT67V4X8/D2sd3MANjDSiJsyP1AiW+R6jNX+jvk6iWzusgdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('522aa923d6da396c664d6220a2020f7c')

line_bot_api.push_message('', TextSendMessage(text='系統測試中，若您覺得訊息干擾到您，您可以將聊天室設為靜音，謝謝喔！'))

@app.route("/callback", methods=['POST'])
# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



######################處理LINE USER 傳來得訊息 ###############################


###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
