from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('puppies/', views.puppies_index, name='index'),
  path('puppies/<int:puppy_id>/', views.puppies_detail, name='detail'),
  path('puppies/create/', views.PuppyCreate.as_view(), name='puppies_create'),
  # Add the new routes below
  path('puppies/<int:pk>/update/', views.PuppyUpdate.as_view(), name='puppies_update'),
  path('puppies/<int:pk>/delete/', views.PuppyDelete.as_view(), name='puppies_delete'),
]