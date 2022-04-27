from django.shortcuts import render, redirect
# import a create view 
# import UpdateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from .models import Puppy
from .forms import FeedingForm

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
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', {
    # include the puppy and feeding_form in the context
    'puppy': puppy, 'feeding_form': feeding_form
  })
def add_feeding(request, puppy_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = puppy_id
    new_feeding.save()
  return redirect('detail', puppy_id=puppy_id)