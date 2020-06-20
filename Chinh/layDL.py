from KiemTra.models import Lop, ThanhTich

def layDL(request):
    dslop = Lop.objects.all()
    dsthanhtich = ThanhTich.objects.all().order_by('Diem')[:5]
    return {'dslop': dslop, 'dsthanhtich': dsthanhtich}
