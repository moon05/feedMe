from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Directory
from feedMe.serializers import StudentSerializer
import json
from django.http import JsonResponse


MASTER_ORDER_LIST = {}


@api_view(['GET'])
#RECEIVES netid
#SENDS out a students all details
def login_check(request):
	try:
		if request.method == 'GET':
			# students = Directory.objects.get(email="amamun")
			rec_netid = request.data["netid"]
			# print request.data
			lookup_student = Directory.objects.filter(netid=rec_netid).first()
			#this is how it properly prints
			serializer = StudentSerializer(lookup_student)
			# print serializer.data
			print "Login Successful"
			return JsonResponse(serializer.data)
		except:
			return JsonResponse({"Response":400, "Data-Received": request.data})

@api_view(['GET'])
#RECIEVES netid
#SENDS out a students all details
def get_profile(request):
	if request.method == 'GET':
		try:
			rec_netid = request.data["netid"]
			lookup_student = Directory.objects.filter(netid=rec_netid).first()
			serializer = StudentSerializer(lookup_student)
			print "Get Profile Successful"
			
			return JsonResponse(serializer.data)
		except:
			return JsonResponse({"Response":400, "Data-Received": request.data})


@api_view(['POST'])
#RECEIVES netid, store_name, items_list, total_price, delivery_charge, delivery_location
def master_order(request):
	if request.method == 'POST':
		try:
			rec_data = request.data
			netid = rec_data["netid"]
			rec_data.pop("netid")
			MASTER_ORDER_LIST[netid] = rec_data
			print MASTER_ORDER_LIST
			print "Order received into Master Order Successfully"
			return JsonResponse({"Order_Received": True})
		except:
			return JsonResponse({"Response":400, "Data-Received": request.data})

@api_view(['POST'])
#RECEIVES only netid
def order_accepted(request):
	if request.method == 'POST':
		try:
			rec_data = request.data
			netid = rec_data["netid"]
			MASTER_ORDER_LIST.pop(netid)
			print MASTER_ORDER_LIST
			print "Order Accepted Successfully"
			return JsonResponse({"Order_Accepted": True})
		except:
			return JsonResponse({"Response":400, "Data-Received": request.data})

@api_view(['POST'])
#RECEIVES only netid
#SENDS first_name, last_name, item_list, store_name, delivery_location
def delivery_accept(request):
	if request.method == 'POST':
		try:
			rec_data = request.data
			rec_netid = rec_data['netid']
			print "HERE@^@!@!^@^!@^&^@!&@!"
			lookup_student = Directory.objects.filter(netid=rec_netid).first()
			print lookup_student
			outgoing_dict = {}
			outgoing_dict["first_name"] = lookup_student.first_name
			outgoing_dict["last_name"] = lookup_student.last_name
			temp_ord = MASTER_ORDER_LIST[rec_netid]
			outgoing_dict["items_list"] = temp_ord["items_list"]
			outgoing_dict["store_name"] = temp_ord["store_name"]
			outgoing_dict["delivery_location"] = temp_ord["delivery_location"]

			print "Delivery Accepted Successfully"

			return JsonResponse(outgoing_dict)

		except:
			return JsonResponse({"Response":400, "Data-Received": request.data})





