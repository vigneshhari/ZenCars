from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import content,comment
from user_data.models import User_Account
import datetime

# Create your views here.

def blog(request):
	blog = {}
	id = request.GET.get('id','')
	if(id == ''):return HttpResponseRedirect('/home')
	data = content.objects.all().filter(blog_id=id)
	user_id = request.session.get('id','')
	if(user_id == ''):user_id = -1
	pic = []
	temp = 0;
	for i in data:
		for img in i.photo.split(","):
			pic.append({"link" : img , "ind" : temp});temp+=1
		blog['title'] = i.title
		blog['photo'] = pic
		blog['author'] = i.author
		blog['date'] = i.date.date()
		blog['content'] = i.content
		blog['category'] = i.category
	review = comment.objects.all().filter(blog_id = id )
	re = []
	for r in review:
		for jj in User_Account.objects.all().filter(user_id = r.user_id):
			re.append({'name' : jj.name , 'content' : r.content ,'photo' : jj.photo})
	blog['rev'] = re
	blog['user_id'] = user_id
	for u in User_Account.objects.all().filter(user_id = user_id):
		blog['username'] = u.name 
	blog['revlen'] = len(re)
	blog['blog_id'] = id
	return render(request,"blog.html" , blog)

def list(request):
	data = {}
	blog = []
	temp = 0
	user_id = request.session.get('id',-1)
	if(user_id != ''):
		for n in User_Account.objects.all().filter(user_id = user_id):
			data['name'] = n.name
	if(request.GET.get('search','') != ''):
		for i in content.objects.all().filter(title__contains = request.GET.get('search')):
			comm = 0
			for c in comment.objects.all().filter(blog_id = i.blog_id):
				comm+=1
			pic = []
			for img in i.photo.split(","):
				pic.append({"link" : img , "ind" : temp});temp+=1
			link = "/blog/blog?id=" + str(i.blog_id)
			blog.append({"link" : link , "title" : i.title , "photo" : pic , 'count' : comm , 'author' : i.author , 'date' : i.date.date() , 'content' : (''.join(i.content.split("\n")))[:150] , "category" : i.category  } )
		data['blog'] = blog
		data['len'] = len(blog)
	else:
		category = request.GET.get('category','nil')
		print category
		if category == 'nil':return HttpResponseRedirect("/home")
		for i in content.objects.all().filter(category = category):
			comm = 0
			for c in comment.objects.all().filter(blog_id = i.blog_id):
				comm+=1
			pic = []
			for img in i.photo.split(","):
				pic.append({"link" : img , "ind" : temp});temp+=1
			link = "/blog/blog?id=" + str(i.blog_id)
			blog.append({"link" : link ,"id" : i.blog_id, "title" : i.title , "photo" : pic , 'count' : comm , 'author' : i.author , 'date' : i.date.date() , 'content' : (''.join(i.content.split("\n")))[:150] , "category" : category  } )
		data['blog'] = blog
	return render(request,"bloglist.html",data)

def comm(request):
	comment(blog_id = request.POST.get('id','') , user_id = request.POST.get('user','') , content = request.POST.get('text') ,date = datetime.datetime.now() ).save()
	return HttpResponseRedirect(request.META['HTTP_REFERER'])