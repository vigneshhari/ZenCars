from django.shortcuts import render

# Create your views here.

# Fields in Car_Details ... General Information/Review --> Features/Specs --> User Reviews --> Estimated Fuel Cost --> Gallery

def search(request):
	lis = []
	lis.append({"test":"test"})
	lis.append({"test":"test"})
	return render(request,"listv.html",{'cardata' : lis , 'resultlen' : len(lis)})