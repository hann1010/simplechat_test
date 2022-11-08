from django import forms
from .models import Chat_post
from ckeditor.widgets import CKEditorWidget


class Chat_view_Form(forms.ModelForm):
    content = forms.CharField(max_length=100, widget=CKEditorWidget(attrs={'cols':42, 'rows': 5}))
    class Meta:
        model = Chat_post
        fields = ['content']
        