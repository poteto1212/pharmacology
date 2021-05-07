from django.contrib import admin
from .models import Subject,Grade,Season,Work,Fields,Detail,Target


#作用点管理画面(抹消・中枢・循環etc)
class TargetAdmin(admin.ModelAdmin):
    list_display=('targets','targetsnum')
    list_editable('targetsnum',)

#作用の仕方の管理画面(刺激・遮断・酵素阻害etc)
class WorkAdmin(admin.ModelAdmin):
    list_display=('works','worknum')
    list_editable('worknum',)

#作用領域管理画面
class FieldsAdmin(admin.ModelAdmin):
    list_display=('subject','fields','_reltarget','fieldsnum')
    list_editable=('fieldsnum',)
    ordering=('fieldsnum',)
    list_filter=('subject__subjects',)
    season_field=('fields')#分野名から検索
    filter_horizontal=('reltarget',)
    
    def _reltarget(self,row):
        return '\n'.join([X.targets for X in row.reltarget.all()])


#医薬品登録(管理画面カスタマイズ)    
class DetailAdmin(admin.ModelAdmin):
    list_display=(
        'field',
        'name',
        '_target',
        'work',
        'detail',
        'studynum',
        )
     #一覧画面での編集

    list_editable=(
        'work',
        'studynum',
        )
        
    #デフォルト並び順
    ordering=('studynum',)
    
    fields=[
        'field',
        'name',
        'target',
        'work',
        'detail',
        'structure',
        'grade',
        'season',
        'studynum',
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
    
    #ManyttoManyの設定
    filter_horizontal=('target',)
    
    def _target(self,row):
        return '\n'.join([X.targets for X in row.target.all()])
    


#管理権限付与
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Season)
admin.site.register(Work,WorkAdmin)
admin.site.register(Target,TargetAdmin)
admin.site.register(Fields,FieldsAdmin)
admin.site.register(Detail,DetailAdmin)
# Register your models here.
