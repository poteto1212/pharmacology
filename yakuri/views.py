from django.views.generic import TemplateView,ListView
from .models import Detail,Subject,Fields
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
        context['medicines']=Detail.objects.filter(field__subject__id=titlekey).distinct().order_by('-work','-detail')
        
        #分野名のみを取得
        context['fields']=Fields.objects.filter(subject__id=titlekey).order_by('fields').distinct().values('fields')
        
        return context
        

#科目別の一覧目次画面を作成するクラス
class PharmIndex(ListView):
    template_name='index.html'
    model=Fields
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        key=self.kwargs['id']
        context['target_list']=Fields.objects.filter(subject__id=key).order_by('id')
        return context
    
    
#科目別一覧目次画面を作成するクラス