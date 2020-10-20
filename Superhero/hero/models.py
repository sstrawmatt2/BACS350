from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    image = models.CharField(max_length=20, null=True)
    # null is the default value
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('hero.list', args=[str(self.id)])