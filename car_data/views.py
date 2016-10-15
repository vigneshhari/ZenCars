from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Car_data_new,Car_data_old

# Create your views here.

# Fields in Car_Details ... General Information/Review --> Features/Specs --> User Reviews --> Estimated Fuel Cost --> Gallery

def search(request):
	lis = []
	lis.append({"test":"test"})
	lis.append({"test":"test"})
	return render(request,"listv.html",{'cardata' : lis , 'resultlen' : len(lis)})

def viewadd(request):
	print "hi there"
	step = request.session.get('step','1')
	link = 'a' + str(step) +".html"
	return render(request,link)


def add(request):
	#print request.GET.viewkeys() 
	user_id = request.session.get("id",'1')
	step = request.session.get('step','1')
	car_id = request.session.get('car_id',None)
	print step
	if(int(step) == 1):
			Car_data_old(user_id=user_id,brand=request.GET.get("brand"),name=request.GET.get("name"),year=int(request.GET.get("year")),body_type=request.GET.get("type"),fuel=request.GET.get("fuel"),transmission=request.GET.get("transmission"),reading=request.GET.get("reading"),milege=request.GET.get("milege"), confirmed=0).save()
			obj = Car_data_old.objects.latest('car_id')
			request.session['step'] = '2'
			request.session['car_id'] = obj
			print obj
			return HttpResponseRedirect("/car/add")	
	return 0