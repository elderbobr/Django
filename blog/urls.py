from django.urls import path, include
from django.contrib import admin

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), namespace='blog'),
]
