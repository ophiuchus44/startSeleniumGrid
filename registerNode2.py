import os
import json


#load environmentVersion.json

with open('environmentVersion.json') as config:
	data= json.load(config)

sssVersion = data['selenium-server-standalone_version']

startServer = 'java -jar selenium-server-standalone-' + sssVersion +'.jar -role' 


#register node2 to port 5556
#registerNode2 = startServer + ' node -hub http://192.168.0.5:4444/grid/register/ -port 5556 -browser browswerName=chrome,maxInstance=5'
registerNode2 = startServer + ' node -hub http://192.168.0.5:4444/grid/register/ -port 5556'

os.system(registerNode2)