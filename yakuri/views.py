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
        
        #分野名のみを取得
        context['fields']=Fields.objects.filter(subject__id=titlekey).order_by('fieldsnum').distinct().values('fields')
        
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
    