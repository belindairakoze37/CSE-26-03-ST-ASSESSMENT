from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_quality', 'date_of_publishing', 'video_file', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Video Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Description (Optional)'}),
            'video_quality': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Video quality'}),
            'date_of_publishing': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Date of Publishing'}),
            'video_file': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'video/*'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }
        error_messages = {
            'title': {'required': 'required field.'},
            'video_quality': {'required': 'required field.'},
            'date_of_publishing': {'required': 'required field.'},
            'video_file': {'required': 'required field.'},
            'thumbnail': {'required': 'required field.'},
        }
