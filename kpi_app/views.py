
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from kpi_app.models import User, Company
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def login_page(request):
	context_dict = {}
	return render(request, "kpi_app/login.html", context_dict)

def home(request):
	if request.user.is_authenticated():
		email = request.user.email
		try:
			user_obj = User.objects.get(email=email)
			if user_obj:
				context_dict = getData(user_obj)
				return render(request,"kpi_app/home.html", context_dict)
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
	else:
		return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')


def charts(request):
	if request.user.is_authenticated():
		email = request.user.email
		user_obj = User.objects.get(email=email)
		context_dict=getData(user_obj)
		try:
			if User.objects.get(email=email):
				return render(request,"kpi_app/charts.html",context_dict)
		except ObjectDoesNotExist:
			logout(request)
			return redirect('/')
	else:
		return redirect('/')


def getData(user_obj):
	company_obj = Company.objects.get(id=user_obj.company_name.id)
	context_dict = {'filter1': company_obj.filter1_dimValue, 'filter2': company_obj.filter2_dimValue,
					 'filter3': company_obj.filter3_dimValue, 'tab3': company_obj.tab3_name,
					  'tab4': company_obj.tab4_name}
	return context_dict
