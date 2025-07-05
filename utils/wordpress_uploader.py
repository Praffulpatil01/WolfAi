import requests
import os

ACCESS_TOKEN = os.getenv("WP_ACCESS_TOKEN")
SITE_ID = os.getenv("WP_BLOG_ID")


def publish_post(title, content):
    url = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE_ID}/posts/new"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    post_data = {"title": title, "content": content, "status": "publish"}
    res = requests.post(url, headers=headers, data=post_data)
    print("✅ Published:", res.status_code == 201)
    print("📝 HTML Content Preview:\n", content[:500], "...\n")
    print(res.json())


#import requests

#ACCESS_TOKEN = "7fwhl9ePOXpJQFo^ecku9D6J&)MXOa8h$$uQ03u7mZ0!ALqaSltQ7iKCLN&)Rl8W"
# Paste the token you just got
#SITE_ID = "245890663"             # Paste your blog_id (a number)

# def publish_post(title, content):
#     url = f"https://public-api.wordpress.com/rest/v1.1/sites/{SITE_ID}/posts/new"
#     headers = {
#         "Authorization": f"Bearer {ACCESS_TOKEN}"
#     }
#     post_data = {
#         "title": title,
#         "content": content,
#         "status": "publish"
#     }

#     response = requests.post(url, headers=headers, data=post_data)
#     if response.status_code == 201:
#         print("✅ Blog posted successfully!")
#     else:
#         print("❌ Failed to post")
#         print("Status:", response.status_code)
#         print("Response:", response.text)

# utils/wordpress_publisher.py

# Replace with your real token and site ID
#import os
#import requests

#def publish_post(title, content, image_path):
#access_token = os.getenv("WP_ACCESS_TOKEN")
#blog_id = os.getenv("WP_BLOG_ID")

#f not access_token or not blog_id:
#raise Exception("WordPress access token or blog ID not set.")

# Upload the image
#media_url = f"https://public-api.wordpress.com/rest/v1.1/sites/{blog_id}/media/new"
#with open(image_path, "rb") as image_file:
#files = {'media[]': image_file}
#headers = {'Authorization': f'Bearer {access_token}'}
#media_res = requests.post(media_url, headers=headers, files=files)

#if media_res.status_code != 200:
#print("❌ Image upload failed:", media_res.text)
#return False

#image_data = media_res.json()
#image_url = image_data["media"][0]["URL"]

# Create post
#post_url = f"https://public-api.wordpress.com/rest/v1.1/sites/{blog_id}/posts/new"
# post_data = {
#"title": title,
#"content": f"<img src='{image_url}' /><br><br>{content}",
#"status": "publish"
#}

#post_res = requests.post(post_url, headers=headers, json=post_data)

#if post_res.status_code == 201:
#return True
#else:
# print("❌ Post failed:", post_res.text)
#return False
