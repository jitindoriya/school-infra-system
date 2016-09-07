from django.shortcuts import render


# Create your views here.
def asprincipal(request):
    return render(request, 'principal/principal.html', {})
