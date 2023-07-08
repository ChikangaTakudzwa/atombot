from django.shortcuts import render
from .forms import prompt

# Create your views here.
def index(request):
    """"""
    


    return render(request, "index.html")

def getdata(request):
    """"""
    if request.method == 'POST':
        form = prompt(request.POST)

        if form.is_valid():
            query = form.cleaned_data['prompt']
            print(query)
    else:
        form = prompt()

    return {'form': form}
