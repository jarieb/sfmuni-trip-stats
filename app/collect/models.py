from django.db import models

# Create your models here.

class Route(models.Model):
	rid = models.CharField(max_length=10, db_index=True, verbose_name="ID", unique=True)
	title = models.CharField(max_length=100, db_index=True, verbose_name="Title", unique=True)

	def __str__(self):
		return str(self.rid) + u' - ' + str(self.title)

class Trip(models.Model):
	ip_address = models.CharField(max_length=16, db_index=True, verbose_name="IP Address")
	route = models.ForeignKey('Route', null=True, blank=True, on_delete=models.CASCADE)
	start_datetime = models.DateTimeField('Start of Trip Time')
	end_datetime = models.DateTimeField('End of Trip Time')
	start_lat = models.DecimalField(default=0,max_digits=11,decimal_places=7)
	start_lon = models.DecimalField(default=0,max_digits=11,decimal_places=7)
	end_lat = models.DecimalField(default=0,max_digits=11,decimal_places=7)
	end_lon = models.DecimalField(default=0,max_digits=11,decimal_places=7)

	def __str__(self):
		return str(self.ip_address) + u' - ' + str(self.route)

class Observation(models.Model):
	trip = models.ForeignKey('Trip', null=True, blank=True, on_delete=models.CASCADE)
	datetime = models.DateTimeField('Observation datetime')
	bid = models.CharField(max_length=16, verbose_name="Bus ID")
	secsSinceReport = models.IntegerField(default=0)
	lat = models.DecimalField(default=0,max_digits=11,decimal_places=7)
	lon = models.DecimalField(default=0,max_digits=11,decimal_places=7)
	kph = models.IntegerField(default=0)
	heading = models.IntegerField(default=0)

	def __str__(self):
		return 'Observation ' + str(self.pk) + u' for ' + str(self.trip.ip_address)