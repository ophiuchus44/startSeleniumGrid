import json
import os

#load environmentVersion.json
with open('environmentVersion.json') as config:
	data= json.load(config)


sssVersion = data['selenium-server-standalone_version']

startServer = 'java -jar selenium-server-standalone-' + sssVersion +'.jar -role' 

#start the hub
startHub = startServer + ' hub -hubConfig grid_hub.json'
#startHub = startServer + ' webdriver -hub'

os.system(startHub)
