from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # 한땀 한땀
        # 여기서 정해야 함
        # 필요힐때 바꿀수있음!
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control mt-2",
                }
            ),
            "content": forms.Textarea(attrs={"class": "form-control mt-2", "rows": 10}),
        }
        labels = {
            "title": "제목",
            "content": "내용",
        }
