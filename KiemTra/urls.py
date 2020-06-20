from django.urls import path
from . import views

urlpatterns = [
    path('', views.layDSMon, name="DSMon"),
    path('mon<idmon>/', views.layDSBaiKT),
    path('mon<idmon>/bai<idbai>/',views.xuLyFormCauHoi, name="ShowCauHoi"),
    path('mon<idmon>/bai<idbai>/ketqua/',views.hienThiKQ, name="ShowKQ"),
]