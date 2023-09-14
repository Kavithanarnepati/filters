from django.shortcuts import render


# Create your views here.
def built_in_filters(request):
    data='Pardeep Narwal IS mY Favouriate player IN KabaDDI'
    d={'data':data}
    return render(request,'built_in_filters.html',d)