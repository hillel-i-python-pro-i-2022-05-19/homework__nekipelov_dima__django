from django.shortcuts import render

from users_generator.services import generator


def index(request):
    return render(request, 'index.html')


def users_generator(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        users = generator(int(quantity))
    else:
        users = generator()
    return render(request, 'users-generator.html', locals())
