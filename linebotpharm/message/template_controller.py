from yakuri.models import Detail
from django.db.models import Q
def template_message(message):

    #薬品名の検索は弾く
    if Detail.objects.filter(field__fields__icontains=message) and Detail.objects.filter(field__fields__icontains=message).count() < 10:
        details=Detail.objects.filter(field__fields__icontains=message)
        return details
    
    elif Detail.objects.filter(target__targets__icontains=message) and  Detail.objects.filter(target__targets__icontains=message).count()<10:
        details= Detail.objects.filter(target__targets__icontains=message)
        return details

    elif Detail.objects.filter(detail__icontains=message) and Detail.objects.filter(detail__icontains=message).count()<10:
        details=Detail.objects.filter(detail__icontains=message)
        return details
    else:
        return False