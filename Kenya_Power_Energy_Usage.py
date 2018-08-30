#!/usr/bin/env python
import datetime
month_names= {
"1": "January",
"2" : "February",
"3" : "March",
"4" : "April",
"5" : "May",
"6" : "June",
"7" : "July",
"8" : "August",
"9" : "September",
"10" : "October",
"11" : "November",
"12" : "December"}
class MonthlyEnergyConsumption:
	"""Main use: The program calculates the daily average energy consumption.
	Other uses: Outputs to a text file; added token, current meter reading, total amount spent on energy tokens, and finally the average daily consumption.
	Required parameters: meter reading as float, start date in format YYYYMMDD."""

	amount_spent= 0 #Assumes the beginning of expense tracking
	
	def __init__(self, meter_reading, start_date):
		self.meter_reading= meter_reading 
		self.start_date= start_date

	def add_tokens(self, token_units, amount):
		"""Cumulatively adds token units and amount to your initial variables."""
		self.meter_reading+=token_units
		self.amount_spent+=amount	
		with open("kplc_data_dump.txt", "a") as f:
			print(datetime.date.today(), file=f)
			print(f"Added {token_units} units, \nTotal amount spent is Kes. {self.amount_spent}.\
				\nTotal units are {round(self.meter_reading)} units.\
				\n\n--------------------------------", file=f)
		return "Total amount spent: Kes." + str(self.amount_spent)

	def daily_usage_month(self, current_reading):
		"""Calculates the average usage on a daily basis plus creates required variables."""
		units_consumed= self.meter_reading- current_reading
		today= datetime.date.today()
		y= int(self.start_date[:4])
		m= int(self.start_date[4:6])
		d= int(self.start_date[6:])
		start_date_formatted=datetime.date(y,m,d)
		total_days= (today- start_date_formatted).days
		avg_daily_usage= format((units_consumed/total_days), ".3f")
		with open("kplc_data_dump.txt", "a") as f:
			print(datetime.date.today(), file=f)
			print(f"#############################################\n*****Average Daily Usage is {avg_daily_usage} units.*****\n#############################################\n\n\n", file=f)
		units= format(float(units_consumed), ".2f")
		return f"For the month of {month_names[str(today.month)]}, you have consumed {units} units averaging to about {avg_daily_usage}."
		 
august= MonthlyEnergyConsumption(4.6, "20180801")
august.add_tokens(4.6,100)
august.add_tokens(4.6,100)
august.add_tokens(4.6,100)
august.add_tokens(13.6,300)
august.add_tokens(2.25,50)
august.add_tokens(4.51,100)
august.add_tokens(4.51,100)
august.add_tokens(2.25,50)
august.add_tokens(4.51,100)
august.add_tokens(4.51,100)
august.add_tokens(2.48,55)
august.add_tokens(2.25,50)
august.add_tokens(0.99,22)
august.add_tokens(3.52,78)
august.add_tokens(4.51,100)
print(august.daily_usage_month(6.72))
