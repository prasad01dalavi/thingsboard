import requests  # Import requests library to send requests to Thingworx

url = 'http://demo.thingsboard.io:80/api/v1/AZXWfYj6hVnwRHsohluH/telemetry'
# Specify the thingsboard url

headers = {
    'Content-Type': 'application/json'
}

# JSON data to upload on Thingworx
data = {"temperature": "30", "humidity": "16"}

response = requests.post(url, headers=headers, json=data)
print 'Response Code:', response.status_code
# If 200 then data has been uploaded successfully
