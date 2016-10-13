from django.shortcuts import render
from user_data.models import User_Account

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
	request.session.pop('infomessage','')
	request.session.pop('errormessage','')
	request.session.pop('open','')
	return render(request,'homep.html',data)
