from django import forms
class UploadFileForm(forms.Form):
    title=forms.CharField(max_length=50)
    file=forms.FileField()

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)

class NameForm(forms.Form):
    your_name=forms.CharField(label='Your name',max_length=100)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)

class ArticleForm(forms.Form):
    title=forms.CharField(max_length=100)
    pub_date=forms.DateField()

