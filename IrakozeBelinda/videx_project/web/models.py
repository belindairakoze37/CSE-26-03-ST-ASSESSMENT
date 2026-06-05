from django.db import models

# Create your models here.
class Video(models.Model):
    VIDEO_QUALITY_CHOICES = [
        ('240p', '240p'),
        ('360p', '360p'),   
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    ] 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video_quality = models.CharField(max_length=50, choices=VIDEO_QUALITY_CHOICES)
    date_of_publishing = models.DateField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return self.title