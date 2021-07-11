from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn,TextSendMessage
)

from .message import message_controller,template_controller
LINE_CHANNEL_ACCESS_TOKEN = 'tgrGCa33Z8HKX5ug84Iq4/+3dHZYJggUYQsPmtxl6KwJKQAre40SGrsNZd1wfdLoo0vCjWAYqZ3aBxqqCYOwfb2HA+VsIAoU0Zr7PbmaGJHUHwLscV/yEDp/0Z8/KGdMHwgqwJRUa0gRL0H1VvX8/gdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '3ea3febc256e24df0bb3da11ef421678'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(LINE_CHANNEL_SECRET)

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
                reply_list=[]
                #メッセージを生成してリストで返すインスタンス
                details=template_controller.template_message(event.message.text)

                if details != False:
                    details=template_controller.template_message(event.message.text)
                    #メソッドから帰って来たクエリを使ってテンプレートメッセージを生成する。
                    reply_list=[]
                    for detail in details:
                        #構造式画像が存在するかの確認
                        if detail.structure:
                            thumbnail=detail.structure.url
                        else:
                            thumbnail="https://www.sozailab.jp/db_img/sozai/17976/e32e86c7d1a7e7e2ce0bf0d39d17d82f.jpg"

                        if detail.blandname:
                            blandname=detail.blandname
                        else:
                            blandname="販売中止"
                        template_list=[CarouselColumn(
                                        thumbnail_image_url=thumbnail,
                                        title="一般名:"+detail.name,
                                        text="商品名"+blandname,
                                        actions=[
                                            {
                                            "type":"message",
                                            "label":"詳細表示",
                                            "text":detail.name
                                            }
                                        ]
                                    )]
                        reply_list.extend(template_list)
                                    
                    
                        
                    reply_list=[TemplateSendMessage(
                            alt_text='template',
                            template=CarouselTemplate(columns=reply_list)
                        )]

                                 

            #生成したメッセージを送信する処理
                elif details==False:
                    #reply_list=[TextSendMessage(text=x) for x in message_controller.replay_controll(event.message.text)]
                    #reply_list.extend(reply_list)
                    
                    for replys in message_controller.replay_controll(event.message.text):
                        reply=TextSendMessage(replys)
                        reply_list.append(reply)

                line_bot_api.reply_message(
                        event.reply_token,
                        reply_list
                        )

        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest()