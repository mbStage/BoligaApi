import requests, os

def get_image(url, addr) :
    img_data = requests.get(url).content
    with open(addr, 'wb') as handler:
        handler.write(img_data)


images = [
    {'id': 2250068, 'date': '2025-08-08T08:05:52.000Z', 'url': 'https://i.boliga.org/dk/550x/2250/2250068.jpg'}
    , {'id': 1674805, 'date': '2020-09-06T22:00:00.000Z', 'url': 'https://i.boliga.org/dk/550x/1674/1674805.jpg'}]

street = 'Faldskærmsvej 43, Jonstrup'
os.mkdir(f'./images/{street}')

for image in images :
    addr = f'./images/{street}/{image['id']}.jpg'
    url = image['url']

    get_image(url, addr)
    


