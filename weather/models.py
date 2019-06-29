from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25,help_text = 'City Name', null=True)
    temp = models.DecimalField(max_digits = 4,decimal_places = 2,help_text = 'Temperature', null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

