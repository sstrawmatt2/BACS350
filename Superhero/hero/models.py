from django.db import models
from django.urls import reverse

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
#    strength = models.CharField(max_length=200, null=True)
#    weakness = models.CharField(max_length=200, null=True)
#    Superhero.objects.create(name='Hulk', identity='Bruce Banner', power='Super strength', weakness='Black Widow')
    image = models.CharField(max_length=200, null=True)
    # null is the default value
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('hero_detail', args=[str(self.id)])