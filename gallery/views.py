from django.shortcuts import render
from .models import Gallery, GalleryImage
# Create your views here.
def gallery(request):
    print(Gallery.objects.all())
    context = {
        'galleries': Gallery.objects.all(),
    }
    return render(request, 'gallery/gallery.html', context)


def gallerySingle(request, galleryname):
    
    context = {
        'gallery': Gallery.objects.filter(gallery_name=galleryname).first(),
        'galleryImages': GalleryImage.objects.filter(gallery_name__gallery_name=galleryname),
    }
    return render(request, 'gallery/gallerysingle.html', context)