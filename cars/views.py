from django.shortcuts import render
from user_data.models import User_Account
from car_data.models import Car_data_new,Car_data_old
from blog.models import content
from django.http import HttpResponseRedirect


def home(request):
	data = {}
	data['infomessage'] = request.session.get('infomessage')
	data['open'] = request.session.get('open')
	data['errormessage'] = request.session.get('errormessage')
	user_id = request.session.get('id','')
	vericode = request.session.get('vericode','')
	if(user_id != '' and vericode != ''):
		user = User_Account.objects.all().filter(user_id = user_id , vericode = vericode)
		for i in user:
			data['name'] = i.name  
	new_car = Car_data_new.objects.all().order_by('-hits')[0:10];
	new_first = []
	for i in new_car:
		link = "/car/view?type=new&id=" + str(i.car_id)
		new_first.append({"photo" : i.photolinks.split(",")[0] ,"url" : link, "name" : i.name , "milege" : i.milege , "price" : i.price})
	data['first'] = new_first

	blog = []
	for b in content.objects.all().order_by('-date')[0:3]:
		link = "/blog/blog?id=" + str(b.blog_id)
		blog.append({"photo" : b.photo.split(",")[0] , "content" : b.content[0:60] , "link" : link , "title" : b.title})
	data["blog"] = blog
	request.session.pop('infomessage','')
	request.session.pop('errormessage','')
	request.session.pop('open','')
	return render(request,'homep.html',data)

def about(request):
	return render(request,"about.html")

def contact(request):
	return render(request,"contact.html")
def red(request):
	return HttpResponseRedirect('/home')
