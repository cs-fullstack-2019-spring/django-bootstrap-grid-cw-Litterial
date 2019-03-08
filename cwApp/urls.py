from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('p2/',views.p2,name='p2'),
    path('p3/',views.p3,name='p3'),

]