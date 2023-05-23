from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import Form

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})

def add_album(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'add_album.html', {'form': form})

def update(request, id):
    album = Album.objects.get(pk = id)
    album.name = request.POST.get('name')
    album.save()

def delete(request, id):
    album = Album.objects.get(pk = id)
    album.delete()
    