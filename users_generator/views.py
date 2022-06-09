from django.shortcuts import render

from users_generator.services import generator_of_users


def index(request):
    return render(request, 'index.html')


def generate_humans_view(request, quantity: int = 100) -> str:
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        users = generator_of_users(amount_of_users=int(quantity))
    else:
        users = generator_of_users(amount_of_users=quantity)
    return render(request, 'users-generator.html', locals())
