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
    elif event.message.text == "內科看診":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好請問那裏不舒服？\n醫生：你好！請問那位毋鬆爽？\n病人：醫生我最近食慾很好，一直吃而且尿很多、體重又減輕很奇怪。\n病人：醫生??最近盡會食，緊食又合尿盡多、體重又減輕當奇怪。\n醫生：請問家族有糖尿病史嗎？\n醫生：請問你?家族有人著過糖尿病無？\n病人：我爸爸有糖尿病。\n病人：??爸有糖尿病。\n醫生：那您比一般人得糖尿病的機會更高，先抽血驗糖化血色素，可以知道近三個月的血糖值。\n醫生：該你比一般人著糖尿病?機會較高，愛先抽血驗糖化血色素，就做得知你近三個月?血糖值。\n病人：我了解了，請問多久後回診看報告。\n病人：??了解咧，請問愛幾時來回診看報告。\n醫生：預約一週後看回診報告。\n醫生：預約一禮拜後來看回診報告。\n病人：好的。\n病人：好。恁仔細/承蒙你。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/u4b3q4br76zmpgt/%E5%85%A7%E7%A7%91%E7%9C%8B%E8%A8%BA.m4a', duration=50000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/9w8tynbqezog5bb/%E5%85%A7%E7%A7%91%E7%9C%8B%E8%A8%BA%E5%9B%9B%E7%B8%A3.m4a', duration=50000))
    elif event.message.text == "內科回診":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好最近一個月飲食還是吃很多尿很多嗎？體重有減輕嗎？\n醫生：你好！最近一隻月食東西，還係食當多合尿當多係無？體重有減輕無？\n病人：最近吃了糖尿病的藥，那些三多徵狀都沒了。\n病人：最近食糖尿病?藥仔，該兜三多?症頭全無咧。\n醫生：那先一樣規則服藥及飲食控制。\n醫生：該還係共樣愛照規則服藥摎飲食控制。\n病人：我理解了。\n病人：??了解咧，承蒙醫生。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/7ywab4hbrr500l4/%E5%85%A7%E7%A7%91%E5%9B%9E%E8%A8%BA%E6%B5%B7%E9%99%B8.m4a', duration=29000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/obxfnmqp430brcs/%E5%85%A7%E7%A7%91%E5%9B%9E%E8%A8%BA%E5%9B%9B%E7%B8%A3.m4a', duration=29000))
    elif event.message.text == "看報告":
        line_bot_api.push_message(uid, TextSendMessage('醫生：上次初診時，您所形容的確實是很典型糖尿病徵象。\n醫生：上回初診?時節，你所講?確實係盡典型糖尿病?病症。\n病人：是喔！\n病人：係哦！\n醫生：這次驗的糖化血色素報告是異常，代表這三個月的血糖值很高。\n醫生：這擺驗?糖化血色素報告係無正常，表示這三隻月?血糖值盡高。\n病人：那我該怎麼辦，需要打胰島素嗎？\n病人：該??愛仰般？愛使打胰島素無？\n醫生：目前先吃藥控制，及飲食控制，除非控制不好才會用到打胰島素來控制。\n醫生：目前先食藥仔控制，摎飲食控制，除非控制毋好正愛用著打胰島素來控制。\n病人：我了解了。\n病人：??了解咧。\n醫生：預約一個月後回診。\n醫生：預約一個月後轉來回診。\n病人：好。\n病人：好，承蒙。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/ropd12nhajquqnz/%E5%85%A7%E7%A7%91%E7%9C%8B%E5%A0%B1%E5%91%8A%E6%B5%B7%E9%99%B8.m4a', duration=42000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/4t2he412cyv1zqo/%E5%85%A7%E7%A7%91%E7%9C%8B%E5%A0%B1%E5%91%8A%E5%9B%9B%E7%B8%A3.m4a', duration=42000))
    elif event.message.text == "手術前":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好！明天早上９點進行XX手術。\n醫生：你好！天光日/韶\n朝晨９點進行XX手術。\n病人：好。\n病人：好。\n醫生：請問對藥物過敏？以前有手術過嗎？\n醫生：請問你有對麼?藥物過敏無？以前有手術過無？\n病人：都沒有。\n病人：全無。\n醫生：手術之前會先進行麻醉。\n醫生：手術以前愛先進行麻醉。\n病人：請問是局部還是全身的？\n病人：請問係局部抑係全身?？\n醫生：採取局部麻醉。\n醫生：採用局部麻醉。\n病人：我了解。\n病人：??知咧。\n醫生：麻煩請填寫手術同意書。\n醫生：麻煩你填寫手術同意書。\n病人：手術有風險嗎？\n病人：手術有風險無？\n醫生：任何手術皆有風險。\n醫生：任何手術都有風險。\n病人：我了解。\n病人：??了解。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/08u7fi0s8httac2/%E6%89%8B%E8%A1%93%E5%89%8D%E6%B5%B7%E9%99%B8.m4a', duration=39000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/5pr1efeogd1fnws/%E6%89%8B%E8%A1%93%E5%89%8D%E5%9B%9B%E7%B8%A3.m4a', duration=39000))
    elif event.message.text == "手術準備":
        line_bot_api.push_message(uid, TextSendMessage('醫生：等會進行背部局部麻醉，請放輕鬆。\n醫生：等加下愛進行背囊?局部麻醉，請放輕鬆毋使緊張。\n病人：醫生我會的。\n病人：醫生??知咧。\n醫生＜麻醉科＞：確認生命徵象，生命徵象穩定、準備施打麻醉針。\n醫生＜麻醉科＞：確認生命徵象，生命徵象穩定、準備愛打麻醉針。\n病人：好，我會放鬆。\n病人：好，??會放輕鬆兜。\n醫生：確認手術周圍無反應。\n醫生：確認手術旁脣無反應。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/qx5c05r8xb6rab2/%E6%89%8B%E8%A1%93%E6%BA%96%E5%82%99%E6%B5%B7%E9%99%B8.m4a', duration=26000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/qx5c05r8xb6rab2/%E6%89%8B%E8%A1%93%E6%BA%96%E5%82%99%E6%B5%B7%E9%99%B8.m4a', duration=26000))
    elif event.message.text == "手術進行中":
        line_bot_api.push_message(uid, TextSendMessage('醫生：再次確認生命徵象，手術順利完成，麻醉退後傷口會疼痛，開止痛消炎藥及保持傷口乾燥。\n醫生：再次確認生命徵象，手術順利完成，麻藥過忒後傷口會痛，??開兜止痛消炎藥還過愛保持傷口?燥爽。\n病人：我會注意的。\n病人：??會注意兜。\n醫生：預約下次回診拆線。\n醫生：預約下次回診?時節來拆線。\n病人：謝謝醫生。\n病人：承蒙醫生。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/2j16o280ef5pnov/%E6%89%8B%E8%A1%93%E9%80%B2%E8%A1%8C%E6%B5%B7%E9%99%B8.m4a', duration=27000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/kbcjib3ya5906rx/%E6%89%8B%E8%A1%93%E9%80%B2%E8%A1%8C%E5%9B%9B%E7%B8%A3.m4a', duration=27000))
    elif event.message.text == "車禍案例1":
        line_bot_api.push_message(uid, TextSendMessage('護理師：妳怎麼了，需要幫忙嗎?\n護理師：你仰般形，愛使手無?\n病人：剛在路上走路被車子撞到了，我的腳很痛，無法走路、一直在流血。\n病人：頭先行路?時節分車仔撞著，???腳盡痛，無法度行、緊流血。\n護理師：您先別動，先來止血、用固定板固定痛得位置，立刻請醫生過來評估。\n護理師：你莫停動，先來止血，用固定板固定痛?位所，黏時請醫生來看。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/slkgg8q5bb6jhne/%E8%BB%8A%E7%A6%8D1%E6%B5%B7%E9%99%B8.m4a', duration=25000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/gpjshhbv0emfe8o/%E8%BB%8A%E7%A6%8D1%E5%9B%9B%E7%B8%A3.m4a', duration=25000))
    elif event.message.text == "車禍案例2":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好我是急診醫生，我幫您看一下腳痛及出血的位置。\n醫生：你好，??係急診醫生，??來摎你看一下，你哪位痛？哪位出血？\n病人：痛的位置在左腳，麻煩醫生。\n病人：痛?位所在左腳，麻煩醫生。\n醫生：我初步評估可能有骨折，需要做進一步檢查，先安排照片子，確定診斷。\n醫生：目前看來可能係骨頭斷忒，愛做進一步?檢查，先安排照片仔來確定診斷。\n病人：好的。\n病人：好。\n醫生：照片子的結果確定是骨折，立刻安排手術。\n醫生：照片仔?結果確定係骨頭斷忒，馬上愛安排手術。\n病人：請問需要住院嗎?\n病人：請問愛使戴院無？\n醫生：目前看片子結果必需手術，之後住院治療。\n醫生：手術了後愛住院治療。\n病人：我理解。\n病人：??了解，恁仔細／承蒙你。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/rgkr0wsoq7eueld/%E8%BB%8A%E7%A6%8D2%E6%B5%B7%E9%99%B8.m4a', duration=46000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/5dv1yzkv4tj0rww/%E8%BB%8A%E7%A6%8D2%E5%9B%9B%E7%B8%A3.m4a', duration=46000))
    elif event.message.text == "燙傷案例1":
        line_bot_api.push_message(uid, TextSendMessage('護理師：妳怎麼了，需要幫忙嗎?\n護理師：你仰般形，愛使手無?\n病人：剛在煮晚餐手掌被熱湯燙傷了。\n病人：頭先煮夜?時節手巴掌分燒湯熝著。\n護理師：我們先用生理食鹽水沖洗傷口，請忍耐、等醫生過來評估。\n護理師：俚先用生理食鹽水來沖洗傷口，請你忍耐一下、等醫生過來看。\n病人：我的手掌刺痛而且好熱，好痛喔！\n病人：???手巴掌當燒合??滾痛，還痛哦！'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/kesvvhlrlngyrus/%E7%87%99%E5%82%B71%E6%B5%B7%E9%99%B8.m4a', duration=27000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/0u6op5u86809xp0/%E7%87%99%E5%82%B71%E5%9B%9B%E7%B8%A3.m4a', duration=27000))
    elif event.message.text == "燙傷案例2":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好我是急診醫生，看您的傷口紅腫情形，為一級燙傷，必須持續冰敷。\n醫生：你好，??係急診醫生，看你?傷口恁紅恁腫，係一級熝傷，定著愛續町冰敷。\n病人：請問冰敷要多久？\n病人：請問冰敷愛幾久？\n醫生：每次冰敷約30分種，等會開3天份消炎止痛藥，若有發燒立刻回來就醫。\n醫生：每擺冰敷大約30分鐘，等下會開3日份?消炎止痛藥，若係有發燒馬上愛轉來看。\n病人：我知道了，謝謝醫生。\n病人：??知了，承蒙醫生。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/r1d6aqdliv70uzp/%E7%87%99%E5%82%B72%E6%B5%B7%E9%99%B8.m4a', duration=31000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/ppkw8kf6iylkae8/%E7%87%99%E5%82%B72%E5%9B%9B%E7%B8%A3.m4a', duration=31000))
    elif event.message.text == "兒童案例1":
        line_bot_api.push_message(uid, TextSendMessage('護理師：妳怎麼了，需要幫忙嗎?\n護理師：你仰般形，愛使手無?\n家屬：我的小孩一直拉肚子，有時候會吐、還有發燒，不知道甚麼原因？\n家屬：???細人仔緊屙痢肚，成時會嘔、還合會發燒，毋知做麼?會恁樣？\n護理師：我幫孩子先量生命徵象，體溫38.9度，我請醫生過來。\n護理師：??先摎佢量看有發燒無？體溫38.9度，??請醫生過來。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/4vwjjl32qoj4cbx/%E5%85%92%E7%AB%A51%E6%B5%B7%E9%99%B8.m4a', duration=25000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/tuqvuwwcyn4s7g4/%E5%85%92%E7%AB%A51%E5%9B%9B%E7%B8%A3.m4a', duration=25000))
    elif event.message.text == "兒童案例2":
        line_bot_api.push_message(uid, TextSendMessage('醫生：您好我是急診醫生，剛護理師量體溫38.9度，看孩子精神倦怠、有拉肚子情形，會吐，先抽血及大便檢查，在確定診斷。\n醫生：你好，??係急診醫生，頭先護理師量體溫係38.9度，??看細人仔當作，歸身軟怠怠無精神、還過會屙痢肚、會嘔，愛先抽血摎做大便檢查，正來確定診斷。\n家屬：醫生請問報告要會等多久？\n家屬：醫生請問報告愛等幾久？\n醫生：報告很快就出來了。\n醫生：報告當遽就會出來。\n家屬：好的。\n家屬：好。\n醫生：報告出來了，確定是輪狀病毒。\n醫生：報告出來咧，確定係輪狀病毒。\n家屬：我該怎麼辦，需要注意甚麼。\n家屬：該??愛仰般？愛注意兜麼?。\n醫生：勤洗手，補充水分、注意精神狀態。\n醫生：愛較勤兜洗手，補充水分、注意看佢?精神好無？\n家屬：那除了注意這些，需要住院嗎？\n家屬：除了愛注意這兜，該還需要住院無？\n醫生：目前輪狀病毒我們先給止瀉藥及退燒就好了。\n醫生：目前輪狀病毒??兜先分佢止瀉藥摎退燒就好咧。\n家屬：我了解了。\n家屬：??了解咧，承蒙。'))
        line_bot_api.push_message(uid, AudioSendMessage('https://dl.dropbox.com/s/3d55koqubvibsaa/%E5%85%92%E7%AB%A52%E6%B5%B7%E9%99%B8.m4a', duration=64000))
        line_bot_api.reply_message(event.reply_token, AudioSendMessage(original_content_url='https://dl.dropbox.com/s/q4wg331v0ancpyo/%E5%85%92%E7%AB%A52%E5%9B%9B%E7%B8%A3.m4a', duration=64000))




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
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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
                thumbnail_image_url='https://i.imgur.com/Hz1DDhu.png',
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