from django.shortcuts import render, redirect
from categories.forms import CatagoryFrom

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        catagory_form = CatagoryFrom(request.POST)
        if catagory_form.is_valid():
            catagory_form.save()
            return redirect('add_category')
    else:
        catagory_form = CatagoryFrom()
    return render(request, 'add_catagory.html', {'form' : catagory_form})