from django.shortcuts import render
from django.http import JsonResponse
from .forms import prompt

# Create your views here.
def index(request):
    """"""
    return render(request, "index.html")


def getdata(request):
    if request.method == 'POST':
        form = prompt(request.POST)
        if form.is_valid():
            query = form.cleaned_data
            print(query)
            return JsonResponse({'status': 'success'})  # Return a JSON response indicating success
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)  # Return a JSON response indicating errors
    else:
        form = prompt()
    return render(request, 'index.html', {'form': form})
