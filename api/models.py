from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Meal(models.Model): 
    title = models.CharField(max_length=250)
    description = models.TextField() 

    def __str__(self):
        return self.title 
    
    
class Rating(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self): 
        return str(self.meal) 
    


    class Meta:
        unique_together = (('user', 'meal'))
        index_together = (('user', 'meal'))



