
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from inventory.views import InventoryTemplateView, ExampleTemplateView, MyView, InventoryDetail, InventoryListView, InventoryCreateView
admin.autodiscover()

urlpatterns = [
    # url(r'^paste/', include('pastebin.urls')),
    #url(r'^inventory/', include('inventory.urls')),
    #url(r'^polls/', include('polls.urls')),
    #url(r'^inventory/', 'inventory.views.index', name='inventory'),
    url(r'^inventorydetail/create/$', InventoryCreateView.as_view(), name='inventory_create'),
    url(r'^inventorydetail/$', InventoryListView.as_view(), name='inventory_list'),
    url(r'^inventorydetail/(?P<slug>[-\w]+)$', InventoryDetail.as_view(), name='inventory_detail'),
    url(r'^inventory/$', InventoryTemplateView.as_view(template_name='inventory.html'), name='inventory'),
    url(r'^example/$', ExampleTemplateView.as_view(template_name='inventory.html'), name='example'),
    url(r'^someview/$', MyView.as_view(template_name='inventory.html'), name='someview'),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)