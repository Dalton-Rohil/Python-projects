import requests

def shorten_url(url):
    tinyurl = "http://tinyurl.com/api-create.php?url="
    shortened_url = requests.get(tinyurl + url).text
    return shortened_url

original_url = "https://www.example.com/very/long/url"
short_url = shorten_url(original_url)
print(short_url)