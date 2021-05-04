from django.views.generic import TemplateView,ListView
from .models import Detail,Subject
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
        context['medicines']=Detail.objects.filter(field__subject__id=titlekey).order_by('target','-work','-detail')
        
        #分野名のみを取得
        context['fields']=Detail.objects.filter(field__subject__id=titlekey).order_by('field').distinct().values('field__fields')
        
        return context
        
  
    