# utils/content_generator.py

#import os
#import requests

#def generate_blog(topic):
# headers = {
#   "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
#   "HTTP-Referer": "https://yourblog.com",
#   "X-Title": "AI Blog Bot"
#}
#payload = {
# "model":
#  "mistralai/mistral-7b-instruct",  # ✅ Updated model
#  "messages": [{
#      "role":
#      "system",
#     "content":
#    "You are an expert AI blogger. Format the blog in clean Markdown with H1, subheadings, meta description, and CTA."
#  }, {
#    "role": "user",
#    "content": f"Write a 700‑word SEO blog post on: {topic}"
#}]
#}
#res = requests.post("https://openrouter.ai/api/v1/chat/completions",
#      headers=headers,
#        json=payload)

# Debug logs
# print("Status Code:", res.status_code)
#print("Response Text:", res.text)

#data = res.json()
#if 'choices' not in data:
#    raise ValueError(
#        "API response has no 'choices'. Check model ID or API key.")
# return data['choices'][0]['message']['content']

import os
import requests


def generate_blog(topic):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "HTTP-Referer": "https://yourblog.com",
        "X-Title": "AI Blog Bot"
    }
    payload = {
        "model":
        "mistralai/mistral-7b-instruct",
        "messages": [{
            "role":
            "system",
            "content":
            "You are an expert AI blogger. Format the blog in clean Markdown with H1, subheadings, meta description, and CTA."
        }, {
            "role": "user",
            "content": f"Write a 700‑word SEO blog post on: {topic}"
        }]
    }

    res = requests.post("https://openrouter.ai/api/v1/chat/completions",
                        headers=headers,
                        json=payload)
    print("Status Code:", res.status_code)

    data = res.json()
    if 'choices' not in data:
        raise ValueError("API response missing 'choices'")

    markdown = data['choices'][0]['message']['content']

    # Replace placeholder image if present
    image_url = "https://yourcdn.com/images/ai-precision-medicine.jpg"
    markdown = markdown.replace("](url-to-image)", f"]({image_url})")

    return markdown
