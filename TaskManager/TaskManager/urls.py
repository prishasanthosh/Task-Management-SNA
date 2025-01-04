from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views
from tasks import auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', auth_views.register, name='register'),
]