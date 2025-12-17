import requests  # <-- ESTA LÍNEA ES FUNDAMENTAL

r = requests.get("https://httpbin.org/get")
print(r.status_code)
print(r.json())