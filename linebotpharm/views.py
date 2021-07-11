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

from .message import message_controller
LINE_CHANNEL_ACCESS_TOKEN = 'Li0swYw0GWbk1o7XzBF1KJLJ2/BV9n9nttEbuDsQdQi7AggHSmYL5w3Tsc+IUJ6fLHMa2DMj95oRww0W+DKJiBk978G2btHgqUO8wjs8dtJZJCjQjDks7sAsjK9rujXVvkBPmk77rtHjSLKfbWAi5QdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '18657efd765b4ed4cbb7cc2cfe3612fe'

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

                #メッセージを生成してリストで返すインスタンス
                reply_list=[TextSendMessage(text=x) for x in message_controller.replay_controll(event.message.text)]
                #生成したメッセージを送信する処理
                line_bot_api.reply_message(
                    event.reply_token,
                    reply_list
                   )

        return HttpResponse('ok')
    else:
        return HttpResponseBadRequest()