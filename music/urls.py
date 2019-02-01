from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/', views.DetailView.as_view(), name='detail'),

]
