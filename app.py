# -*- coding: utf-8 -*-
"""
Created on Fri July 15 2020

@author: wandereryeh
"""


from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import mongodb
import re
import schedule
import urllib.parse
import datetime
from bs4 import BeautifulSoup
import time


app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('')
# 必須放上自己的Channel Secret
handler = WebhookHandler('')

#line_bot_api.push_message('Uc52a42025be949ba1b1e0654d6536122', TextSendMessage(text='啟動'))

# 監聽所有來自 /callback 的 Post Request
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

#訊息傳遞區塊
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    usespeak=str(event.message.text) #使用者講的話
    if event.message.text == "Help": 
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://imgur.com/VHAAgdU.png', preview_image_url='https://imgur.com/VHAAgdU.png'))
    elif event.message.text == "help":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://imgur.com/NTFTH3d.png', preview_image_url='https://imgur.com/o8WuFjh.png'))

def buttons_template(): #尚未更正: 其他使用者看不到請輸入..
    buttons = TemplateSendMessage(
            alt_text='Help',
            template=ButtonsTemplate(
                    title='請選擇服務功能',
                    text='此APP提供以下功能',
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                actions=[
                     MessageTemplateAction(
                        label='掛號',
                        text='掛號'
                    ), 
                     MessageTemplateAction(
                        label='診所',
                        text='診所'
                    ),
                     MessageTemplateAction(
                        label='醫院',
                        text='醫院'
                    ) 
                ]
            )
    ) 
    return buttons


if __name__ == '__main__':
    app.run(debug=True)