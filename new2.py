#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://dev98448.service-now.com/api/now/table/incident'
cmd
# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'wTh/h1-HKv2U'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data="{\"description\": \"money deducted\",\"short_description\": \"ticket creation testing from service now api\"}")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
