# download_xkcd.py - Dowloads some comics from the popular webcomic xkcd.com

'''
The main idea behind this script is to pull all of the comics and their respective author comments from xkcd.com
There are a a few issues with using this script as a general use case for ripping images and comics from any generic site:
	1) The while condition is specific to xkcd.com
	2) The html id's and tags used are site specific
	3) It's sloppy and my first time doing this
	4) It lacks any sort of elegance
	5) A deeper understanding of html parsing and archeteture is required for further webpage scrapping
'''




import requests, os, bs4

url = 'https://xkcd.com'
# the below syntax is valid in py3, sublime interprets it as an error because it uses py2
os.makedirs('xkcd/comments', exist_ok=True) # stores the comics in ./xkcd

# this condition only works for xkcd
# meaning this while loop cannot be extrapolated in a generic manner
while not url.endswith('#'):
	# Download the page
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	#find the url of the comic image
	# find the img file inside of the comic id
	comic_elem = soup.select('#comic img')


	if comic_elem == []:
		# no valid image element to pull
		print('Could not find comic image.')
	else:
		# url to the comic image
		comic_url = 'https:' + comic_elem[0].get('src')
		# the author comments displayed when the mouse hovers over the image
		comment = comic_elem[0].get('title')

		# Download the image
		print('Downloading image %s...' % (comic_url))
		res = requests.get(comic_url)
		res.raise_for_status()

		# Save the image to ./xkcd
		image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
		# Save the hover comments to ./xkcd/comments
		comments_file = open(os.path.join('xkcd/comments', os.path.basename(soup.select('#ctitle')[0].getText())), 'w')

		# using chunks and iter_content conserves memory when writing large files
		for chunk in res.iter_content(100000):
			image_file.write(chunk)
		image_file.close()

		# write the comment to the comment file in a folder
		comments_file.write(comment)
		comments_file.close()
	# get the prev button's url
	# the id is found by inspecting the element with dev tools
	previous_link = soup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + previous_link.get('href')
	break # removing this break will download every single xkcd comic!
	# you don't have the memory for this

print('Done!')
