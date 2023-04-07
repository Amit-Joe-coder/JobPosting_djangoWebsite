from django.shortcuts import render
from mainapp.models import hydrabad,goa,noida,meerut
# Create your views here.
def home_view(request):
    return render(request,'home.html')

def hydrabad_view(request):
    first_list=hydrabad.objects.all()
    city_one='hydrabad'
    mydic_one={'item':first_list,'cityone':city_one}
    return render(request,'info.html',context=mydic_one)

def goa_view(request):
    second_list=goa.objects.all()
    city_two='goa'
    mydic_two={'item':second_list,'citytwo':city_two}
    return render(request,'info.html',context=mydic_two)

def noida_view(request):
    third_list=noida.objects.all()
    city_three='noida'
    mydic_three={'item':third_list,'citythree':city_three}
    return render(request,'info.html',context=mydic_three)

def meerut_view(request):
    fourth_list=meerut.objects.all()
    city_four='meerut'
    mydic_four={'item':fourth_list,'cityfour':city_four}
    return render(request,'info.html',context=mydic_four)