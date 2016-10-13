from django.shortcuts import render

def home(request):
	return render(request,'homep.html',{ "infomessage" : "Please Verify Your Account to Continue"})