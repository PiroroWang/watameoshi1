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


line_bot_api = LineBotApi('4Wqfqtn7bLGCno3diBfYQUUd1cACeiV7DR17OyrzhBeFwh7NlhXmKO9IEE20eagny+d2H2aJiDYxLaEjhegfws3uY8+hcccOpz/q+XfAjyLHin8qV/M9dg6LH+3Hf0RmmA4F/qVoCpF5ZXanZUTk7wdB04t89/1O/w1cDnyilFU=')

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

######################處理LINE USER 傳來得訊息 ###############################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    
    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name     #使用者名稱
    uid = profile.user_id             #使用者ID  
    user_message=str(event.message.text) 
    

        #user_message='圖文訊息'
    if user_message.find('WTM') != -1:    
        
        res_message = TemplateSendMessage(
            alt_text='わため推廣主選單',
            template=ButtonsTemplate(
                thumbnail_image_url='https://images.plurk.com/4wqrmDmQcXOcQYHpoPN8bq.jpg', 
                title='わため推廣主選單',
                text='依照需要的資訊選擇下面的按鈕',
                actions=[
                    URITemplateAction(
                        label='現正直播',
                        uri='https://www.youtube.com/channel/UCqm3BQLlJfvkTsX_hvm0UmA/live'
                        ),
                    URITemplateAction(
                        label='官方推特',
                        uri='https://twitter.com/tsunomakiwatame'
                        ),

###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
