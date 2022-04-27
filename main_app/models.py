from django.db import models
# import the reverse function
from django.urls import reverse

class Puppy(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

    # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'puppy_id': self.id})

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Add new Feeding model below Puppy model
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  puppy = models.ForeignKey(Puppy, on_delete=models.CASCADE)
  def __str__(self):
		    # this method will gives us the friendly meal choices value, so like Breakfast instead of B
		    return f"{self.get_meal_display()} on {self.date}"
   
    

	 

	  

