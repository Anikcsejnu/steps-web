from django.shortcuts import render
from .models import Gallery, GalleryImage
# Create your views here.
def gallery(request):
    print(Gallery.objects.all())
    context = {
        'galleries': Gallery.objects.all(),
    }
    return render(request, 'gallery/gallery.html', context)


def gallerySingle(request, galleryid):

    print(galleryid)
    
    context = {
        'gallery': Gallery.objects.filter(pk=galleryid).first(),
        'galleryImages': GalleryImage.objects.filter(gallery_name_id=galleryid).all(),
    }
    return render(request, 'gallery/gallerysingle.html', context)