import requests
port = "9000"
url = "http://127.0.0.1:9000"


print("Get response ",requests.get(url, data=b'some GET1 payload').content)
#print("Status code = ",requests.get(url).status_code)

print("Post response ",requests.post(url, data=b' Post Data Hello Auriga').content)
print("Status code = ",requests.post(url).status_code)

print("Put response ",requests.put(url,data=b' Put data').content)
print("Status code = ",requests.put(url).status_code)

print("DELETE response ",requests.request('delete',url,data=b' Delete data').content)
print("Status code = ",requests.delete(url).status_code)