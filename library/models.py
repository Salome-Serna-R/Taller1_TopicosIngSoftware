from django.db import models

# Create your models here.
class Content(models.Model):
    STRESS = 'stress'
    DEPRESSION = 'depression'
    ANXIETY = 'anxiety'

    TOPIC_CHOICES = [
        (STRESS, 'Stress'),
        (DEPRESSION, 'Depression'),
        (ANXIETY, 'Anxiety'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/content/images/')
    url = models.URLField(blank=True)
    topic = models.CharField(
        max_length=10,
        choices=TOPIC_CHOICES,
    )

    def __str__(self):
        return self.title
    
class Searches(models.Model):
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.choice