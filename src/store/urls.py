from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', 'home.views.home', name = 'home'),
	url(r'^createaccount', 'user.views.createaccount', name = 'createaccount'),
	url(r'^signin', 'user.views.signin', name = 'signin'),
	url(r'^logout', 'user.views.logout_view', name = 'logout'),
	url(r'^product', 'product.views.product', name = 'product'),
	url(r'^order/([0-9]{1,2})', 'order.views.order', name = 'order'),
	url(r'^cart', 'order.views.cart', name = 'cart'),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)