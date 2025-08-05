from django.shortcuts import render
from .models import Slider, Project, Gallery,AboutMe,OurService

def portfolio_view(request):
    sliders = Slider.objects.all()
    projects = Project.objects.all()
    hero_project = Project.objects.first()  # یا یک پروژه خاص را انتخاب کنید
    galleries = Gallery.objects.all()

    a=AboutMe.objects.last()
    service=OurService.objects.all()

    context = {
        'sliders': sliders,
        'projects': projects,
        'hero_project': hero_project,
        'galleries': galleries,
        "a":a,
        "service":service
    }
    return render(request, 'portfolio/index.html', context)