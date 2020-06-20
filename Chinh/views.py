from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import ThanhVien
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages, sessions
#from KiemTra.models import Mon, Lop

# Create your views here.
def index(request):
    return render(request,"Chinh/TrangChu.html")

def lienHe(request):
    return render(request, "Chinh/LienHe.html")

def luuThanhVien(ten,mk1):
    tv = ThanhVien()
    tv.TenTV = ten
    tv.MatKhau = mk1
    tv.MatKhauMaHoa = make_password(mk1)
    tv.save()

def dangKy(request):
    if request.method=='POST':
        ten = request.POST["username"]
        mk1 = request.POST["password1"]
        mk2=request.POST["password2"]
        try:
            tv = ThanhVien.objects.get(TenTV = ten)
        except ThanhVien.DoesNotExist:
            luuThanhVien(ten,mk1)
            #messages.success(request, 'Dang ky thanh cong. Vui long dang nhap!')
            return redirect("/dangkythanhcong")
        else: 
            messages.error(request, "Ten thanh vien da ton tai")
    return render(request, "Chinh/DangKy.html")

def dangKyThanhCong(request):
    return render(request, "Chinh/TBDkyThanhCong.html")

def dangNhap(request):
    if request.method == "POST":
        ten = request.POST['username']
        mk = request.POST['password']
        try:
            tv = ThanhVien.objects.get(TenTV = ten)
        except ThanhVien.DoesNotExist:
            messages.error(request, "Ten thanh vien khong dung!")
        else:
            if check_password(mk, tv.MatKhauMaHoa):
                request.session['tentk'] = ten
                request.session['idtv'] = tv.id
                return redirect("/")
            else:
                messages.error(request, "Mat khau khong dung!")
    return render(request, 'Chinh/DangNhap.html')

def dangXuat(request):
    del request.session['tentk']
    del request.session['idtv']
    del request.session['tongch']
    del request.session['pathfilekq']
    del request.session['filekq']
    #del request.session['tongch']
    request.session.pop("tongch", None)
    return redirect("/")


