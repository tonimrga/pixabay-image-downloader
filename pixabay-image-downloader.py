import requests
from sys import exit
API_KEY = '5462540-1063e196ee3440ce8d9666483'

def get_images(search_term, num_of_images):
    URL = 'https://pixabay.com/api/'
    PARAMS = { 'q': search_term, 'key': API_KEY, 'per_page': num_of_images } 
    req = requests.get(url = URL, params = PARAMS)
    if req.status_code != 200:
        print('An error occured.')
        exit()
    return req.json()

def download_images(images):
    for image in images:
        url = image['largeImageURL']
        filename = url.split('/')[-1]
        r = requests.get(url, allow_redirects=True)
        print('Downloading image: ' + filename); 
        open(filename, 'wb').write(r.content)
    print('Images downloaded.')

search_term = input('Please enter a search term: ')
num_of_images = input('Please enter a number of images(3 - 200): ')

images = get_images(search_term, num_of_images)
if images['totalHits'] > 0:
    download_images(images['hits'])
else:
    print("No images found.")

