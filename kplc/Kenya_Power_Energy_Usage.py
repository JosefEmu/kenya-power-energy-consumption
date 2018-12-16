
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
