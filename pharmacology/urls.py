from django.contrib import admin
from django.urls import path,include
#画像処理に必要なメソッド
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('yakuri.urls')),
    path('linebot/',include('linebot.urls')),
]

#画像urlを定義
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)