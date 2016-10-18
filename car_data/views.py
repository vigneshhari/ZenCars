from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import DocumentForm
from django.http import JsonResponse
from .models import Car_data_new,Car_data_old, Varient_data , Car_review
from user_data.models import User_Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

# Fields in Car_Details ... General Information/Review --> Features/Specs --> User Reviews --> Estimated Fuel Cost --> Gallery

def search(request):
	oldcar,newcar = {},{}
	new = Car_data_new.objects.all()
	old = Car_data_old.objects.all().filter(status = 'sell' , confirmed = 1)
	if(str(request.GET.get('brand',"Any Make")) != "Any Make" ):
		print "Reached"
		new = new.filter(name__contains = request.GET.get('brand'))
		old = old.filter(brand__contains = request.GET.get('brand'))
		if(str(request.GET.get('model',"Any Model")) != "Any Model"):
			new = new.filter(name__contains =request.GET.get('model'))
			old = old.filter(name__contains =request.GET.get('model'))
	if(request.GET.get('type','Any') != "Any"):
		new = new.filter(body_type__iexact = request.GET.get('type'))
		old = old.filter(body_type__iexact = request.GET.get('type'))
	if(request.GET.get('status',"Any") != "Any"):
		if(request.GET.get('status') == "New"):old =[]
		if(request.GET.get('status') == "Used"):new =[]
	if(request.GET.get('min','') != '' or request.GET.get('max','') != ''):
		new = new.filter(price__gte = (int(request.GET.get('min')) * 100000) , price__lte = ((int(request.GET.get('max')) - 20)) * 100000)
		old = old.filter(price__gte = (int(request.GET.get('min')) * 100000) , price__lte = ((int(request.GET.get('max')) - 20)) * 100000)
		
	n = []
	for j in new:
		newcar['car'] = 'new'
		newcar['name'] = j.name
		newcar['milege'] = j.milege
		newcar['info'] = ' '.join(j.general_information.split("\n"))[:100]
		newcar['det'] = "/car/view?type=new&id=" + str(j.car_id)
		newcar['price'] = j.price
		newcar['pic'] = j.photolinks.split(",")[0]
		n.append(newcar)
		newcar={}
	for i in old:
		oldcar['car'] = 'old'
		oldcar['name'] = i.brand + " " + i.name
		oldcar['info'] = ' '.join(i.general_information.split("\n"))[:100]
		oldcar['det'] = "/car/view?type=old&id=" + str(i.car_id)
		oldcar['price'] = i.price
		oldcar['reading'] = i.reading
		oldcar['fuel'] = i.fuel
		oldcar['year'] = i.year
		oldcar['pic'] = i.photolinks
		oldcar['trans'] = i.transmission 
		n.append(oldcar)
		oldcar={}

	paginator = Paginator(n, 8)
	page = request.GET.get('page')
	try:
		car = paginator.page(page)
	except PageNotAnInteger:
		car = paginator.page(1)
	except EmptyPage:
		car = paginator.page(paginator.num_pages)
	return render(request,"listv.html",{"len" :(len(n)) , "car" : car})

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
			return HttpResponseRedirect(("car/view?type=old?id="+str(car_id)))
	return 0

def view(request):
	data = {}
	type = request.GET.get('type',False)
	id = request.GET.get('id',False)
	if(type == False or id == False):
		return HttpResponseRedirect("/home")
	user_id = request.session.get('id','')
	if(user_id ==''):user_id=-1
	data['user_id'] = user_id
	data['car_id'] = id
	user = User_Account.objects.all().filter(user_id = user_id)
	for i in user:
		data['username'] = i.name

	review = Car_review.objects.all().filter(car_id = id , car_type = type)
	re = []
	for r in review:
		for jj in User_Account.objects.all().filter(user_id = r.user_id):
			re.append({'name' : jj.name , 'content' : r.content ,'photo' : jj.photo})
	data['rev'] = re
	data['revlen'] = len(re)

	if(type == 'old'):
		data['status'] = 'old'
		details = Car_data_old.objects.all().filter(car_id = id)
		for i in details:
			data['brand'] = i.brand
			data['name'] = i.brand + " " + i.name
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
	elif(type == "var"):
		data['status'] = 'var'
		details = Varient_data.objects.all().filter(varient_id = id)
		for i in details:
			data['name'] = i.name
			data['price'] = i.price
			data['brand'] = i.main_car
			pic = i.photolinks
			picture,spec,feat = [],[],[]
			temp = 0
			for k in pic.split(","):
				picture.append({"link" : k ,'no' : temp})
				temp +=1
			data['picture'] = picture
			for j in i.specifications.split(","):
				if(len(j.split(":")) == 2):
					n,m = j.split(":")
					spec.append({'ind' : n  , 'val' :m})
			data['spec'] = spec
			data['info'] = i.general_information
			f = i.features
			f1,f2,f3 = [],[],[]
			temp = 0;
			for d in f.split(","):
				if(temp == 3):temp = 0
				if(temp == 0):f1.append({"feat" : d.split(":")[0]})
				if(temp == 1):f2.append({"feat" : d.split(":")[0]})
				if(temp == 2):f3.append({"feat" : d.split(":")[0]})
				temp += 1
			data['f1'] = f1;data['f2'] = f2;data['f3'] = f3
		return render(request,'varicar.html',data)
	elif(type == "new"):
		data['status'] = 'new'
		details = Varient_data.objects.all().filter(varient_id = id)
		for i in details:
			pic = i.photolinks
			picture,spec,feat = [],[],[]
			temp = 0
			for k in pic.split(","):
				picture.append({"link" : k ,'no' : temp})
				temp +=1
			data['picture'] = picture
			for j in i.specifications.split(","):
				if(len(j.split(":")) == 2):
					n,m = j.split(":")
					spec.append({'ind' : n  , 'val' :m})
			data['spec'] = spec
			data['info'] = i.general_information
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
		return render(request,'varicar.html',data)

def comm(request):
	Car_review(car_id = request.POST.get('car','') , user_id = request.POST.get('user','') , car_type = request.POST.get('type','') , content = request.POST.get('text') ,date = datetime.datetime.now() ).save()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])