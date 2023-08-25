import os
import requests
import json

ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')  # Fetch the token from environment variable

def fetch_instagram_photos():
    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    media_urls = [item['media_url'] for item in data['data'] if item['media_type'] == 'IMAGE']
    return media_urls

def update_website_gallery(media_urls):
    # Assuming you have a simple gallery page with placeholders for images
    with open('gallery.html', 'r') as file:
        html_content = file.read()

    # Insert the images in the desired location
    new_content = ""
    for url in media_urls:
        new_content += f'<div class="instagram-image"><img src="{url}" alt="Instagram Photo"></div>\n'
    
    # Replace placeholder with the images' HTML
    html_content = html_content.replace("<!-- INSTAGRAM_PHOTOS -->", new_content)
    
    # Write the updated content back to the gallery.html
    with open('gallery.html', 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    media_urls = fetch_instagram_photos()
    update_website_gallery(media_urls)
