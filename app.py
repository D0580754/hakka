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
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
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
    elif event.message.text == "身心科":
        line_bot_api.reply_message(event.reply_token, buttons_template6())
    elif event.message.text == "醫院":
        line_bot_api.reply_message(event.reply_token, buttons_template7())
    elif event.message.text == "內科":
        line_bot_api.reply_message(event.reply_token, buttons_template8())
    elif event.message.text == "手術":
        line_bot_api.reply_message(event.reply_token, buttons_template9())
    elif event.message.text == "急診":
        line_bot_api.reply_message(event.reply_token, carousel_template())  
    elif event.message.text == "泌尿科":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好哪不舒服?\n醫生：你好！哪位有毋鬆爽？\n病人：醫生最近一直解尿很不順。\n病人：醫生，恁久一直屙尿盡毋順。\n醫生：怎麼解尿不順說說看！\n醫生：係仰般屙尿毋順，試講看啊！\n病人：一直想尿可是去了廁所又一直尿不出來。\n病人：緊想屙尿毋過行到便所又屙毋出來。\n醫生：這情況多久了?\n醫生：這種情形有幾久咧。\n病人：最近幾年越來越嚴重。\n病人：最近幾年越來越嚴重。\n醫生：晚上睡覺會一直想解尿嗎?\n醫生：暗晡時睡目會緊想愛屙尿無?\n病人：晚上更誇張，躺下就想尿。\n病人：暗晡時還較誇張，睡下去就想愛屙尿。\n醫生：那有解出來嗎?\n醫生：該有屙出來無?\n病人：在廁所努力很久也只尿出一點點。\n病人：在便所企當久也還係屙出一點仔定。\n醫生：一個晚上這種情形會有幾次?\n醫生：這種情形一暗晡會有幾多到?\n病人：至少10次以上，整晚沒睡。\n病人：至少10到以上，歸暗晡無睡。\n醫生：聽你的描述，像是攝護腺肥大。\n醫生：聽你講?，像人係攝護腺肥大。\n病人：甚麼是攝護腺肥大?\n病人：麼?係攝護腺肥大？\n醫生：攝護腺肥大其實簡單來說就是尿道狹窄。\n醫生：攝護腺肥大其實簡單來講就係尿道變狹。\n病人：甚麼是尿道狹窄?\n病人：麼?係尿道變狹？\n醫生：尿道狹窄就是良性攝護腺肥大因壓迫到膀胱及尿道。\n醫生：尿道變狹就係良性攝護腺肥大，因為壓迫著膀胱摎尿道。\n病人：原來是這樣，難怪我尿得很辛苦。\n病人：原來係恁樣，難怪??屙尿屙到恁辛苦。\n醫生：是的，所以才會夜尿多次。\n醫生：係啊！所以正會暗晡時愛?起來屙恁多到。\n病人：那要如何確定?\n病人：該愛仰般來確定？\n醫生：一般確定診斷方式常見是肛門指診。\n醫生：一般確定診斷方式，較常用?係肛門指診。\n病人：現在就可以判斷嗎?\n病人：這下就做得判斷無?\n醫生：等會我會將手指伸入肛門，請放輕鬆比較不會有異物感。\n醫生：等加下??會將手指伸入肛門，請你放較輕鬆兜，毋使緊張。\n病人：我知道了。\n病人：??知咧。\n醫生：剛進行肛門指診結果，確定是攝護腺肥大。\n醫生：頭下進行肛門指診?結果，確定係攝護腺肥大。\n病人：那我該怎麼辦?\n病人：該??愛仰般？\n醫生：目前先吃藥。\n醫生：目前先食藥仔。\n病人：吃藥會好嗎?\n病人：食藥仔會好無?\n醫生：一般吃藥若沒改善可考慮手術方式。\n醫生：一般食藥仔若係無改善，做得考慮手術。\n病人：甚麼手術?\n病人：麼?手術？\n醫生：手術方式利用雷射光將多餘攝護腺組織瞬間氣化，達到治療效果。\n醫生：手術?方式係利用雷射光將多餘?攝護腺組織摎佢瞬間氣化，達到治療?效果。\n病人：那會很痛嗎?會流血嗎?\n病人：該會當痛無?會流血無?\n醫生：手術過程出血量及少，會輕微疼痛需住院一晚。\n醫生：手術?過程出血量極少，會有多少仔痛，愛住院一暗晡。\n病人：那目前我的情形先吃藥就可以嗎?\n病人：該目前???情形，先食藥就做得係無?\n醫生：先吃藥。\n醫生：先食藥仔。\n病人：吃多久?\n病人：愛食幾久？\n醫生：若解尿情形有比較改善，則藥物則有療效。\n醫生：若係屙尿?情形有較改善，該藥仔就有效果。\n病人：我了解了。\n病人：??了解咧，恁仔細／承蒙你。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/giyv102ziwivshg/%E6%B3%8C%E5%B0%BF%E6%B5%B7%E9%99%B8.m4a', duration=170000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/gpf0nchk99b7rek/%E6%B3%8C%E5%B0%BF%E5%9B%9B%E7%B8%A3.m4a', duration=170000))       
    elif event.message.text == "初診":
        line_bot_api.push_message(uid, TextSendMessage('櫃檯：第一次來嗎？\n櫃檯：第一擺來係無？\n病人：是的。\n病人：係。\n櫃檯：麻煩填一下資料。\n櫃檯：麻煩填一下資料。\n病人：好的。\n病人：好。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropboxusercontent.com/s/wr2r5hjjetuxd5s/abafcb0e-e190-ce77-6964-625a915d20fc%20%28online-audio-converter.com%29.m4a', duration=14000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/lnrabyvq0rgjdvb/%E8%A4%87%E8%A8%BA%E6%B5%B7%E9%99%B8%20%28online-audio-converter.com%29.m4a', duration=14000))
    elif event.message.text == "複診":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='櫃檯：第一次來嗎？\n櫃檯：第一擺來係無？\n病人：不是，之前來過了。\n病人：毋係，以前有來過。\n櫃檯：麻煩給我您的健保卡。\n櫃檯：麻煩分??你?健保卡。\n病人：好的，在這裡。\n病人：好，在這裡位。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/oslhnkms01zr6p9/%E8%A4%87%E8%A8%BA%E6%B5%B7%E9%99%B8.m4a', duration=14000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/69opf85vgcmmdn6/%E8%A4%87%E8%A8%BA%E5%9B%9B%E7%B8%A3.m4a', duration=14000))        
    elif event.message.text == "電話掛號1":
        line_bot_api.push_message(uid, TextSendMessage('櫃檯：你好，這裡是新生診所。\n櫃檯：你好，這位係新生診所。\n病人：請問可以電話預約嗎？\n病人：請問做得用電話先掛號無？\n櫃檯：可以，麻煩給我你的身分證字號。\n櫃檯：做得，麻煩分??你?身分證號碼。\n病人：好的，A123456789\n病人：好，A123456789。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/yro6rm2h1rk2zob/%E9%9B%BB%E8%A9%B11%E6%B5%B7%E9%99%B8.m4a', duration=22000))
        #line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropboxusercontent.com/s/lqpabvzcni2mpc9/%E9%9B%BB%E8%A9%B11%E5%9B%9B%E7%B8%A3.m4a', duration=19000))
    elif event.message.text == "電話掛號2":
        line_bot_api.push_message(uid, TextSendMessage('櫃檯：你好，這裡是新生診所。\n櫃檯：你好，這位係新生診所。\n病人：請問可以電話預約嗎？\n病人：請問做得電話先掛號無？\n櫃檯：不可以喔,必須現場掛好。\n櫃檯：做毋得哦！一定愛現場掛號。\n病人：好的\n病人：好。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/lm5w282bx706gqf/%E9%9B%BB%E8%A9%B12%E6%B5%B7%E9%99%B8.m4a', duration=17000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/u4kn6zza93rngbz/%E9%9B%BB%E8%A9%B12%E5%9B%9B%E7%B8%A3.m4a', duration=17000))
    elif event.message.text == "電話掛號3":
        line_bot_api.push_message(uid, TextSendMessage('櫃檯：目前編號是30號，你的編號是40號。\n櫃檯：目前?號碼係30號，你?號碼係40號。\n病人：謝謝。\n病人：恁仔細/承蒙你。\n櫃檯：大約30分鐘後就輪到你，建議你提早過來。\n櫃檯：大約30分鐘過後就輪到你，建議你提早兜過來。\n病人：好的，10分鐘後過去，謝謝\n病人：好，10分鐘後會過去，恁仔細/承蒙你。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/7w7s6kjdx340xqs/%E9%9B%BB%E8%A9%B13%E6%B5%B7%E9%99%B8.m4a', duration=22000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/j0me9yt64y0lmei/%E9%9B%BB%E8%A9%B13%E5%9B%9B%E7%B8%A3.m4a', duration=22000))
    elif event.message.text == "身心科看診":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好我是精神科醫生，您怎麼了?\n醫生：你好，??係精神科醫生，你有仰般係無?\n病人：最近不知道就一直想哭，心情不好\n病人：最近無做麼?就緊想愛噭，心情毋好。\n醫生：這些情況持續多久?\n醫生：這兜情形續町有幾久咧？\n病人：大概有三個多月。\n病人：大約有三個零月。\n醫生：最近家裡或生活周遭發生什麼狀況嗎?\n醫生：最近屋下抑係生活?環境有發生麼?事情係無?\n病人：對爸爸的生活方式，比較不能接受(哭哭..)。\n病人：對??爸?生活方式，較不能接受(哭哭..)。\n醫生：看來這對於你影響很大。\n醫生：看來這對於你?影響盡大。\n病人：是的，想到就會哭，我可以聽到自己內心聲音，會想自殘自己。\n病人：係啊！想著就會噭，??做得聽著自家內心?聲音，會想愛傷害自家。\n醫生：最近晚上睡得好嗎?\n醫生：最近暗晡頭睡著好無?\n病人：晚上都沒什麼在睡，白天上課無法集中精神，就一直想哭。\n病人：暗晡頭都無麼?睡，日時頭上課無法度集中精神，就緊想愛噭。\n醫生：看來很困擾你。\n醫生：看來分你帶來盡多煩勞。\n病人：是的！\n病人：係啊！\n醫生：先吃藥看看情況可以改善，夜眠會比較好。\n醫生：先食藥仔看看，情況應該做得改善，暗晡頭會較好睡。\n病人：我知道了！\n病人：??知咧！\n醫生：預約一週後回診。\n醫生：預約一禮拜後轉來回診。\n病人：好的。\n病人：好，恁仔細/承蒙你。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/3gebcigetdesfl8/%E8%BA%AB%E5%BF%83%E7%A7%91%E7%9C%8B%E8%A8%BA%E6%B5%B7%E9%99%B8.m4a', duration=80000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/136oli64qenrm0a/%E8%BA%AB%E5%BF%83%E7%A7%91%E7%9C%8B%E8%A8%BA%E5%9B%9B%E7%B8%A3.m4a', duration=80000))
    elif event.message.text == "身心科回診":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好最近還好嗎?\n醫生：你好！恁久還好無?\n病人：沒什麼改善。\n病人：無麼?改善。\n醫生：例如哪裡？\n醫生：講看啊！係哪位仰般？\n病人：平常還是會聽到自己內心的聲音，我會想傷害家人及自己，我好害怕！\n病人：平常還係會聽著自家內心?聲音，??會想傷害屋下人摎自家，??當驚！\n醫生：上週拿的藥，請問有規則服藥嗎?\n醫生：上禮拜拿?藥仔，你有照規則服用無?\n病人：沒有，有時候會忘記吃\n病人：無，成時會毋記得食。\n醫生：情緒穩定的藥物一定要規則服藥，不能中斷。\n醫生：分心情穩定?藥仔一定愛照規則來服用，做毋得斷。\n病人：好的，我知道。\n病人：好，??知咧！\n醫生：幫你安排心理測驗。\n醫生：愛摎你安排心理測驗。\n病人：甚麼是心理測驗。\n病人：麼?係心理測驗。\n醫生：心理測驗是由心理師用圖片等做一些檢測。\n醫生：心理測驗係心理師用圖片等做?一兜檢測。\n病人：原來如此。\n病人：原來係恁樣。\n醫生：一樣要規則服藥，千萬別中斷\n醫生：共樣愛照規則服藥，千萬毋好停藥。\n病人：我會設定鬧鐘提醒，一免忘記，謝謝醫生。\n病人：??會設定鬧鐘仔來提醒，正毋會毋記得，承蒙醫生。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/z133utx61f6qdht/%E8%BA%AB%E5%BF%83%E7%A7%91%E5%9B%9E%E8%A8%BA%E6%B5%B7%E9%99%B8.m4a', duration=64000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/2haqizuajoyz3jy/%E8%BA%AB%E5%BF%83%E7%A7%91%E5%9B%9E%E8%A8%BA%E5%9B%9B%E7%B8%A3.m4a', duration=64000))
    elif event.message.text == "小兒科":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好寶寶怎麼了?\n醫生：你好！嬰兒仔有仰般係無?\n家屬：最近屁股紅紅的、有破皮，換尿布都會哭。\n家屬：最近屎朏紅紅、有爛皮，換尿布都會噭。\n醫生：讓我打開尿布看寶寶的臀部。\n醫生：分??打開尿布看嬰兒仔?屎朏。\n家屬：好的。\n家屬：好。\n醫生：這是尿布疹。\n醫生：這係尿布疹。\n家屬：甚麼是尿布疹。\n家屬：麼?係尿布疹。\n醫生：太長時間沒更換尿布，所導致的。\n醫生：時間忒長無換尿布，所因致?。\n家屬：我該怎麼辦?\n家屬：該??愛仰般？\n醫生：勤換尿布，保持乾爽，別使用爽身粉。\n醫生：愛較輒兜換尿布，保持燥爽，毋好用爽身粉。\n家屬：為甚麼不能用爽身粉，這樣不是可以更乾爽嗎?\n家屬：做麼?毋好用爽身粉，恁樣敢毋係做得較燥爽乜?\n醫生：尿液及糞便加上爽身粉會沾附皮膚，使皮膚不透氣。\n醫生：該尿摎大便加上爽身粉會黏在皮膚，皮膚就毋會透氣。\n家屬：我了解。\n家屬：??了解。\n醫生：開個藥膏給寶寶使用，少量擦。\n醫生：開隻藥膏分嬰兒仔使用，愛少量兜仔膏。\n家屬：好的，謝謝醫生。\n家屬：好，承蒙醫生。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/end557rr97vx0lt/%E5%B0%8F%E5%85%92%E7%A7%91%E6%B5%B7%E9%99%B8.m4a', duration=60000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/1zthhofqh4u5rux/%E5%B0%8F%E5%85%92%E7%A7%91%E5%9B%9B%E7%B8%A3.m4a', duration=60000))
def buttons_template(): 
    buttons = TemplateSendMessage(
            alt_text='功能選單',
            template=ButtonsTemplate(
                    title='請選擇服務功能',
                    text='此APP提供以下功能',
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
                        text='電話掛號3'
                    )
                ]
            )
    ) 
    return buttons
def buttons_template5(): 
    buttons = TemplateSendMessage(
            alt_text='診所選擇',
            template=ButtonsTemplate(
                    title='診所選擇',
                    text='診所選擇',
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
def buttons_template6(): 
    buttons = TemplateSendMessage(
            alt_text='身心科看診/回診',
            template=ButtonsTemplate(
                    title='身心科看診/回診',
                    text='看診/回診',
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
                actions=[
                     MessageTemplateAction(
                        label='看診',
                        text='身心科看診'
                    ), 
                     MessageTemplateAction(
                        label='回診',
                        text='身心科回診'
                    )
                ]
            )
    ) 
    return buttons
def buttons_template7(): 
    buttons = TemplateSendMessage(
            alt_text='醫院服務項目',
            template=ButtonsTemplate(
                    title='醫院',
                    text='項目選擇',
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
                actions=[
                     MessageTemplateAction(
                        label='內科',
                        text='內科'
                    ), 
                     MessageTemplateAction(
                        label='手術',
                        text='手術'
                    ),
                    MessageTemplateAction(
                        label='急診',
                        text='急診'
                    ),
                    MessageTemplateAction(
                        label='泌尿科',
                        text='泌尿科'
                    )

                ]
            )
    ) 
    return buttons
def buttons_template8(): 
    buttons = TemplateSendMessage(
            alt_text='內科看診/回診',
            template=ButtonsTemplate(
                    title='內科看診/回診',
                    text='看診/回診/看報告',
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
                actions=[
                     MessageTemplateAction(
                        label='內科看診',
                        text='內科看診'
                    ), 
                     MessageTemplateAction(
                        label='內科回診',
                        text='內科回診'
                    ),
                    MessageTemplateAction(
                        label='看報告',
                        text='看報告'
                    )

                ]
            )
    ) 
    return buttons
def buttons_template9(): 
    buttons = TemplateSendMessage(
            alt_text='手術狀態',
            template=ButtonsTemplate(
                    title='手術狀態',
                    text='手術前/手術準備/手術進行',
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
                actions=[
                     MessageTemplateAction(
                        label='手術前',
                        text='手術前'
                    ), 
                     MessageTemplateAction(
                        label='手術準備',
                        text='手術準備'
                    ),
                    MessageTemplateAction(
                        label='手術進行中',
                        text='手術進行中'
                    )

                ]
            )
    ) 
    return buttons

def  carousel_template():
    carousel = TemplateSendMessage(
        alt_text='急診情境',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                title='急診情境',
                text='車禍',
                actions=[
                    MessageTemplateAction(
                        label='車禍案例1',
                        text='車禍案例1'
                    ),
                    MessageTemplateAction(
                        label='車禍案例2',
                        text='車禍案例2'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                title='急診情境',
                text='燙傷',
                actions=[
                    MessageTemplateAction(
                        label='燙傷案例1',
                        text='燙傷案例1'
                    ),
                    MessageTemplateAction(
                        label='燙傷案例2',
                        text='燙傷案例2'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.imgur.com/CCohubT.jpg',
                title='急診情境',
                text='兒童',
                actions=[
                    MessageTemplateAction(
                        label='兒童案例1',
                        text='兒童案例1'
                    ),
                    MessageTemplateAction(
                        label='兒童案例2',
                        text='兒童案例2'
                    )
                ]
            )
        ]
    )
    )
    return carousel      
if __name__ == "__main__":
    app.run()