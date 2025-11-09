#Habit Tracker
import requests
from datetime import datetime

TOKEN =  "pixela_token123"
USERNAME = "atharvalotankar"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

#TODO 1: Create your account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#TODO 2: Create a Graph Definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#TODO 3: Get your graph:
#Link - https://pixe.la/v1/users/atharvalotankar/graphs/graph1.html

#TODO 4: Post Value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?: ")
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

#TODO 5: Update and delete a pixel

#UPDATE
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

#DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

