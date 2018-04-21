import requests

r = requests.get('https://sc-hackathon.urbanpulse.de/UrbanPulseManagement/api/eventtypes', auth=('hackathon', 'L33333t+'))

print("r=", r)
print("#############################################")
print("content", r.content)