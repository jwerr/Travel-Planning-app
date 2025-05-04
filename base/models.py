from django.db import migrations, models
from django.contrib.auth.models import User


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_auto_some_migration'),  # Adjust this to your latest migration
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

class TravelPackage(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    available_slots = models.IntegerField()

    def __str__(self):
        return self.name
    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attractions = models.TextField(blank=True)
    visit_hours = models.TextField(blank=True)
    best_time = models.TextField(blank=True)
    duration = models.TextField(blank=True)
    shopping = models.TextField(blank=True)
    restaurants = models.TextField(blank=True)
    hotels = models.TextField(blank=True)
    image = models.ImageField(upload_to='destinations/images', blank=True)
    video = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    destinations = models.ManyToManyField(Destination, related_name="packages")

    def __str__(self):
        return self.name
