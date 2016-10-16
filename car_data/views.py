from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import DocumentForm
from .models import Car_data_new,Car_data_old
from user_data.models import User_Account
import datetime

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
	if(step == '4'):
		print "here"
		user_id = request.session.get("id",None)
		data = User_Account.objects.all().filter(user_id = user_id)
		for i in data:
			data = {"name" :i.name , "email" :i.email ,"phone_number" :i.phone_no}
			return render(request,link,data)
	return render(request,link)


def add(request):
	#print request.GET.viewkeys() 
	user_id = request.session.get("id",'1')
	step = request.session.get('step','1')
	car_id = request.session.get('car_id',None)
	if(step == '1'):
			Car_data_old(user_id=user_id,brand=request.GET.get("brand"),name=request.GET.get("name"),year=int(request.GET.get("year")),body_type=request.GET.get("type"),fuel=request.GET.get("fuel"),transmission=request.GET.get("transmission"),reading=request.GET.get("reading"),milege=request.GET.get("milege"), confirmed=0).save()
			obj = Car_data_old.objects.latest('car_id').car_id
			request.session['step'] = '2'
			request.session['car_id'] = obj
			print obj
			return HttpResponseRedirect("/car/add")	
	if(step == '2'):
			feat = []
			for i in request.GET.keys():
				if(request.GET.get(i) != 'ex' and len(request.GET.get(i)) > 0 ):
					for it in str(request.GET.get(i)).split(","):
						if(str(it) != ''):
							feat.append(str(it))
				else:
					if(str(request.GET.get(i)) != ''):
						feat.append(str(request.GET.get(i)))
			feature = ','.join(feat)
			print car_id
			Car_data_old.objects.all().filter(car_id = int(car_id)).update(features = feature)
			request.session['step'] = '3'
			return HttpResponseRedirect("car/add")
	if(step =='3' ):
			temp = Car_data_old.objects.get(car_id = int(car_id))
			temp.photolinks = request.FILES['photolinks']
			temp.videolink = videolink = request.POST.get('videolink','')
			temp.general_information = request.POST.get('review','')
			temp.save()
			request.session['step'] = '4'
			return HttpResponseRedirect("car/add")
	if(step == '4'):
			Car_data_old.objects.all().filter(car_id = car_id).update(price = request.GET.get('price') , Location = request.GET.get("location"))
			request.session['step'] = '5'
			return HttpResponseRedirect("car/add")
	if(step == '5'):
			Car_data_old.objects.all().filter(car_id = car_id).update(hits = 0 , confirmed = 1 ,status = "sell" , date = datetime.datetime.now())
			request.session['step'] = '1'
			return HttpResponseRedirect("user/cars")
	return 0

def view(request):
	type = request.GET.get('type',False)
	id = request.GET.get('id',False)
	if(type == False or id == False):
		return HttpResponseRedirect("/home")
	details = Car_data_old.objects.all().filter(car_id = id)
	data = {}
	for i in details:
		data['brand'] = i.brand
		data['name'] = i.name
		data['photo'] = i.photolinks
		data['price'] = i.price
		data['video'] = i.videolink
		data['read'] = i.reading
		data['general'] = i.general_information
		for n in User_Account.objects.all().filter(user_id = i.user_id):
			data['sellername'] = n.name
			data['phno'] = n.phone_no
		data['milege'] = i.milege
		data['location'] = i.Location
		f = i.features
		f1,f2,f3 = [],[],[]
		temp = 0;
		for d in f.split(","):
			if(temp == 3):temp = 0
			if(temp == 0):f1.append({"feat" : d})
			if(temp == 1):f2.append({"feat" : d})
			if(temp == 2):f3.append({"feat" : d})
			temp += 1
		data['f1'] = f1;data['f2'] = f2;data['f3'] = f3
		data['type'] = i.body_type
		data['trans'] = i.transmission
		data['fuel'] = i.fuel
	return render(request,"oldcar.html",data)