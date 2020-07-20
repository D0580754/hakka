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
    elif event.message.text == "診所":
        line_bot_api.reply_message(event.reply_token, buttons_template5())
    elif event.message.text == "初診":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：第一次來嗎？\n櫃檯：第一擺來係無？\n病人：是的。\n病人：係。\n櫃檯：麻煩填一下資料。\n櫃檯：麻煩填一下資料。\n病人：好的。\n病人：好。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://www.sample-videos.com/audio/mp3/crowd-cheering.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
    elif event.message.text == "複診":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：第一次來嗎？\n櫃檯：第一擺來係無？\n病人：不是，之前來過了。\n病人：毋係，以前有來過。\n櫃檯：麻煩給我您的健保卡。\n櫃檯：麻煩分??你?健保卡。\n病人：好的，在這裡。\n病人：好，在這裡位。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/abafcb0e-e190-ce77-6964-625a915d20fc.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
    elif event.message.text == "電話掛號1":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：你好，這裡是新生診所。\n櫃檯：你好，這位係新生診所。\n病人：請問可以電話預約嗎？\n病人：請問做得用電話先掛號無？\n櫃檯：可以，麻煩給我你的身分證字號。\n櫃檯：做得，麻煩分??你?身分證號碼。\n病人：好的，A123456789\n病人：好，A123456789。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/abafcb0e-e190-ce77-6964-625a915d20fc.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
    elif event.message.text == "電話掛號2":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：你好，這裡是新生診所。\n櫃檯：你好，這位係新生診所。\n病人：請問可以電話預約嗎？\n病人：請問做得電話先掛號無？\n櫃檯：不可以喔,必須現場掛好。\n櫃檯：做毋得哦！一定愛現場掛號。\n病人：好的\n病人：好。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/abafcb0e-e190-ce77-6964-625a915d20fc.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
    elif event.message.text == "電話掛號3":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：目前編號是30號，你的編號是40號。\n櫃檯：目前?號碼係30號，你?號碼係40號。\n病人：謝謝。\n病人：恁仔細/承蒙你。\n櫃檯：大約30分鐘後就輪到你，建議你提早過來。\n櫃檯：大約30分鐘過後就輪到你，建議你提早兜過來。\n病人：好的，10分鐘後過去，謝謝\n病人：好，10分鐘後會過去，恁仔細/承蒙你。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/abafcb0e-e190-ce77-6964-625a915d20fc.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
    elif event.message.text == "身心科":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：目前編號是30號，你的編號是40號。\n櫃檯：目前?號碼係30號，你?號碼係40號。\n病人：謝謝。\n病人：恁仔細/承蒙你。\n櫃檯：大約30分鐘後就輪到你，建議你提早過來。\n櫃檯：大約30分鐘過後就輪到你，建議你提早兜過來。\n病人：好的，10分鐘後過去，謝謝\n病人：好，10分鐘後會過去，恁仔細/承蒙你。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/abafcb0e-e190-ce77-6964-625a915d20fc.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
    elif event.message.text == "小兒科":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='醫生：您好寶寶怎麼了?\n醫生：你好！嬰兒仔有仰般係無?\n家屬：最近屁股紅紅的、有破皮，換尿布都會哭。\n家屬：最近屎朏紅紅、有爛皮，換尿布都會噭。\n醫生：讓我打開尿布看寶寶的臀部。\n醫生：分??打開尿布看嬰兒仔?屎朏。\n家屬：好的。\n家屬：好。\n醫生：這是尿布疹。\n醫生：這係尿布疹。\n家屬：甚麼是尿布疹。\n家屬：麼?係尿布疹。\n醫生：太長時間沒更換尿布，所導致的。\n醫生：時間忒長無換尿布，所因致?。\n家屬：我該怎麼辦?\n家屬：該??愛仰般？\n醫生：勤換尿布，保持乾爽，別使用爽身粉。\n醫生：愛較輒兜換尿布，保持燥爽，毋好用爽身粉。\n家屬：為甚麼不能用爽身粉，這樣不是可以更乾爽嗎?\n家屬：做麼?毋好用爽身粉，恁樣敢毋係做得較燥爽乜?\n醫生：尿液及糞便加上爽身粉會沾附皮膚，使皮膚不透氣。\n醫生：該尿摎大便加上爽身粉會黏在皮膚，皮膚就毋會透氣。\n家屬：我了解。\n家屬：??了解。\n醫生：開個藥膏給寶寶使用，少量擦。\n醫生：開隻藥膏分嬰兒仔使用，愛少量兜仔膏。\n家屬：好的，謝謝醫生。\n家屬：好，承蒙醫生。'))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/abafcb0e-e190-ce77-6964-625a915d20fc.mp3', duration=100000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='http://163.25.34.177/Upload/Audio/08f43665-c5fe-a5b1-6c1e-14a5dc75f432.mp3', duration=100000))
def buttons_template(): 
    buttons = TemplateSendMessage(
            alt_text='功能選單',
            template=ButtonsTemplate(
                    title='請選擇服務功能',
                    text='此APP提供以下功能',
                thumbnail_image_url='https://imgur.com/Hz1DDhu.jpg',
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
                    title='初診/複診',
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
def buttons_template4(): 
    buttons = TemplateSendMessage(
            alt_text='電話掛號',
            template=ButtonsTemplate(
                    title='電話掛號',
                    text='電話掛號',
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                actions=[
                     MessageTemplateAction(
                        label='電話掛號1',
                        text='電話掛號1'
                    ), 
                     MessageTemplateAction(
                        label='電話掛號2',
                        text='電話掛號2'
                    ),
                    MessageTemplateAction(
                        label='電話掛號3',
                        text='電話掛號'
                    )
                ]
            )
    ) 
    return buttons
def buttons_template5(): 
    buttons = TemplateSendMessage(
            alt_text='診所選擇'',
            template=ButtonsTemplate(
                    title='診所選擇',
                    text='診所選擇',
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                actions=[
                     MessageTemplateAction(
                        label='身心科',
                        text='身心科'
                    ), 
                     MessageTemplateAction(
                        label='小兒科',
                        text='小兒科'
                    )
                ]
            )
    ) 
    return buttons
if __name__ == "__main__":
    app.run()