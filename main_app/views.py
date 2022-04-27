from django.shortcuts import render, redirect #always redirect after making changes to the database
# import a create view 
# import UpdateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Add the following import
from .models import Puppy, Toy 
from .forms import FeedingForm

# Add the Puppy class & list and view function below the imports
# when we have a model the classPuppy and puppies lists will be deleted 

# the template the CreateView and the UpdateView use is the same
class PuppyCreate(CreateView):
    model = Puppy
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/puppies/' # get_absolute_url doesnt work for create/update , so i can create a success_url and itll work
class PuppyUpdate(UpdateView):
  model = Puppy
  fields = ['breed', 'description', 'age']
  success_url = '/puppies/'

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
  toys_puppy_doesnt_have = Toy.objects.exclude(id__in = puppy.toys.all().values_list('id'))

  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', {
    # include the puppy and feeding_form in the context
    'puppy': puppy, 'feeding_form': feeding_form,
    'toys': toys_puppy_doesnt_have
  })

def add_feeding(request, puppy_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the puppy_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = puppy_id
    new_feeding.save()
  return redirect('detail', puppy_id=puppy_id)
  
def assoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.add(toy_id)
  return redirect('detail', puppy_id=puppy_id)

def unassoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.remove(toy_id)
  return redirect('detail', puppy_id=puppy_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'