from django.contrib import admin
from .models import Project, Gallery,ProjectChild,GalleryChild,Slider,AboutMe,OurService

admin.site.register([
    Project, Gallery,ProjectChild,GalleryChild,Slider,AboutMe,OurService
])