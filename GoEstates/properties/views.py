from django.shortcuts import render, get_object_or_404
from users.decorators import buyer_required
from .models import Property, Category, PropertyImages,Videos


def homepage(request):
    property = Property.objects.all()
    return render(request, 'property/home.html', {'property':property})

def properties(request):
    property = Property.objects.all()
    return render(request, 'property/property.html', {'property':property})

@buyer_required
def details(request, pk):
    property = get_object_or_404(Property, pk=pk)
    images = PropertyImages.objects.filter(property=property)
    video = Videos.objects.filter(property=property)
    related_properties = Property.objects.filter(category=property.category).exclude(pk=pk)
    return render(request, 'property/details.html',{'property': property,
                                                    'video':video,
                                                    'related_property':related_properties,
                                                    'images':images,})
def vid(request, pk):
    property = get_object_or_404(Property, pk=pk)
    video = Videos.objects.get(property=property)

    return render(request, 'property/video.html', {'video':video})