# Generated by Django 3.0.5 on 2020-06-08 03:18

import KiemTra.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Chinh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaiKiemTra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenBai', models.CharField(max_length=100)),
                ('NoiDung', models.FileField(blank=True, default='No file', upload_to=KiemTra.models.taoPathChoBaiKT)),
            ],
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenLop', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ThanhTich',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diem', models.FloatField(default=0.0)),
                ('baikiemtra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KiemTra.BaiKiemTra')),
                ('thanhvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chinh.ThanhVien')),
            ],
        ),
        migrations.CreateModel(
            name='Mon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenMon', models.CharField(max_length=50)),
                ('lop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KiemTra.Lop')),
            ],
        ),
        migrations.AddField(
            model_name='baikiemtra',
            name='mon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='KiemTra.Mon'),
        ),
    ]