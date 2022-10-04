from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # 한땀 한땀 
        # 여기서 정해야 함 
        # 필요힐때 바꿀수있음!
        fields = ['title', 'content']