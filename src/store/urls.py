from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', 'home.views.home', name = 'home'),
	
		#these 3 are for editing the database info as staff
	url(r'^usermanage', 'home.views.users', name = 'manageusers'),
	url(r'^productmanage', 'home.views.products', name = 'manageproducts'),
	url(r'^ordermanage', 'home.views.orders', name = 'manageorders'),


	url(r'^createaccount', 'user.views.createaccount', name = 'createaccount'),
	url(r'^editaccount', 'user.views.editaccount', name = 'editaccount'),
	url(r'^signin', 'user.views.signin', name = 'signin'),
	url(r'^logout', 'user.views.logout_view', name = 'logout'),
	url(r'^product', 'product.views.product', name = 'product'),
	url(r'^alert', 'supply.views.alert', name = 'alert'),
	url(r'^manage', 'home.views.manage', name = 'manage'),
	url(r'^supply', 'supply.views.supply', name = 'supply'),					
	url(r'^order/([0-9]{1,2})', 'order.views.order', name = 'order'),
	url(r'^cart', 'order.views.cart', name = 'cart'),
	url(r'^createproduct', 'product.views.createproduct', name = 'createproduct'),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)