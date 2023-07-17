from django.shortcuts import render
from django.http import JsonResponse
from .forms import MyForm

# Create your views here.
def index(request):
    """"""
    return render(request, "index.html")

def chat(request):
    """"""
    if request.method == 'POST':
        prompt = request.POST.get('prompt')

        # Return a JSON response indicating the success or any other relevant information
        response_data = {'message': 'Form data processed successfully'}
        return JsonResponse(response_data)

    # Handle other HTTP methods if needed
    else:
        return JsonResponse({'message': 'Invalid request method'})
    # return render(request, "mainpage/chat.html")


def getdata(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data
            print(query)
            return JsonResponse({'status': 'success'})  # Return a JSON response indicating success
        else:
            print(form.errors)  
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)  # Return a JSON response indicating errors
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})
