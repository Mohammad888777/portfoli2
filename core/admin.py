from django.contrib import admin
from .models import Project, Gallery,ProjectChild,GalleryChild,Slider,AboutMe,OurService

admin.site.site_header = "nasimsalehnia panel"  # متن هدر بالای صفحه
admin.site.site_title = "nasimsalehnia"        # عنوان تب مرورگر
admin.site.index_title = "Welcome Nasim"  # مت


admin.site.register([
    Project, Gallery,ProjectChild,GalleryChild,Slider,AboutMe,OurService
])