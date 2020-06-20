import os
import unicodedata
from django.db import models
from Chinh.models import ThanhVien

# Create your models here.
class Lop(models.Model):
    TenLop = models.CharField(max_length=20)

    def __str__(self):
        return self.TenLop

class Mon(models.Model):
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    MaMon = models.CharField(max_length=10, default="thu", blank=True)
    TenMon = models.CharField(max_length=50)

    def __str__(self):
        return self.MaMon

def taoPathChoBaiKT(instance, filename):
    pathTN = "TracNghiem/" + instance.mon.MaMon + "/" + instance.MaBai
    return os.path.join(pathTN, filename)
class BaiKiemTra(models.Model):
    mon = models.ForeignKey(Mon, on_delete=models.CASCADE)
    MaBai = models.CharField(max_length=10, default="thu", blank=True)
    TenBai = models.CharField(max_length=100)
    NoiDung = models.FileField(default="Khong co bai kiem tra", blank=True, upload_to=taoPathChoBaiKT)

    def __str__(self):
        chuoi = self.mon.MaMon + "_" + self.MaBai
        return chuoi

def taoPathChoHinhLQBaiKT(instance, filename):
    pathHinhBaiKT = "TracNghiem/" + instance.baikiemtra.mon.MaMon + "/" + instance.baikiemtra.MaBai
    return os.path.join(pathHinhBaiKT, filename)
class HinhLienQuanBaiKT(models.Model):
    baikiemtra = models.ForeignKey(BaiKiemTra, on_delete=models.CASCADE)
    HinhLienQuan = models.ImageField(default="Khong co", blank=True, upload_to=taoPathChoHinhLQBaiKT)

def taoPathChoDeTuLuan(instance, filename):
    pathTL = "TuLuan/" + instance.mon.MaMon + "/" + instance.MaBai
    return os.path.join(pathTL, filename)
class DeTuLuan(models.Model):
    mon = models.ForeignKey(Mon, on_delete=models.CASCADE)
    TenDe = models.CharField(max_length=100)
    NoiDungDe = models.FileField(default="Khong co de", blank=True, upload_to=taoPathChoDeTuLuan)
    HuongDanGiai = models.FileField(default="Khong co huong dan giai", blank=True, upload_to=taoPathChoDeTuLuan)

class ThanhTich(models.Model):
    thanhvien = models.ForeignKey(ThanhVien, on_delete=models.CASCADE)
    baikiemtra = models.ForeignKey(BaiKiemTra, on_delete=models.CASCADE)
    Diem = models.FloatField(default=0.0,blank=True)