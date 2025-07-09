import requests
from absl.testing.parameterized import parameters
from datetime import datetime
#
# response=requests.get(url="https://api.kanye.rest")
# response.raise_for_status()
# print(response.status_code)
#
# data=response.json()
# print(data)
#
# # longitude=data["iss_position"]["longitude"]
# # latitude=data["iss_position"]["latitude"]
# #
# # position=(longitude,latitude)
# # print(position)


parameter={
    "lat":51.503399,
    "lng":-0.119519,
    "formatted":0
}
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
response.raise_for_status()
data=response.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now=datetime.now()
print(time_now.hour)