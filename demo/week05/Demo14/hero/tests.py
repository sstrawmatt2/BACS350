from django.test import TestCase

from .models import Superhero

class HeroTests(TestCase):
    
    def test_hero_model(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        
        
    def test_create(self):
        Superhero.objects.create(name='xxx', identity='yyy')
#        for s in Superhero.objects.all():
#            print("Super", s.name)
        self.assertEqual(len(Superhero.objects.all()), 1)
        self.assertEqual(Superhero.objects.get(pk=1).name,'xxx')
        ## pk = primary key
        self.assertEqual(Superhero.objects.get(pk=1).identity,'yyy')
        
        
        
    def test_update(self):
        Superhero.objects.create(name='Batman', identity='Bruce Wayne')
        x = Superhero.objects.get(pk=1)
        x.name = 'Superman'
        x.save()
        y = Superhero.objects.get(pk=1)
        self.assertEqual(y.name, 'Superman')
        self.assertEqual(y.identity, 'Bruce Wayne')
    
    def test_read(self):
        Superhero.objects.create(name='Batman', identity='Bruce Wayne')
        x = Superhero.objects.get(pk=1)
        self.assertEqual(x.name, 'Batman')
        self.assertEqual(x.identity, 'Bruce Wayne')
        
    
    def test_image(self):
        Superhero.objects.create(name='Batman', identity='Bruce Wayne')
        x = Superhero.objects.get(pk=1)
        x.image = 'Batman.jpg'
        x.save()
        self.assertEqual(x.image, 'Batman.jpg')
    
    
