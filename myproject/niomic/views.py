from django.http import HttpResponse

def index(request):
    
    halo = "<h1> HALO DUNIA"
    
    return HttpResponse(halo)
