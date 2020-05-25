from django import forms 
from .models import Post , Contact , Comment
from django_filters import CharFilter




class PostForm(forms.ModelForm):
    status = CharFilter(field_name='status', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = '__all__'
    class Media:
        js = ('js/tinyInject.js',)
    
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'full-width','placeholder': 'Wrire a Comment', 'rows': '4' , 'cols' : '50'}))
    name  = forms.CharField(label="", widget=forms.TextInput(attrs={'class' :'full-width','placeholder': 'User Name'}))
    email  = forms.CharField(label="", widget=forms.TextInput(attrs={'class' :'full-width','placeholder': 'Email'}))
    class Meta:
        model = Comment
        fields = ['content','name','email']


