from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo_project.my_app.urls')),
    path('accounts/', include('demo_project.accounts.urls')),
    path('glasses/', include('demo_project.glasses.urls')),

]
