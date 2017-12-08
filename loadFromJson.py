#!/usr/bin/python

import json
from django.contrib.auth.models import User
from navia_apis.models import UserProfile, Doctor

linkWith = "doctor_number"

uhid_dictionary = {
	"uhid":"",
	"doctor_number" : linkWith,
	"partner" : "INDIVIDUAL"
}

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

	# Add UHID
	uhid_dictionary["uhid"] = patient['patient_number'] 

	# Handle DOB
	dob = cleanDOB(patient["dob"])

	# Create UserProfile
	user_profile_object = UserProfile(
			user = user_object,
			linked_doctors = json.dumps([]),
			uhids = json.dumps([uhid_dictionary]),
			device_id = 0007,
			gender = patient['gender'],
			dob = dob

		)

	user_profile_object.save()

	# Link Patient to Doctor

	try:
		doc_object = Doctor.objects.get(phone = linkWith)
		linked_members = json.loads(doc_object.linked_patients)
		linked_members.append(patient['mobile_number'])
		doc_object.linked_patients = json.dumps(linked_members)
		doc_object.save()
	except Exception as Error:
		print "Error linking patients ::: to doctor"
		print Error
		print "Error in patient :",
		print patient




def cleanDOB(dob):
	try:
		split_dob = dob.split("-")
		returnDob = ""
		if len(split_dob[0]) == 4 :
			returnDob = split_dob[0] + "-" + split_dob[1] + "-" + split_dob[2]

		else :
			returnDob = split_dob[2] + "-" + split_dob[1] + "-" + split_dob[0]
	except:
		returnDob = "1990-01-01"

	return returnDob


