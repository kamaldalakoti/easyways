from django.shortcuts import render
from home.models import Hospital,Shop,Tour

# Create your views here.
def home(request):
    data = Hospital.objects.all().count()
    shops = Shop.objects.all().count()
    tour = Tour.objects.all().count()
    go = {'goa':data, 'shop':shops, 'tours': tour}
    return render(request, 'home.html',go)  
def hospital(request):
    query = 'district'
    query2 = 'base'
    data = Hospital.objects.all()
    dataName = Hospital.objects.filter(Location__icontains=query)
    dataName1 = Hospital.objects.filter(Location__icontains=query2)

    sta = {'upload_1':dataName ,'upload_2': dataName1 }
    return render(request, 'hospital.html',sta)  
def dentist(request):
    return render(request, 'dentist.html')  
def search(request):
    # data = Hospital.objects.all()
    
    query = request.GET['query']
    # query1 = request.GET['query1']
    dataDoctor = Hospital.objects.filter(Doctor__icontains=query)
    dataDoctor_of = Hospital.objects.filter(Doctor_of__icontains=query)
    dataName = Hospital.objects.filter(Name__icontains=query)
    datatime = Hospital.objects.filter(Timing__icontains=query)
    dataloc = Hospital.objects.filter(Location__icontains=query)


   
    data = dataDoctor.union(dataName).union(datatime).union(dataloc).union(dataDoctor_of)
    sta = {'upload_1':data, 'query': query  } 
    # if query == data :
        # params = {'allhospital':allhospital}
    return render(request, 'search.html', sta )  
    # else:
        # bata = "'No Search Results'"
        # bata = {'No Search Results' : bata}
        # return render(request, 'search.html', bata)

def options(request):
     
    query = request.GET['query']
    dataDoctor = Hospital.objects.filter(Doctor__icontains=query)
    dataDoctor_of = Hospital.objects.filter(Doctor_of__icontains=query)
    dataName = Hospital.objects.filter(Name__icontains=query)
    datatime = Hospital.objects.filter(Timing__icontains=query)
    dataloc = Hospital.objects.filter(Location__icontains=query)


    data = dataDoctor.union(dataName).union(datatime).union(dataloc).union(dataDoctor_of)
    sta = {'upload_1':data  } 
    return render(request, 'options.html', sta )  


# shop    
def shop(request):
    types = 'sweets'
    types2 = 'paan'
    # nanital = ' nanital'
    # data3 = 'naini peak '
    passit = Shop.objects.filter(Product_name__icontains=types)
    passit2 = Shop.objects.filter(Product_name__icontains=types2)
    data = {'data1': passit , 'data2': passit2}
    return render(request, 'shop.html', data) 

def shop_search(request):
    # data = Shop.objects.all()
    query  = request.GET['query']
    shop_name = Shop.objects.filter(Shop_name__icontains=query)
    city = Shop.objects.filter(city__icontains=query)
    state = Shop.objects.filter(State__icontains=query)
    Shop_discription = Shop.objects.filter(Shop_discription__icontains=query)
    Product_name = Shop.objects.filter(Product_name__icontains=query)

    # shop_name = Shop.objects.filter(Shop_name__icontains=query)
    


    data = shop_name.union(shop_name).union(city).union(state).union(Shop_discription).union(Product_name)
    dataa = {'data1': data ,'query': query }
    return render(request, 'shop_search.html' , dataa) 

def map(request):
    value = request.GET['value1']
    value_1 = request.GET['value2']
    value_2 = request.GET['value3']
    data = {'value1':value,'value2':value_1,'value3':value_2}
    print(value)
    return render(request, 'map.html', data ) 
def option_shop(request):
    query = request.GET['types']
    shop_name = Shop.objects.filter(Shop_name__icontains=query)
    city = Shop.objects.filter(city__icontains=query)
    state = Shop.objects.filter(State__icontains=query)
    Shop_discription = Shop.objects.filter(Shop_discription__icontains=query)
    Product_name = Shop.objects.filter(Product_name__icontains=query)
    # shop_name = Shop.objects.filter(Shop_name__icontains=query)
    


    data = shop_name.union(shop_name).union(city).union(state).union(Shop_discription).union(Product_name)
    dataa = {'data1': data ,'types': query }
    return render(request, 'option_shop.html', dataa) 
def tour(request):
    
    data = Tour.objects.all()
    data1 = {'data2':data}
    return render(request, 'tour.html',data1)

def index(request):
    map1 = request.POST.get('map1')
    print(map1)
    return render(request, 'maps/index.html')