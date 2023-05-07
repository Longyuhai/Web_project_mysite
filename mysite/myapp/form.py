from django import forms

class CommentForm(forms.Form):
    name=forms.CharField(max_length=50)
    comment=forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
