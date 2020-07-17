# -*- coding: utf-8 -*-
"""
Created on Fri July 15 2020

@author: wandereryeh
"""

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('iV2OXMJ2HNRPzxsC12MmZQ2YzSw62Hgq5YyWMtQjOjMcfFhnL0bma+FnntoSVk9Rbx3JrlXxzAN/e/r5HXNVO3+NGERE0pM2BJHEXjmr51wFLp6YW/Kjue8tjy2m8wALtpUV5L5QHFrBG97CRpi6MgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('f72d0c623547e1af685b4698b4cfae03')

line_bot_api.push_message('U001571421ef73fd8b6f0d8cde5f68391', TextSendMessage(text='伺服器已啟動'))

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #line_bot_api.reply_message(
     #   event.reply_token,
      #  TextSendMessage(text=event.message.text))
    if event.message.text == "Help":
        line_bot_api.reply_message(event.reply_token, buttons_template())
    elif event.message.text == "掛號":
        line_bot_api.reply_message(event.reply_token, buttons_template2())
    elif event.message.text == "一般掛號":
        line_bot_api.reply_message(event.reply_token, buttons_template3())
    elif event.message.text == "電話掛號":
        line_bot_api.reply_message(event.reply_token, buttons_template4())

def buttons_template(): 
    buttons = TemplateSendMessage(
            alt_text='功能選單',
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

def buttons_template2(): 
    buttons = TemplateSendMessage(
            alt_text='掛號方式',
            template=ButtonsTemplate(
                    title='請選擇掛號方式',
                    text='電話掛號&一般掛號',
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                actions=[
                     MessageTemplateAction(
                        label='一般掛號',
                        text='一般掛號'
                    ), 
                     MessageTemplateAction(
                        label='電話掛號',
                        text='電話掛號'
                    )
                ]
            )
    ) 
    return buttons
def buttons_template3(): 
    buttons = TemplateSendMessage(
            alt_text='一般掛號',
            template=ButtonsTemplate(
                    title='初診/複診'',
                    text='妳是初診還是複診',
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                actions=[
                     MessageTemplateAction(
                        label='初診',
                        text='初診'
                    ), 
                     MessageTemplateAction(
                        label='複診',
                        text='複診'
                    )
                ]
            )
    ) 
    return buttons
if __name__ == "__main__":
    app.run()