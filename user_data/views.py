from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from models import User_Account
from django.db.models import Max
from django.http import HttpResponseRedirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import datetime
import time 





def login(request):
	email =  request.POST.get("email","")
	password = request.POST.get("password","")
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
	return HttpResponseRedirect('/home')

def signup(request):
	password = request.POST.get('password','')
	name = request.POST.get('name','')
	phone = request.POST.get('phone_number','')
	email = request.POST.get('email','')
	print password,name,phone,email
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
	vericode = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
	print vericode 
	'''
	outer = MIMEMultipart('alternative')
	outer['Subject'] = "Verify Account For Cygnus"
	outer['To'] = email
	outer['From'] = 'cygnus@cecsummit.org'
	verilink = "https://cygnusquiz.herokuapp.com/app/verified?id=" + str(new_user_id) + "&veri=" + vericode
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
					<h4>Cygnus Team :)</h4>
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
	'''
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
			request.session['logid'] = id
			request.session['vericode'] = vericode
			return render(request, 'login.html' , {'loginmessage' : "Account Verified Login To Continue"})
	return render(request,'verified.html',{'id' : id})

def change(request):
	email = request.GET.get('email','')
	veri = request.GET.get('veri','')
	new_pass = request.GET.get('pass','')
	if(len(new_pass) < 7):
		return render(request,"forpass.html",{'changemessage' : "Password should be longer than 7 charecters"})
	acc = User_Account.objects.all().filter(mail = email)
	for i in acc:
		vericode = i.vericode
		print vericode
	if(vericode == veri):
		User_Account.objects.all().filter(mail = email).update(password = new_pass)
	else:
		return render(request,"forpass.html",{'changemessage' : "Wrong Vericode"})
	return render(request, 'login.html' , {'loginmessage' : "Password Changed Please Login To Continue"})

def sendveri(request):
	email = request.GET.get('email','')
	user = User_Account.objects.all().filter(mail = email)
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

    
