import requests

# Replace YOUR_API_KEY and coordinates with actual values
api_key = 'Your_API_Key'
start_coords = '52.3779,4.9003'
end_coords = '52.3792,4.9002'

url = f'https://api.tomtom.com/routing/1/calculateRoute/{start_coords}:{end_coords}/json?apikey={api_key}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    distance = data['routes'][0]['summary']['lengthInMeters']  # Distance in meters
    print(f'Distance between the points: {distance} meters')
else:
    print('Failed to retrieve distance information')
