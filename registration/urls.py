from django.contrib import admin
from django.conf.urls import url, include
from accounts.views import FacebookLogin, CurrentUser

urlpatterns = [
    url('zingo/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/current', CurrentUser.as_view(), name='curent user'),

]
