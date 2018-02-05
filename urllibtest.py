from urllib import request

page = request.urlopen("http://www.google.com")
for line in page:
    print(line)
response = page.getcode()

print("Status Code:" + str(response))
