
from django.contrib import admin
from django.urls import path
from Apoth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('floinfo/<int:pk>', views.flower_detail),
    path('floinfo/', views.flower_list),
]
