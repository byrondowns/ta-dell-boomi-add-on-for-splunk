'''
Python 3.7
Post request to Dell Boomi instance to pause all listeners
'''

import requests

# pull variables out of config for modularity
API_TOKEN = $atomsphere_apiToken$
ACCOUNT_ID = $atomsphere_accountID$
CONTAINER_ID = $atomsphere_containerId$
#LISTENER_ID = $atomsphere_listenerId$		# required to pause single listener


url = f"https://api.boomi.com/api/rest/v1/{ACCOUNT_ID}/changeListenerStatus"

# AtomSphere API token or user name and password required for authentication
auth = f"BOOMI_TOKEN.{ACCOUNT_ID}:{API_TOKEN}"


header = 
	{
		"Content-Type": "application/json"		# use JSON-formatted request bodies 
		#"Accept": "application/JSON"			# receive JSON-formatted responses
	}

# do not specify listenerId param to pause all
payload =
	{
		#"listenerId" :  LISTENER_ID	# required to pause single listener
		"containerId" : CONTAINER_ID,
		"action" : "pause_all" 			# options: pause, resume, restart, pause_all, resume_all, or restart_all.
	}


# POST REQUEST
response = requests.post(url, json=payload, headers=header, auth=auth)


# check if request successful
# returns empty changeListenerStatusResponse if success
if (!response):
	print("Request successful: Dell Boomi listeners have been paused")

else:
	print("Request failed: " + str(response))


