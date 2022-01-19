from django.http import HttpResponse


def index(request):
    return HttpResponse('I`ve done it!!!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
