from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import content,comment
# Create your views here.

def blog(request):

	return render(request,"blog.html")

def list(request):
	data = {}
	blog = []
	category = request.GET.get('category','nil')
	print category
	if category == 'nil':return HttpResponseRedirect("/home")
	for i in content.objects.all().filter(category = category):
		comm = 0
		for c in comment.objects.all().filter(blog_id = i.blog_id):
			comm+=1
		pic = []
		temp = 0
		for img in i.photo.split(","):
			pic.append({"link" : img , "ind" : temp});temp+=1
		link = "/blog/blog?id=" + str(i.blog_id)
		blog.append({"link" : link , "title" : i.title , "photo" : pic , 'count' : comm , 'author' : i.author , 'date' : i.date.date() , 'content' : (''.join(i.content.split("\n")))[:150] , "category" : category  } )
	data['blog'] = blog
	return render(request,"bloglist.html",data)

def comm(request):
	return 0 ;