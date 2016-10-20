import cPickle as pickle
import datetime
from car_data.models import Car_data_new,Varient_data


a=pickle.load(open("variant_cars_data.p","rb"))

for type in a.keys():		#selecting car variant

	for vehicle_no in a[type].keys():	#selecting car using the number
		print vehicle_no
		spec = []
		feat = []
		for sf in a[type][vehicle_no]['Specs and Features']:	#each detail of a car
			for key in sf.keys():
				if(sf[key].strip() == "Yes"):
					fe = key + ":" + "Yes"
					feat.append(fe)
				else:
					sp= key + ":" + sf[key]
					spec.append(sp)
		car = Car_data_new.objects.all().filter(name = a[type][vehicle_no]['Main Car Name'])
		for i in car:
			photo = i.photolinks
			video = i.videolinks
			id =  i.car_id
		Varient_data(car_id = id ,milege = a[type][vehicle_no]['Mileage'] , name = a[type][vehicle_no]['Variant Car Name'] , photolinks = photo , videolink = video ,main_car = a[type][vehicle_no]['Main Car Name'] , price = a[type][vehicle_no]['Price'] , features = ','.join(feat) , body_type = type ,specifications =','.join(spec) ,general_information = a[type][vehicle_no]['Review'] ,hits = 0 ).save()
	




	
	
'''
['Mileage', 'Specs and Features', 'Review', 'Variant Car Name', 'Main Car Name', 'Price']


class Varient_data(models.Model):
	car_id = models.IntegerField()
	varient_id = models.AutoField(primary_key=True);
	name = models.CharField(max_length = 500)
	photolinks = models.TextField()
	videolink = models.CharField(max_length =100)
	main_car = models.CharField(max_length = 500)
	price = models.IntegerField()
	features = models.TextField()
	body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()
	hits = models.IntegerField(null=True) # Count Number of People Viewing Car 
'''