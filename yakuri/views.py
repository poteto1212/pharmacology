from django.views.generic import TemplateView,ListView
from .models import Detail,Subject,Fields,Target,Work
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'
    
class PharmList(ListView):
    template_name="list.html"
    model=Detail
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        #Subjectモデルのidをベースに絞り込み
        titlekey=self.kwargs['id']
        context['title']=Subject.objects.filter(id=titlekey).first()
        context['medicines']=Detail.objects.filter(field__subject__id=titlekey).distinct().order_by('studynum','-work','-detail')
        
        #科目に準じた分野名と分野idを取得
        context['fields']=Fields.objects.filter(subject__id=titlekey).order_by('fieldsnum').distinct().values('fields','id')
        
        
        #絞り込みプルダウン用
        context['fields_list']=Fields.objects.filter(subject__id=titlekey).order_by('fieldsnum').distinct().values('fields','id')
        
        return context

#医薬品一覧の分野別絞り込み
class FilterPharmList(ListView):
    template_name="list.html"
    model=Detail
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        titlekey=self.request.GET.get('fieldset')
        
        fieldkey=Fields.objects.filter(id=titlekey).first()
        
        context['title']=Subject.objects.filter(id=fieldkey.subject.id).first()
        context['fields_list']=Fields.objects.filter(subject__id=fieldkey.subject.id).order_by('fieldsnum').distinct().values('fields','id')
        
        
        #医薬品一覧及び科目名はpost値と分野IDによってフィルタ
        context['medicines']=Detail.objects.filter(field__id=titlekey).distinct().order_by('studynum','-work','-detail')
        
        #分野名はpost値をそのままisに
        context['fields']=Fields.objects.filter(id=titlekey).order_by('fieldsnum').distinct().values('fields','id')
        return context
#科目別の一覧目次画面を作成するクラス
class PharmIndex(ListView):
    template_name='index.html'
    model=Fields
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        key=self.kwargs['id']
        context['title']=Subject.objects.filter(id=key).first()
        context['field_list']=Fields.objects.filter(subject__id=key).order_by('id')
        
        return context




#作用機序別に薬物を絞り込むクラス
class TargetList(ListView):
    template_name="target.html"
    model=Detail
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        targetkey=self.kwargs['id']
        #作用点をベースに絞り込み
       
        #タイトル・見出し・生理機能説明用       
        context['targets']=Target.objects.get(id=targetkey)
        
        #作用の仕方(刺激・遮断etcを取得)
        context['work_list']=Detail.objects.filter(target__id=targetkey).order_by('work__worknum').distinct().values('work__works')
        
        #情報取得クエリ
        context['medicines_list']=Detail.objects.filter(target__id=targetkey)
        return context
        
#問題一覧を作用機序別に表示する(薬理学序論から順番に)       
class PracticeList(ListView):
    template_name="practice.html"
    model=Detail
    
    #科目・分野での絞り込み用ボタンの設置
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #科目リスト取得
        context['subjects_list']=Subject.objects.all().order_by('subjectsnum')
        #ボタン用に分野名と分野IDを取得
        context['fields_list']=Fields.objects.all().order_by('subject__subjectsnum','fieldsnum',).distinct().values('fields','subject__id','id')
        #分野選択のデフォルト値
        context['defaultfield']=Fields.objects.all().first()
        #見出し用に分野名と分野IDを取得
        context['fieldsmedicines_list']=Fields.objects.all().order_by('subject__subjectsnum','fieldsnum',).distinct().values('fields','subject__id','id')
        #科目順に医薬品名を取得する
        context['medicines_list']=Detail.objects.all().order_by('field__subject__subjectsnum','studynum')
      
        
        #Get値がある時のり込み用の処理
        
        if self.request.GET.get('subjectkey'):
            key=self.request.GET.get('subjectkey')
            context['fields_list']=Fields.objects.filter(subject__id=key).order_by('subject__subjectsnum','fieldsnum',).distinct().values('fields','subject__id','id')
            context['fieldsmedicines_list']=Fields.objects.filter(subject__id=key).order_by('subject__subjectsnum','fieldsnum',).distinct().values('fields','subject__id','id')
            context['defaultfield']=Fields.objects.filter(subject__id=key).first()
        elif self.request.GET.get('fieldsset'):
            key=self.request.GET.get('fieldsset')
            fieldkey=Fields.objects.filter(id=key).first()
            context['fields_list']=Fields.objects.filter(subject__id=fieldkey.subject.id).order_by('subject__subjectsnum')
            context['fieldsmedicines_list']=Fields.objects.filter(id=key).order_by('subject__subjectsnum','fieldsnum',).distinct().values('fields','subject__id','id')
            context['defaultfield']=Fields.objects.filter(id=key).first()
        
        return context

#構造式一覧画面
class StructureList(ListView):
    template_name="structure.html"
    model=Detail
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data()
        #科目選択ラジオボタン用
        context['subjects_list']=Subject.objects.all().order_by('subjectsnum')
        
        #分野選択プルダウン用
        context['fields_list']=Fields.objects.all().order_by('subject__subjectsnum')
        
        #構造一覧表示
        context['structure_list']=Detail.objects.all().order_by('field__subject__subjectsnum','field__fieldsnum','studynum')
        #プルダウンデフォルト値
        context['defaultfield']=Fields.objects.all().first()
    
#構造式画面の絞り込み検索

        #各GET条件に応じた条件分岐
        #科目で絞り込まれた時
        if self.request.GET.get('subjectkey'):
            key=self.request.GET.get('subjectkey')
            context['fields_list']=Fields.objects.filter(subject__id=key).order_by('subject__subjectsnum')
            context['structure_list']=Detail.objects.filter(field__subject__id=key).order_by('field__subject__subjectsnum','field__fieldsnum','studynum')
            context['defaultfield']=Fields.objects.filter(subject__id=key).first()
        elif self.request.GET.get('fieldskey'):
            key=self.request.GET.get('fieldskey')
            fieldkey=Fields.objects.filter(id=key).first()
            
            context['fields_list']=Fields.objects.filter(subject__id=fieldkey.subject.id).order_by('subject__subjectsnum')
            context['structure_list']=Detail.objects.filter(field__id=key).order_by('field__subject__subjectsnum','field__fieldsnum','studynum')
            context['defaultfield']=Fields.objects.filter(id=key).first()
        
        return context
        
        
        