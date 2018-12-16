#!/usr/bin/env python
import datetime
class EnergyUsage:
	"""This tool helps you get the average daily energy consumption, total consumption and 
	the total amount spent on electricty (Kenya Power) for a given time interval."""
	def __init__(self,initial_meter_reading, initial_date):
		"""Requires the intial meter reading and an intial date in a YYYYMMDD string format."""
		self.initial_meter_reading = initial_meter_reading
		self.initial_date = initial_date
		self.total_units_consumed = 0
		self.total_amount_spent = 0

	def add_tokens(self, units, amount):
		"""Adds units and amount values."""
		self.total_units_consumed+= units
		self.total_amount_spent+= amount
		formatted_units= format(self.total_units_consumed, ".2f")
		print(f"\nAdded {units}.\nTotal units bought {formatted_units}")

	def monthly_usage(self, ending_date, ending_meter_reading):
		"""The last meter reading and an accompanying date is required."""
		yyyy= int(self.initial_date[:4])
		mm= int(self.initial_date[4:6])
		dd= int(self.initial_date[6:])
		starting_date_formatted = datetime.date(yyyy,mm,dd)

		yyyy= int(ending_date[:4])
		mm= int(ending_date[4:6])
		dd= int(ending_date[6:])
		ending_date_formatted = datetime.date(yyyy,mm,dd)


		number_of_days = (ending_date_formatted - starting_date_formatted).days
		units_consumed = self.total_units_consumed - ending_meter_reading
		average_daily_usage_calculation = units_consumed/ number_of_days
		average_daily_usage= format(average_daily_usage_calculation, ".2f")

		start= starting_date_formatted.strftime("%d,%B")
		end= ending_date_formatted.strftime("%d,%B")
		today = datetime.date.today().strftime("%d,%B,%Y")
		print(f"""
-------------------------------------------
Energy Usage Report as at {today}.
-------------------------------------------
Usage report for days between {start}
and {end}.
	
Average daily Usage = {average_daily_usage} kWh
Total units consumed = {format(units_consumed,".2f")} kWh
Total amount spent = KES{format(self.total_amount_spent, ",")}

-------------------------------------------
""")

#Test Data
# august= EnergyUsage(4.6, "20180801")
# august.add_tokens(4.6,100)
# august.add_tokens(4.6,100)
# august.add_tokens(4.6,100)
# august.add_tokens(13.6,300)
# august.add_tokens(2.25,50)
# august.add_tokens(4.51,100)
# august.add_tokens(4.51,100)
# august.add_tokens(2.25,50)
# august.add_tokens(4.51,100)
# august.add_tokens(4.51,100)
# august.add_tokens(2.48,55)
# august.add_tokens(2.25,50)
# august.add_tokens(0.99,22)
# august.add_tokens(3.52,78)
# august.add_tokens(4.51,100)
# august.monthly_usage("20180831",0)

# #print(august.monthly_usage(0.0)) #1.6 reading on the first

# #ending_date, ending_meter_reading

# september= EnergyUsage(0.0, "20180901")
# september.add_tokens(4.6, 100)
# september.add_tokens(4.6, 100)
# september.add_tokens(23, 500)
# september.add_tokens(9.2, 200) #26th Sept
# september.monthly_usage("20180930",0.0)

# october= EnergyUsage(0.0, "20181002")
# october.add_tokens(9.2, 200)
# october.add_tokens(13.8, 300)
# october.add_tokens(8.6, 188) #15th Oct.
# october.add_tokens(13.8, 300) #19th
# october.add_tokens(4.6, 100) #29th
# october.monthly_usage("20181031",4.66)

# november= EnergyUsage(0.0, "20181101")
# november.add_tokens(4.6, 100) #1st Nov.
# november.add_tokens(6.7, 100) #3rd Nov.
# november.add_tokens(6.7, 100) #7th Nov.
# november.add_tokens(6.6, 100) #12th Nov.
# november.add_tokens(6.6, 100) #15th Nov.
# november.add_tokens(13.2, 200)#19th Nov.
# november.add_tokens(6.6, 100)#27th Nov
# november.monthly_usage("20181130",0.0)

# december= EnergyUsage(0.0, "20181201")
# december.add_tokens(6.6, 100) #2nd 
# december.add_tokens(6.6, 100) #6th
# december.add_tokens(6.6, 100) #11th
# december.add_tokens(1.5, 22) #15th

# december.monthly_usage("20181216",1.62)
