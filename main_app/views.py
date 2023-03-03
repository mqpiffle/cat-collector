from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Cat

# Create your views here.
# views.py

# Add this cats list below the imports
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# view functions match urls to code
# like controllers in express

# define our home view function

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    #  we can gather relations from SQL using our model methods
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })

# detail(show) route
# cat_id is expecting an integer in our url
def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 'cat': cat })

class CatCreate(CreateView):
    model = Cat
    # the fields attribute is requires for a CreateView
    # tells the template what form fields to include
    fields = '__all__'
    # or more detailed:
    # fields = ['name', 'description', ...fieldsToInclude]
    # success requires a redirect
    # success_url = '/cats'

class CatUpdate(UpdateView):
    model = Cat
    # custom field example to disallow renaming a cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'