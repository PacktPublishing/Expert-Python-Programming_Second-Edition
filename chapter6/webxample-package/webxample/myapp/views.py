from django.shortcuts import render


# Create your views here.
def delay(request):
    import time; time.sleep(2)
    return "foo"
