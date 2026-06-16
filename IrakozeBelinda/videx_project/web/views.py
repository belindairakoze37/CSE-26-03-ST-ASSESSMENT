from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm
from .models import Video
from django.contrib import messages as message

# Create your views here.
def home(request):
    return render(request, 'home.html')


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})


def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'video_detail.html', {'video': video})


def add_video(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            message.success(request, 'Video added successfully!')
            return redirect('add_video')
        else:
            message.error(request, 'Please fix the errors below and re-upload the files.')

    return render(request, 'add_video.html', {'form': form})
