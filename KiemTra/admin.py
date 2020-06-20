from django.contrib import admin
from .models import Lop, Mon, BaiKiemTra, DeTuLuan, ThanhTich, HinhLienQuanBaiKT

# Register your models here.
class MonAdmin(admin.TabularInline):
    model = Mon
    extra = 3
class LopAdmin(admin.ModelAdmin):
    list_display=['id','TenLop']
    inlines = [MonAdmin]

class BaiKT(admin.TabularInline):
    model = BaiKiemTra
    extra = 3

class TuLuanAdmin(admin.TabularInline):
    model = DeTuLuan
    extra = 3

class MonKTAdmin(admin.ModelAdmin):
    list_display=['id','TenMon']
    inlines = [BaiKT, TuLuanAdmin]

class HinhLQBaiKT(admin.TabularInline):
    model = HinhLienQuanBaiKT
    extra = 3

class BaiKTAdmin(admin.ModelAdmin):
    list_display=['id','TenBai','NoiDung']
    inlines = [HinhLQBaiKT]

class ThanhTichAdmin(admin.ModelAdmin):
    list_display= ['id','Diem','thanhvien', 'baikiemtra']

admin.site.register(Lop, LopAdmin)
admin.site.register(Mon, MonKTAdmin)
admin.site.register(BaiKiemTra, BaiKTAdmin)
admin.site.register(ThanhTich, ThanhTichAdmin)