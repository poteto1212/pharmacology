from .models import Subject

#科目名をグローバル変数に代入する

joron="薬理学序論"
yakurione="薬理学Ⅰ"
yakuritwo="薬理学Ⅱ"
yakurithree="薬理学Ⅲ"
biseibutu="微生物学Ⅱ"
bunsiseibutu="薬治Ⅳ(抗がん剤)"
#全てのテンプレートに渡すデータを作成
def related(request):
    context={
        'joron':Subject.objects.filter(subjects=joron).first(),
        'yakurione':Subject.objects.filter(subjects=yakurione).first(),
        'yakuritwo':Subject.objects.filter(subjects=yakuritwo).first(),
        'yakurithree':Subject.objects.filter(subjects=yakurithree).first(),
        'biseibutu':Subject.objects.filter(subjects=biseibutu).first(),
        'bunsiseibutu':Subject.objects.filter(subjects=bunsiseibutu).first()
    }
    
    return context