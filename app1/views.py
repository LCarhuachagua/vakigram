from django.shortcuts import HttpResponse

# Create your views here.

def say_hi(request, name, age):
    #return a greeting.
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, Welcome to Vakigram'.format(name)
    return HttpResponse(message)
