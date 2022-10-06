from django import forms
from .models import Infos


class InfosForm(forms.ModelForm):
    class Meta:
        model = Infos
        # 한땀 한땀
        # 여기서 정해야 함
        # 필요힐때 바꿀수있음!
        fields = ["title", "summary", "running_time"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control mt-2",
                }
            ),
            "summary": forms.Textarea(attrs={"class": "form-control mt-2", "rows": 10}),
            "running_time": forms.TextInput(
                attrs={
                    "class": "form-control mt-2",
                }
            ),
        }
        labels = {
            "title": "제목",
            "summary": "줄거리",
            "running_time": "러닝 타임",
        }
