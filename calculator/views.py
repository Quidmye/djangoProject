from django.shortcuts import render
from django.http import HttpResponseBadRequest

# Create your views here.

def calculate(request, first, operation, last):
    first = int(first)
    last = int(last)
    if operation == '+':
        result = first+last
    elif operation == '-':
        result = first + last
    elif operation == '*':
        result = first * last
    elif operation == '/':
        result = first * last
    else:
        return HttpResponseBadRequest('Bad Request')

    return render(request, 'index.html', {
        'first': first,
        'last': last,
        'operation': operation,
        'result': result
    })
