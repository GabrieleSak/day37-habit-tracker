import requests
from auth import *
from datetime import datetime, timedelta

GRAPH_ID = "graph1"

# create user

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# create a graph

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    # "date": today.strftime("%Y%m%d"),
    "date": "20230109",
    "quantity": "44",
    "optionalData": '{"title":"Prisipažįstu", "author":"Jaume Cabré"}'
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# update data


pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/20230111"

new_pixel_data = {
    "quantity": "76",
    "optionalData": '{"title":"Prisipažįstu", "author":"Jaume Cabré"}'
}

# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete pixel


pixel_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/20230110"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
