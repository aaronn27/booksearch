import requests

bookname = input()
querybook = bookname.lower()
querybook = querybook.replace(' ','+')

resp = requests.get("http://openlibrary.org/search.json?title=to+kill+a+mockingbird")
info = resp.json()
authorname = info['docs'][0]['author_name'][0]
publishyear = info['docs'][0]['first_publish_year']

print(f"Author of '{bookname}'is '{authorname}'. It was first published in {publishyear}")