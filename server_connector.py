import requests
port = 9500
url = "http://127.0.0.1:9500"

print(requests.post(url, data=b'Hello Auriga').content)
# r=requests.get('http://127.0.0.1:9000')
# print(r.status_code)
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r1=requests.get(url+":"+port, params=payload)
# print(r1.url)
# print("Response Content---",r.text)
# print("Binary Response Content---",r.content)
# print("Raw Response Content---",r.raw)
# #print("JSON Response Content---",r1.json())
# # with open(filename, 'wb') as fd:
# #     for chunk in r.iter_content(chunk_size=128):
# #         fd.write(chunk)
# url = 'http://127.0.0.1:9000'
# headers = {'user-agent': 'my-app/0.0.1'}
# print("Custom Headers", requests.get(url, headers=headers))
# print(requests.post('http://127.0.0.1:9000', params=payload).text)

