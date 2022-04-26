from django.shortcuts import render
# import a create view 
# import UpdateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from .models import Puppy

# Add the Puppy class & list and view function below the imports
# when we have a model the classPuppy and puppies lists will be deleted 

# the template the CreateView and the UpdateView use is the same
class PuppyCreate(CreateView):
    model = Puppy
    fields = '__all__'
    success_url = '/puppies/'
class PuppyUpdate(UpdateView):
  model = Puppy
  # Let's disallow the renaming of a Puppy by excluding the name field!
  fields = ['breed', 'description', 'age']

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'



# Define the home view
def home(request):
  return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
 # Add new view
def puppies_index(request):
  puppies = Puppy.objects.all() #use our model to get our cats table in psql
  return render(request, 'puppies/index.html', { 'puppies': puppies })

def puppies_detail(request, puppy_id):
    puppy = Puppy.objects.get(id=puppy_id)
    return render(request, 'puppies/detail.html', { 'puppy': puppy })