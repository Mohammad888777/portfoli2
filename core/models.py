from django.db import models



class Slider(models.Model):

    image=models.ImageField(
        null=True,
        blank=True
    )

    title=models.CharField(
        max_length=250,
         null=True,
        blank=True
        
    )


    description=models.TextField(
         null=True,
        blank=True
    )


    class Meta:
        verbose_name="silder"
        verbose_name_plural="silder"






class Project(models.Model):

    image=models.ImageField(
        null=True,
        blank=True
    )

    title=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    description=models.TextField(
         null=True,
        blank=True

    )

    description2=models.TextField(
         null=True,
        blank=True

    )

    subject=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    type=models.CharField(
            max_length=250,
             null=True,
        blank=True
    )


    bedrooms=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )


    bathrooms=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )


    scale=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    status=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    style=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    class Meta:

        verbose_name="project"
        verbose_name_plural="project"




class ProjectChild(models.Model):

    project=models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
         null=True,
        blank=True

    )




    image=models.ImageField(
        null=True,
        blank=True
    )


    class Meta:
        verbose_name="ProjectChild"
        verbose_name_plural="ProjectChild"



class Gallery(models.Model):

    image=models.ImageField(
        null=True,
        blank=True
    )

    title=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    subject=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    class Meta:
        verbose_name="Gallery"
        verbose_name_plural="Gallery"


class GalleryChild(models.Model):

    gallery=models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
         null=True,
        blank=True

    )




    image=models.ImageField(
        null=True,
        blank=True
    )



    class Meta:
        verbose_name="GalleryChild"
        verbose_name_plural="GalleryChild"



class AboutMe(models.Model):

    image=models.ImageField(
        null=True,
        blank=True,
        verbose_name="image",
        help_text="image"
    )



    description=models.TextField(
         null=True,
        blank=True

    )



    project_completed=models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="project completed"
    )


    awards=models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="awards completed"
    )


    years_experience=models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="years experience"
    )


    satisfaction=models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="satisfaction percent"
    )



    myemail=models.EmailField(
        null=True,
        blank=True,
        max_length=250,
        verbose_name="email address"
    )

    phone=models.CharField(
         null=True,
        blank=True,max_length=250,
        verbose_name="my phone"
    )

    address=models.CharField(
        null=True,
        blank=True,max_length=250,
        verbose_name="my address"
    )


    class Meta:
        verbose_name="AboutMe"
        verbose_name_plural="AboutMe"


class OurService(models.Model):


    title=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )


    description=models.TextField(
         null=True,
         blank=True,

    )


    class Meta:
        verbose_name="OurService"
        verbose_name_plural="OurService"