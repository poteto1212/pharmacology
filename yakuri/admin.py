from django.contrib import admin
from .models import Subject,Grade,Season,Work,Fields,Detail,Target
from admin_auto_filters.filters import AutocompleteFilter


#科目管理画面
class SubjectAdmin(admin.ModelAdmin):
    list_display=('subjects','subjectsnum')
    list_editable=('subjectsnum',)
    ordering=('subjectsnum',)
    save_as=True
#作用点管理画面(抹消・中枢・循環etc)
class TargetAdmin(admin.ModelAdmin):
    list_display=('targets','targetsnum')
    list_editable=('targetsnum',)
    ordering=('targetsnum',)
    save_as=True
#作用の仕方の管理画面(刺激・遮断・酵素阻害etc)
class WorkAdmin(admin.ModelAdmin):
    list_display=('works','worknum')
    list_editable=('worknum',)
    ordering=('worknum',)
    save_as=True

#薬効分類の検索
class FieldsFilter(AutocompleteFilter):
    title="Field"
    field_name='field'
    
class FieldsFilterAdmin(admin.ModelAdmin):
    search_fields=['fields']

    
#作用領域管理画面
class FieldsAdmin(admin.ModelAdmin):
    search_fields=['subject__subjects','fields']
    list_display=('subject','fields','_reltarget','fieldsnum')
    list_editable=('fields','fieldsnum',)
    ordering=('fieldsnum',)
    list_filter=('subject__subjects',)
    season_field=('fields')#分野名から検索
    filter_horizontal=('reltarget',)
    save_as=True
    def _reltarget(self,row):
        return '\n'.join([X.targets for X in row.reltarget.all()])


#医薬品登録(管理画面カスタマイズ)    
class DetailAdmin(admin.ModelAdmin):
    list_display=(
        'field',
        'name',
        'blandname',
        '_target',
        'work',
        'structure',
        'studynum',
        )
     #一覧画面での編集

    list_editable=(
        'name',
        'blandname',
        'work',
        'structure',
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
        'question',
        'blandname',
        ]
    
    #外部キーフィルター
    list_filter=(
        FieldsFilter,#作用部位検索
        'grade__grades',#学年
        'season__seasons',#学期
        'work__works',#刺激と遮断
        'field__subject__subjects',#科目名
        'field__fields',
        )
    raw_id_fields=('field',)
        
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
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Grade)
admin.site.register(Season)
admin.site.register(Work,WorkAdmin)
admin.site.register(Target,TargetAdmin)
admin.site.register(Fields,FieldsAdmin)
admin.site.register(Detail,DetailAdmin)
# Register your models here.
