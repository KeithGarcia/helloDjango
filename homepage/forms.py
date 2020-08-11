from django import forms
from homepage.models import Recipe, Author


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=10)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]
