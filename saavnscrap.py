from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_')
soup = BeautifulSoup(res.text, 'lxml')

data = soup.find('ol', {'class':'content-list'})
all_songs = data.find_all('div', {'class': 'details'})

for x in all_songs:
	songs = x.find('p', {'class': 'song-name'})
	print(songs.text)
