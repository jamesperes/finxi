"""imoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from siteimoveis.views import (imovel_home, imovel_novo, vendedor_novo,
                               imovel_pesquisa, imovel_list, imovel,
                               imovel_proximos)
from django.conf.urls.static import static

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', imovel_home),
    url(r'^pesquisa/$', imovel_pesquisa, name='imovelpesquisa'),
    url(r'^cadastraimovel/$', imovel_novo, name='imovel_novo'),
    url(r'^cadastravendedor/$', vendedor_novo, name='vendedor_novo'),
    url(r'^lista/$', imovel_list, name='imovel_list'),
    url(r'^imovel/(?P<imovel_id>[0-9]+)$', imovel),
    url(r'^imovelproximo/$', imovel_proximos, name='imovelproximo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
