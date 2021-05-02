from django.views.generic import TemplateView,ListView
from .models import Detail
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'
    
class PharmList(ListView):
    template_name="list.html"
    model=Detail
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        
        titlekey=self.kwargs['id']
        context['title']=Detail.objects.filter(field__subject__id=titlekey).first()
        
        return context
        
    