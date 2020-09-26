from django.shortcuts import render
from .models import Calculation

# Create your views here.
def calculator_in(request):
    return render (request, 'calculator/calculator_in.html')

def calculator_out(request):
	try:
		get_finish_sum = float(request.GET['present_value'])
		get_years = float(request.GET['time_in_years'])
		get_inf = float(request.GET['inflation'])
		get_profit = float(request.GET['profitability'])
		if get_years<300:
			fv = Calculation.future_value_of_money(get_finish_sum, get_years, get_inf)
			rp = Calculation.regular_payment(fv, get_years, get_profit)
			oa = Calculation.investment_in_one_amount(fv, get_years, get_profit)
			lf = Calculation.language_feature_year(get_years)
			calculator_dictionary = {'future_value':fv, 'get_years':get_years, 'get_inf':get_inf, 
			'get_profit': get_profit, 'regular_payment': rp, 'investment_in_one_amount': oa, 
			'language_feature_year': lf}
			return render(request, 'calculator/calculator_out.html', calculator_dictionary)
		else:
			return render(request, 'calculator/calculator_error.html')
	except ValueError:
		return render(request, 'calculator/calculator_error.html')