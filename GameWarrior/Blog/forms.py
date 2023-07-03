from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = "__all__"
        fields = ["title","game", "content", "tag", "score"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "game": forms.Select(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control', "rows": 5}),
            "tag": forms.CheckboxSelectMultiple(attrs={'class': ""}),
            "score": forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1, 'max': 10.0, 'min': 0.1, 'placeholder': 'Value'}),

        }




