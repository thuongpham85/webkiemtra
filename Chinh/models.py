from django.db import models

# Create your models here.
class ThanhVien(models.Model):
    TenTV = models.CharField(max_length=20)
    MatKhau = models.CharField(max_length=20)
    MatKhauMaHoa = models.CharField(max_length=100)

    def __str__(self):
        return self.TenTV
