from django import forms

class FormDangKy(forms.Form):
    tenTK = forms.CharField(max_length=20)
    matKhau = forms.CharField(max_length=20)
    