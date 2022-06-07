from django.http import HttpResponse


def users_generator(request):
    return HttpResponse("Hello, world. You're at the polls index.")
