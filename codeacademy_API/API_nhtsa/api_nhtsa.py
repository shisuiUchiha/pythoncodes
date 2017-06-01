from json import *
from urllib2 import *

apiurl="http://www.nhtsa.gov/webapi/api/SafetyRatings"

#apiparam="/modelyear/2013/make/HONDA/model/ACCORD/"
apiparam="/VehicleId/7522"

apidataformat="?format=json"

response=urlopen(apiurl+apiparam+apidataformat)

json_obj=load(response)

print json_obj


for objectCollection in json_obj['Results']:
	# Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.iteritems():
        print safetyRatingAttribute, ": ", safetyRatingValue
        #exit()
    #exit()
