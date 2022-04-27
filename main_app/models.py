from django.db import models
# import the reverse function
from django.urls import reverse
from datetime import date
# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  # Add this method
  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Puppy(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'puppy_id': self.id})

def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

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
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']
	 

	  

