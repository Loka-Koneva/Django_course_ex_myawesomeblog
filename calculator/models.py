from django.db import models

# Create your models here.
class Calculation (models.Model):
	def future_value_of_money(present_value, time_in_years, inflation_per):
		inflation = inflation_per/100
		future_value = present_value * ((1+inflation)**time_in_years)
		return round(future_value, 2)

	def regular_payment(future_value, time_in_years, profitability_per):
		profitability = profitability_per/100
		regular_per_year = future_value/((((1+profitability)**time_in_years)-1)/profitability)
		regular_per_month = regular_per_year/12
		return round(regular_per_month, 2)


	def investment_in_one_amount(future_value, time_in_years, profitability_per):
			profitability = profitability_per/100
			present_value = future_value/((1+profitability)**time_in_years)
			return round(present_value, 2)

	def language_feature_year(time_in_years):
		last_figure = time_in_years % 10
		if last_figure==1 and time_in_years!=11 and time_in_years!=111:
		    year = "год"
		elif 2<=last_figure<= 4 and time_in_years!=12 and time_in_years!=13 and time_in_years!=14:
			year = "года"
		else:
			year = "лет"
		return year