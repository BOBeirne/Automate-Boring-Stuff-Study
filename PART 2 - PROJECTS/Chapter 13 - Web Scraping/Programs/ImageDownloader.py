# This program goes to image website and searches for a specified category and downloads the first 10 images.
# unfortunately im having problem getting this to work on imgur dues to the 429 error even with time pause (too many requests)
# flickr doesnt seem to work either due to use of dynamic yahoo user interface Id

import requests, os, bs4, time, random

search_term = input('Enter search term: ')
url = 'https://500px.com/search?q=/'
os.makedirs('downloaded_images', exist_ok=True) # store images in cwd ./downloaded_images, check if folder already exists and if it does just continue instead of throwing an error
img_tags = []

try:
    response = requests.get(url + search_term) 
    response.raise_for_status() 
except requests.exceptions.RequestException as errormsg:
    print(f"Error accessing search page: {errormsg}")
    exit()

soup = bs4.BeautifulSoup(response.text, 'html.parser') # create a BeautifulSoup object with the search results page as a string
img_tags = soup.select('img[data-src]') # find all <img> elements with data-src attribute

num_downloaded = 0 # initialize counter

# Loop through the found tags and download each image found

for image in img_tags[0:10]: # for each image in the list
    image_url = 'https:' + str((image.get('data-src') or ''))
    print(f'Downloading image {image_url}...')

    try:
        response_img = requests.get(image_url) # download the image and store it in 'response_img'
        response_img.raise_for_status() # check for any issues downloading
    except requests.exceptions.RequestException as errormsg:
        print(f"Error downloading image: {errormsg}")
        continue # skip to the next image


    img_filename = os.path.basename(image_url).split('?')[0] # get the filename from the url and remove the query string
    file_path = os.path.join('downloaded_images', img_filename) # create the file path

    with open(file_path, 'wb') as image_file:
        for chunk in response_img.iter_content(100000): # save the file in chunks of 100000 bytes
            image_file.write(chunk) # write each chunk to the file

    print(f'Downloaded image {img_filename} to {file_path}')
    num_downloaded += 1
    time.sleep(5) # wait 1 second before downloading the next image

print(f'Downloaded {num_downloaded} images')


# 500px WIP
# body > div:nth-child(15) > div.mainContent > div > div.bottom > rejectAll
#browser.find_element(By.ID, 'a.rejectAll').click() # reject all cookies
# #gwt-debug-close_id
#browser.find_element(By.ID, 'gwt-debug-close_id').click() # close window