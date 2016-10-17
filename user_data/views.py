from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from models import User_Account
from django.db.models import Max
from django.http import HttpResponseRedirect
from car_data.models import Car_data_new,Car_data_old, Varient_data
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import datetime
import time 
import hashlib



def req(request):
		request.session['infomessage'] = "Please Login Here"
		request.session['open'] = 'login'
		request.session['redirect'] = request.META['HTTP_REFERER']
		return HttpResponseRedirect("/home")
def reg(request):
		request.session['open'] = 'register'
		request.session['redirect'] = request.META['HTTP_REFERER']
		return HttpResponseRedirect("/home")
def login(request):
	email =  request.POST.get("email","")
	password = hashlib.sha256(bytes(request.POST.get('password',''))).hexdigest() #hash function
	user_data = User_Account.objects.all().filter(email = email)
	got = True
	for e in user_data:
		got = False
	if(got):
		request.session['errormessage'] = "Email Id Does not Exist Please Signup"
		request.session['open'] = 'login'
		return HttpResponseRedirect("/home")
	_id = 0
	_ver = 0
	for e in user_data:
		_ver = e.verified
		_id = e.user_id
		vericode = e.vericode
		if(e.password != password):
			request.session['errormessage'] = "Password/Emailid entered is wrong please Try again"
			request.session['open'] = 'login'
			return HttpResponseRedirect("/home")
	if(_ver == 0):
		request.session['errormessage'] = "Please Verify Email Adress To Continue"
		request.session['open'] = 'login'
		return HttpResponseRedirect("/home")
	request.session['id'] = _id  
	request.session['vericode'] = vericode
	url = request.session.get('redirect','')
	request.session['redirect'] = ''
	if(url == ''):return HttpResponseRedirect('/home')
	return HttpResponseRedirect(url)

def signup(request):
	password = hashlib.sha256(bytes(request.POST.get('password',''))).hexdigest() #Hasing Password For Better Security
	name = request.POST.get('name','')
	name = name[0].upper() + name[1:] #for capitalizing first letter
	phone = request.POST.get('phone_number','')
	email = request.POST.get('email','')
	vericode = '000000'
	verified = '0'	
	data = User_Account.objects.all().order_by('-user_id')
	email_check = User_Account.objects.all().filter(email = email)
	for y in email_check :
		request.session['infomessage'] = "Email Exists on Server. Please Login With your Existing Account"
		request.session['open'] = 'login'
		return HttpResponseRedirect("/home")
	val = 0
	for i in data:
		if(i.user_id > val):val = i.user_id;break
	new_user_id =  val +  1
	vericode = ''.join(random.choice('0123456789ABCDEF') for i in range(16)) #This creates a random String of letters Used for Unique Identity
	verilink = "zencars.herokuapp.com/auth/verified?id=" + str(new_user_id) + "&veri=" + vericode
	print verilink
	outer = MIMEMultipart('alternative')
	outer['Subject'] = "Verify Account For ZenCars"
	outer['To'] = email
	outer['From'] = 'cygnus@cecsummit.org'
	message = """
			<h2>Hello {},</h2> 
				<h3>This is a Verification Message</h3>
				<p>Please enter the Verification code in the registration process or enter the key after logging in with
				the provided username and password</p>
				<h3>Please Do Keep this message and the verification code for further use</h3>
				<br>	
				<a href = "{}">Click Here To Continue Login process </a>
				<br>
				<p>If the above link is not working please enter the Verification Code Manually</p>
				<br>
				<h3>The verification code is  {}</h3>
					<h4>Team ZenCars</h4>
					<br>
					 DO not Reply To this message 
				""".format(name,verilink,vericode)
	HTML_BODY = MIMEText(message,'html')
	outer.attach(HTML_BODY)
	try:
		server = smtplib.SMTP_SSL('terminal1.veeblehosting.com',465)
		server.login('interstellar@cecsummit.org','interstellar123@')
		server.sendmail('cygnus@cecsummit.org', email,outer.as_string())
		server.quit()
		print "Sent Email"
	except Exception, e:
		print e
	p = User_Account(email = email,password=password,user_id=new_user_id,name=name,phone_no=phone,vericode=vericode,verified=0)
	p.save()
	request.session['infomessage'] = "Please Verify Your Account to Continue"
	request.session['open'] = 'login'
	return HttpResponseRedirect("/home")

def verified(request):
	id = request.GET.get('id')
	vericode = request.GET.get('veri')
	dat = User_Account.objects.all().filter(user_id = id)
	for e in dat:
		if(str(e.vericode) == str(vericode)):
			User_Account.objects.filter(user_id = id).update(verified = 1)
			request.session['infomessage'] = "Account Verified. Login To Continue"
			request.session['open'] = 'login'
			return HttpResponseRedirect("/home")
	return HttpResponseRedirect("/home")

def change(request):
	email = request.POST.get('email','')
	veri = request.POST.get('vericode','')
	new_pass = hashlib.sha256(bytes(request.POST.get('password',''))).hexdigest()
	acc = User_Account.objects.all().filter(email = email)
	for i in acc:
		vericode = i.vericode
	if(vericode == veri):
		User_Account.objects.all().filter(email = email).update(password = new_pass)
	else:
		request.session['errormessage'] = "Wrong Information Provided"
		request.session['open'] = 'forgot'
		return HttpResponseRedirect("/home")
	request.session['infomessage'] = "Password Changed. Log in With your New Acocunt"
	request.session['open'] = 'login'
	return HttpResponseRedirect("/home")

def sendveri(request):
	email = request.GET.get('email','')
	user = User_Account.objects.all().filter(email = email)
	test = True
	for i in user:
		name = i.name
		vericode = i.vericode
		test = False
	if(test):
			return render(request,"forpass.html",{'sendmessage' : "This Email Does not Exist in our Database"})
	outer = MIMEMultipart('alternative')
	outer['Subject'] = "Verify Account For Interstellar"
	outer['To'] = email
	outer['From'] = 'cygnus@cecsummit.org'
	message = """
			<h2>Hello {},</h2> 
				<h3>This is a Verification Message</h3>
				<p>Please enter the Verification code in the registration process or enter the key after logging in with
				the provided username and password</p>
				<h3>Please Do Keep this message and the verification code for further use</h3>
				<br>	
				<h3>The verification code is  {}</h3>

					<h4>Cygnus Team :)</h4>
					<br>
					 DO not Reply To this message 
				""".format(name,vericode)
	HTML_BODY = MIMEText(message,'html')
	outer.attach(HTML_BODY)
	try:
		server = smtplib.SMTP_SSL('terminal1.veeblehosting.com',465)
		server.login('interstellar@cecsummit.org','interstellar123@')
		server.sendmail('cygnus@cecsummit.org', email,outer.as_string())
		server.quit()
		print "Sent Email"
	except Exception, e:
		print e
		return render(request,"forpass.html",{'sendmessage' : "Invalid Email Address or Try again Later"})
	return render(request,"forpass.html",{'sendmessage' : "Verification Code Sent"})

def logout(request):
	request.session['id'] = '' 
	request.session['vericode'] = ''
	return HttpResponseRedirect('/home')

def sold(request):
	Car_data_old.objects.all().filter(user_id = request.session['id'] , car_id= request.GET.get('car_id',-1)).update(status = 'sold')
	return HttpResponseRedirect("/auth/view?type=sell")

def delete(request):
	Car_data_old.objects.all().filter(user_id = request.session['id'] , car_id= request.GET.get('car_id',-1)).delete()
	return HttpResponseRedirect("/auth/view?type=sell")


def details(request):
	user_id = request.session['id']
	if(user_id == ''):return HttpResponseRedirect("/home")
	data = User_Account.objects.all().filter(user_id = user_id)	
	car = Car_data_old.objects.all().filter(user_id = user_id)
	dat = {}
	sell = 0
	sold = 0
	sell_l= []
	sold_l = []
	for c in car:
		if(c.status == 'sell'):sell+=1;sell_l.append({"name" : (c.brand  + " "  + c.name)})
		elif(c.status == 'sold'):sold+=1;sold_l.append({"name" : (c.brand  + " "  + c.name)})
	dat['sold'] = sold
	dat['sell'] = sell
	dat['sold_l'] = sold_l
	dat['sell_l'] = sell_l
	dat['total'] = sell + sold
	for i in data:
		dat['name'] = i.name
		dat['email'] = i.email
		dat['phone'] = i.phone_no
		dat['photo'] = i.photo
		dat['vericode'] = i.vericode
	return render(request,"userdet.html",dat)

def changephoto(request):
	return HttpResponseRedirect("/auth/details")

def view(request):
	try:
		user_id = request.session['id']
		if(user_id == '' ):return HttpResponseRedirect("/home")
	except:
		return HttpResponseRedirect("/home")
	if(request.GET.get("type",'') == 'sell'):
		data = Car_data_old.objects.all().filter(user_id = user_id , status = 'sell')
	else:
		data = Car_data_old.objects.all().filter(user_id = user_id , status = 'sold')
	o = []
	oldcar = {}
	for n in User_Account.objects.all().filter(user_id = user_id):
		user_name = n.name
	for i in data:
		oldcar['name'] = i.brand + " " + i.name
		if(i.general_information == None):i.general_information = ""
		oldcar['info'] = ' '.join(i.general_information.split("\n"))[:100]
		oldcar['det'] = "/car/view?type=old&id=" + str(i.car_id)
		oldcar['price'] = i.price
		oldcar['reading'] = i.reading
		oldcar['fuel'] = i.fuel
		oldcar['year'] = i.year
		oldcar['pic'] = i.photolinks
		oldcar['trans'] = i.transmission 
		oldcar['sold'] = "/auth/sold?car_id=" + str(i.car_id)
		oldcar['delete'] = "/auth/delete?car_id=" + str(i.car_id)
		o.append(oldcar)
		oldcar={}
	return render(request,"usercar.html",{"car" : o , "len" : len(o) , "name" : user_name})
