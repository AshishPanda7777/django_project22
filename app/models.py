from django.db import models

# Create your models here.
class TOPIC(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name
