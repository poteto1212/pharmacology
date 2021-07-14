from yakuri.models import Detail
from django.db.models import Q
from functools import reduce
from operator import and_

def template_message(message):

    #薬品名の検索(完全一致)は弾く(メッセージモジュールに任せる)
    if not Detail.objects.filter(Q(name=message)|Q(blandname=message)):
        #領域名部分一致
        if Detail.objects.filter(field__fields__icontains=message):
            details=Detail.objects.filter(field__fields__icontains=message)
            return details
        
        #作用点部分一致
        elif Detail.objects.filter(target__targets__icontains=message):
            details= Detail.objects.filter(target__targets__icontains=message)
            return details

        #ステム検索(一般名部分一致)
        elif Detail.objects.filter(name__icontains=message):
            details=Detail.objects.filter(name__icontains=message)
            return details

        #商品名の部分一致   
        elif Detail.objects.filter(blandname__icontains=message):
            details=Detail.objects.filter(blandname__icontains=message)
            return details
        #詳細説明の部分一致
        elif Detail.objects.filter(detail__icontains=message):
            details=Detail.objects.filter(detail__icontains=message)
            return details

        #問題文の部分一致
        elif Detail.objects.filter(question__icontains=message):
            details=Detail.objects.filter(question__icontains=message)
            return details
        else:
            return False
    else:
        return False