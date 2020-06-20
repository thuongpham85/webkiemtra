from django.contrib import admin
from .models import ThanhVien

# Register your models here.
class TVAdmin(admin.ModelAdmin):
    list_display = ['TenTV','MatKhau','MatKhauMaHoa']

admin.site.register(ThanhVien, TVAdmin)
