from django.shortcuts import render

#linebot用モジュール
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .utils import message_creater
from linebot.line_message import LineMessage

@csrf_exempt
def index(request):
    #postで受け取ったとき・・・
    if request.method == 'POST':
        #pythonで読み込めるように変換　辞書型のデータリストが返される
        request = json.loads(request.body.decode('utf-8'))
        #メッセージ情報はeventsキーに格納されている
        #格納されているデータは複数のメッセージ辞書を含むリスト型
        events=request['events']
        
        for event in events:
            message=event['message']#メッセージのうち一つえ
            reply_token=event['replyToken']#メッセージの暗号を返信の暗号に渡す
            line_message = LineMessage(message_creater.create_single_text_message(message['text']))
            #メッセージ辞書のtextキーを暗号と一緒に返す
            line_message.reply(reply_token)
            
        return HttpResponse('ok')