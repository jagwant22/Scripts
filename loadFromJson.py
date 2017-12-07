#!/usr/bin/python

import json
from django.contrib.auth.models import User
from navia_apis.models import UserProfile, Doctor


jsonData = []
with open('doctor_database.json') as jsonFile:
	for jsonDict in jsonFile:
		jsonData = json.loads(jsonData)


for patient in jsonData:
	# Create User 
	try:
		user_object = User(
				username = patient['mobile_number'],
				first_name = str(patient['first_name']), " " , str(patient['last_name']),
				password = 0007
			)
		user_object.save()
	except Exception as Err:
		print "error creating user -> model for "
		print patient
		print "error info : \n"
		print str(Err)
	
	# Create UserProfile
	user_profile_object = UserProfile(
			
		)

	# Link Patient to Doctor
