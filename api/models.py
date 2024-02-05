from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count
from django.core.validators import MinValueValidator, MaxValueValidator

class Meal(models.Model): 
    title = models.CharField(max_length=250)
    description = models.TextField() 

    def no_of_rating(self):
        return Rating.objects.filter(meal=self).aggregate(num_of_rating=Count('meal_id')) 

    def avg_rating(self): 
        return Rating.objects.filter(meal=self).aggregate(rate_avg=Avg('stars', default=1))

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



