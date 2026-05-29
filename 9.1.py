import requests

response = requests.get("https://httpbin.org/get")
print(response.content)
print(type(response.content))
print(response.text)
print(type(response.text))

response = requests.post(
    "https://httpbin.org/post",
    data="Test Data",
    headers={"h1": "Test Title"},
)

print(response.text)


response = requests.post(
    "https://httpbin.org/post",
    data={"name": "Mia", "topic": "Python"},
)
print(response.text)