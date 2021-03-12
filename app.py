import requests
from urllib.parse import urlencode
import sys


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({'url': url}))
    result = requests.get(request_url)
    return result.text

# print(make_tiny("http://harshcasper.hashnode.dev/polyglot-programming-with-metacall"))
