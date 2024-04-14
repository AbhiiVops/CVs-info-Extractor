from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_cv, name='upload_cv'),
    path('download/<str:filename>/', views.download_excel, name='download_excel'),
]
