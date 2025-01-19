from django.contrib import admin
from django.shortcuts import render
from django.urls import path , include

from home.models import FooterInfo
from . import settings
from django.conf.urls.static import static



def custom_404_view(request, exception):
    footer = FooterInfo.objects.all()
    return render(request, '404.html', status=404, context={'footer': footer})


handler404 = custom_404_view






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    path('account/', include('account.urls')),
    path('product/', include('product.urls')),
    path('blog/', include('blog.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
