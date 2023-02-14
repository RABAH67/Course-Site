from django.db import models
from django.utils import timezone
# Create your models here.






class Comments(models.Model):



    email = models.EmailField(blank=True, null=True)

    text_comment = models.TextField(blank=True, null=True)

    name = models.CharField(max_length=250,blank=True, null=True)

    date = models.DateTimeField(default=timezone.now,blank=True, null=True)



    
    class Meta:

        ordering = ('-date',)


    def __str__(self):
        return self.name
         



class Dawrat(models.Model):

    title  = models.CharField(max_length=200, blank=True, null=True)

    description = models.TextField(max_length=200, blank=True, null=True)

    price = models.FloatField(blank=True, null=True)

    photo_url = models.TextField(max_length=5000, blank=True, null=True)

    date = models.DateTimeField(default=timezone.now,blank=True, null=True)

    description_detail =  models.TextField(max_length=5000, blank=True, null=True)

    com = models.ForeignKey(Comments,on_delete=models.DO_NOTHING,blank=True, null=True)



    class Meta:

        ordering = ('-date',)


    def __str__(self):
        return self.title






class PostMainHome(models.Model):


    photo_url = models.TextField(max_length=5000, blank=True, null=True)
    title  = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title





class Offre(models.Model):

    status_ofre = [


        ('Pro','Pro'),

        ('Enterprise',"Enterprise")

    ]

    status = models.CharField(max_length=50, choices=status_ofre, blank=True, null=True)

    price = models.FloatField(blank=True, null=True)

    program_of_offre1 = models.CharField(max_length=200,blank=True)

    program_of_offre2 = models.CharField(max_length=200,blank=True)

    program_of_offre3 = models.CharField(max_length=200,blank=True)

    program_of_offre4 = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return self.status





class Command(models.Model):



    name = models.CharField(max_length=150,blank=True, null=True)

    prenom = models.CharField(max_length=150,blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    num = models.IntegerField(blank=True, null=True)

    date = models.DateTimeField(default=timezone.now,blank=True, null=True)



    
    class Meta:

        ordering = ('-date',)


    def __str__(self):
        return self.name
