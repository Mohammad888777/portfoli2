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

    area=models.CharField(
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


    year=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    location=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )

    style=models.CharField(
        max_length=250,
         null=True,
        blank=True
    )





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