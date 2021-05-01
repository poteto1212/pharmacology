from .models import Subject

#科目名をグローバル変数に代入する

joron="薬理学序論"
yakurione="薬理学Ⅰ"
yakuritwo="薬理学Ⅱ"
yakurithree="薬理学Ⅲ"
biseibutu="微生物学Ⅱ"
#全てのテンプレートに渡すデータを作成
def related(request):
    context={
        'joron':Subject.objects.get(subjects=joron),
        'yakurione':Subject.objects.get(subjects=yakurione),
        'yakuritwo':Subject.objects.get(subjects=yakuritwo),
        'yakurithree':Subject.objects.get(subjects=yakurithree),
        'biseibutu':Subject.objects.get(subjects=biseibutu)
    }
    
    return context