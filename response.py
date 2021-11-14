import requests
port = "9000"
url = "http://127.0.0.1:9000"

print(requests.post("http://127.0.0.1:9000", data=b'Hello Auriga').content)
print("Status code = ",requests.post(url).status_code)

print("GET response ",requests.request('get',url).content)
print("Status code = ",requests.get(url).status_code)

print("Put response ",requests.request('put',url).content)
print("Status code = ",requests.put(url).status_code)

print("DELETE response ",requests.request('delete',url).content)
print("Status code = ",requests.delete(url).status_code)