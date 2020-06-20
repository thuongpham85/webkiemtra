from django.urls import path
from . import views

app_name = 'Chinh'
urlpatterns = [
    path('', views.index ),
    path('dangky/',views.dangKy, name="Register"),
    path('dangkythanhcong/', views.dangKyThanhCong),
    path('dangnhap/', views.dangNhap, name="Login"),
    path('dangxuat/', views.dangXuat, name="Logout"),
    path('lienhe/', views.lienHe, name="contact"),
]