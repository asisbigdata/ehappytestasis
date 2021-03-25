from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot.models import AudioSendMessage, VideoSendMessage

import requests
import twder  #匯率套件

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
baseurl = 'https://3073304a6426.ngrok.io/static/'

currencies = {'美金':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD',\
              '日圓':'JPY','歐元':'EUR','人民幣':'CNY' }  #幣別字典
keys = currencies.keys()

def sendText(event):  #傳送文字
    try:
        message = TextSendMessage(  
            text = "我是 Linebot，\n您好！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
		
def sendVoice(event):  #傳送聲音
    try:
        message = AudioSendMessage(
            original_content_url=baseurl + 'mario.m4a',  #聲音檔置於static資料夾
            duration=20000  #聲音長度20秒
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendVedio(event):  #傳送影像
    try:
        message = VideoSendMessage(
            original_content_url=baseurl + 'robot.mp4',  #影片檔置於static資料夾
            preview_image_url=baseurl + 'robot.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendUse(event):  #使用說明
    try:
        text1 ='''
查詢匯率：輸入外幣名稱「XXXX」，例如「美金」,「英鎊」,「港幣」,「澳幣」,「日圓」,「歐元」,「人民幣」
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#函數 sendLUIS 是課本Ch09 範例 >>> 可以修正為自己的函數 sendTWder

def sendTWder(event, mtext):  
    try:
#        money = '美元'
        money = mtext
        if not money == '':  #匯率類幣別存在
            if money in keys:
                rate3 = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                message = money + '_即期買入匯率 : ' + str(rate3)+ '_(台灣銀行端) '
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此幣別匯率資料！'))
        else:  #其他未知輸入
            text = '無法了解你的意思，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
            
    except:
       line_bot_api.reply_message(event.reply_token, TextSendMessage(text='執行時產生錯誤！'))

def neuWeb(event):  #@北歐貿易連結
    try:
        text1 ='''
北歐福利網頁：https://kknews.cc/zh-tw/world/3q2r8ng.html
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
