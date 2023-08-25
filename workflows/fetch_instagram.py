import requests
import json

ACCESS_TOKEN = 'YOUR_INSTAGRAM_ACCESS_TOKEN'

def fetch_instagram_photos():
    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,thumbnail_url,permalink&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    # Extract media URLs or other relevant info
    media_urls = [item['media_url'] for item in data['data'] if item['media_type'] == 'IMAGE']
    return media_urls

def update_website_gallery(media_urls):
    # Open your gallery HTML file and update it with the new media URLs.
    # This part will be specific to how your website is structured.
    pass

if __name__ == "__main__":
    media_urls = fetch_instagram_photos()
    update_website_gallery(media_urls)
