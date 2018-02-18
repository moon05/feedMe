from rest_framework import serializers
from models import Directory


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Directory

		fields = ("first_name", "last_name", "netid", "studentid", "dorm", "balance", "location")
	
