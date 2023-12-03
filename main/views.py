from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        print(f'{name} {email} {massage}')


    return render(request, 'main/index.html')
