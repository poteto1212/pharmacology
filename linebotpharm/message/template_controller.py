from yakuri.models import Detail
from django.db.models import Q
def template_message(message):

    #薬品名の検索は弾く
    if not Detail.objects.filter(Q(name=message)|Q(blandname=message)):
        if Detail.objects.filter(field__fields__icontains=message):
            details=Detail.objects.filter(field__fields__icontains=message)
            return details
        
        elif Detail.objects.filter(target__targets__icontains=message):
            details= Detail.objects.filter(target__targets__icontains=message)
            return details
    
        elif Detail.objects.filter(detail__icontains=message):
            details=Detail.objects.filter(detail__icontains=message)
            return details
        else:
            return False
    else:
        return False