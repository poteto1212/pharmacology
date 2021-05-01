from django.contrib import admin
from .models import Subject,Grade,Season,Work,Fields,Detail




class FieldsAdmin(admin.ModelAdmin):
    list_display=('subject','fields')

#医薬品登録(管理画面カスタマイズ)    
class DetailAdmin(admin.ModelAdmin):
    list_display=(
        'field',
        'name',
        'target',
        'work',
        'detail',
        )
    
    fields=[
        'field',
        'name',
        'target',
        'work',
        'detail',
        'structure',
        'grade',
        'season',
        ]
    
    #外部キーフィルター
    list_filter=(
        'grade__grades',#学年
        'season__seasons',#学期
        'work__works',#刺激と遮断
        'field__subject__subjects',#科目名
        'field__fields',#作用部位
        )
    
    #薬品名検索
    #説明文から検索
    search_fields=['field__fields','name','detail']
    #作用分類・学年・学期はラジオボタンにする
    radio_fields={'work':admin.HORIZONTAL,'grade':admin.HORIZONTAL,'season':admin.HORIZONTAL,}

    save_as=True


#管理権限付与
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Season)
admin.site.register(Work)
admin.site.register(Fields,FieldsAdmin)
admin.site.register(Detail,DetailAdmin)
# Register your models here.
