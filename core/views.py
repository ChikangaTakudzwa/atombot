from django.shortcuts import render
from .forms import prompt

# Create your views here.
def index(request):
    """"""
    if request.method == 'POST':
        form = prompt(request.POST)

        if form.is_valid():
            query = form.cleaned_data['prompt']
            print(query)


    return render(request, "index.html")
