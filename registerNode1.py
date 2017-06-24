import os
import json


#load environmentVersion.json

with open('environmentVersion.json') as config:
	data= json.load(config)

sssVersion = data['selenium-server-standalone_version']

startServer = 'java -jar selenium-server-standalone-' + sssVersion +'.jar -role' 


#register node1 to port 5555
#registerNode1 = startServer + ' node -hub http://192.168.0.5:4444/grid/register/ -port 5555 -browser browswerName=chrome,maxInstance=5'
registerNode1 = startServer + ' node -hub http://192.168.0.5:4444/grid/register/ -port 5557'


os.system(registerNode1)