# Download some sample PSG VGM files to create input samples.

import requests
import re
import os
from urllib.parse import urljoin

# URL to crawl
base_url = "https://download.file-hunter.com/Music/VGM/"

# Retrieve the page

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}
response = requests.get(base_url, headers=headers)

if response.status_code != 200:
    print(f"Error: Unable to retrieve the page (status code {response.status_code}).")
    exit()

# Use regex to find all href attributes that end with .zip
zip_links = re.findall(r'"([^"]+\.zip)"', response.text)
print(f"Found {len(zip_links)} zip files.")

# Loop over each zip link and download the file
for link in zip_links:
    # Create an absolute URL
    zip_url = urljoin(base_url, link)
    print(f"Downloading: {zip_url}")
    
    # Request the zip file
    zip_response = requests.get(zip_url, headers=headers)
    if zip_response.status_code == 200:
        # Extract the filename from the URL
        filename = os.path.basename(link)
        with open(filename, 'wb') as f:
            f.write(zip_response.content)
        print(f"Saved {filename}")
    else:
        print(f"Failed to download {zip_url}")

