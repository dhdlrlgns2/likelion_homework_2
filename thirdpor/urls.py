from django.contrib import admin
from django.urls import path, include
import blog.views
import port.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name = 'home'),
    path('blog/',include('blog.urls')),
    #수정 후 thirdpor(프로젝트이름)안의 url.py
    #include를 추가로 import 해준후, include를 추가함
    path('portfolio/',port.views.portfolio, name = "portfolio"),

    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/login/',accounts.views.login, name = 'login'),
    path('accounts/logout/', accounts.views.logout, name = 'logout'),
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#패스 컨버터