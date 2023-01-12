import requests
from auth import *

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
    "id": "graph1",
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

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}"

pixel_config = {
    "date": "20230112",
    "quantity": "10",
    "optionalData": '{"title":"Prisipažįstu", "author":"Jaume Cabré"}'
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)