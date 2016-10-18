import pickle
import datetime
from car_data.models import Car_data_new

car_type=pickle.load(open("main_car_full_data.p","r"))

for i in car_type.keys():
	
	print car_type[i]['Car Name']
	print ','.join(car_type[i]['Car Images'])
	temp = []
	for s in car_type[i]['Car Features']:
		data = s + " " + ": HEADING"
		temp.append(data)
		for c in car_type[i]['Car Features'][s]:
			for k in c.keys():
				car = k + " : " + c[k] 
				temp.append(car)
	Car_data_new(name = car_type[i]['Car Name'] , photolinks = ','.join(car_type[i]['Car Images']) , videolinks = '' , price = car_type[i]['Car Price'] , milege = car_type[i]['Car Mileage'] , body_type = car_type[i]['Car Type'] , specifications = ",".join(temp) , general_information = car_type[i]['Car Review'] ,dealer_number = "9562854642", dealer_email = "CarDealer@Zencars.com" , hits = 0 ,date = datetime.datetime.now()).save()	

'''
class Car_data_new(models.Model):
	car_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 100) # Name of the Car
	photolinks = models.CharField(max_length=1000)
	videolinks = models.CharField(max_length=100)
	price = models.CharField(max_length = 50) # its a charecter because its a range of values most commonly :)
	milege = models.CharField(max_length=10) # Vehicle Milege ** Seperatly Stored For Easy Acess
	body_type = models.CharField(max_length=20) #Sedan ,Suv ,Muv Etc ..
	specifications = models.TextField()
	general_information = models.TextField()
	dealer_number = models.IntegerField()
	dealer_email = models.CharField(max_length=100)
	hits = models.IntegerField() # Count Number of People Viewed this car
	date = models.DateTimeField() # Model Introduction Time
'''