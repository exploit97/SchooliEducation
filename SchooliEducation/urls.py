
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler403, handler500



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls', namespace='blogs')),
    path('accounts/',include('allauth.urls')),
    path('',include('users.urls', namespace='users')),
    path('courses/',include('courses.urls', namespace='courses')),
    path('examen_et_concours/',include('examen_et_concours.urls', namespace='examen_et_concours')),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
