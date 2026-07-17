import re
url = input("url: ")
if modified := re.search(r".+(?:\..+)?@.+\.(edu|com)", url, re.IGNORECASE ):
    print("valid")
else:
    print("invalid")
