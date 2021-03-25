from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage
from linebot.models import AudioSendMessage, VideoSendMessage

from module import func

from django.shortcuts import render
from datetime import datetime

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
#                    if mtext != '@傳送文字':
#                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=mtext))	
                    if mtext == '@傳送文字':
                        func.sendText(event)	
                    if mtext == '@傳送聲音':
                        func.sendVoice(event)	
                    if mtext == '@傳送影片':
                        func.sendVedio(event)
                    if mtext == '@使用說明':
                        func.sendUse(event)
                    if mtext == '@北歐貿易':
                        func.neuWeb(event)

                    else:
                        func.sendTWder(event, mtext)
											
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
		
# define sayhello
def sayhello(request):
   return HttpResponse("Hello Django!")

# define hello3
def hello3(request,username):
   now=datetime.now()
   return render(request,"hello3.html",locals())
   
# define hello4
def hello4(request,username):
   now=datetime.now()
   return render(request,"hello4.html",locals()) 
   
# define hello4
def hello5(request):
   now=datetime.now()
   return render(request,"hello5.html",locals()) 