from django.shortcuts import render
from .models import Slider, Project, Gallery,AboutMe,OurService
from django.db import transaction
from django.contrib.sites.shortcuts  import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt







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






@csrf_exempt
def send_email(request):

    if request.method=="POST":


        name = request.POST.get("name")
        email_address = request.POST.get("email")
        project = request.POST.get("project")
        subject = request.POST.get("subject")

        body = render_to_string(
            template_name="email_message.html",
            context={
                "name":name,
                "email_address":email_address,
                "project":project,
                "subject":subject,

            }
        )
        
    
        try:
            new_email_to_send = EmailMultiAlternatives(subject, "", to=[
                "nasimslhn@gmail.com"
            ])
            new_email_to_send.attach_alternative(body, "text/html")  # تنظیم محتوای HTML
            new_email_to_send.send()

            print("Email sent successfully!")



        except Exception as e:
            print(e)
            pass
            

        return JsonResponse({
            "send":True
        })
        

