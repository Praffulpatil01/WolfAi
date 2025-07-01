# from datetime import datetime
# from utils.content_generator import generate_blog
# from utils.image_generator import get_placeholder_image
# from utils.wordpress_uploader import publish_post

# def main():
# # topic = "Top 5 Free AI Tools for Creators in 2025"
# # #print("Generating content...")
# # blog_content = generate_blog(topic)
# # #print("Generating image...")
# # image_path = get_placeholder_image(topic)
# # #print("Publishing to WordPress...")
# # success = publish_post(topic, blog_content)
# # #print(f"[{datetime.now()}] Blog published: {success}")

# # if __name__ == "__main__":
# # main()

# from utils.content_generator import generate_blog
# from utils.image_generator import get_placeholder_image  # or real image generator
# from utils.wordpress_uploader import publish_post

# def main():
#   # STEP 1: Define your topic
#   topic = "Top 5 Free AI Tools for Creators in 2025"  # You can replace with dynamic trending topic

#   print("Generating blog content...")
#   blog_content = generate_blog(topic)

#   print("Generating image...")
#   image_path = get_placeholder_image(topic)  # Or use real AI-generated image

#   print("Publishing blog...")
#   success = publish_post(topic, blog_content,image_path)

#   if success:
#     print("✅ Blog published successfully!")
#   else:
#     print("❌ Failed to publish blog.")

# if __name__ == "__main__":
#   main()
#from utils.wordpress_uploader import publish_post

# Example post

# main.py
from datetime import datetime
from utils.content_generator import generate_blog
from utils.image_generator import get_placeholder_image
from utils.wordpress_uploader import publish_post
from utils.trending_topic import fetch_trending_topic  # trending topic fetcher


def main():
  print("🧠 Fetching trending topic...")
  topic = fetch_trending_topic()
  print("🎯 Topic:", topic)

  print("✍️ Generating content...")
  blog_content = generate_blog(topic)

  #print("🖼️ Generating image...")
  #image_path = get_placeholder_image(topic)

  print("🚀 Publishing post to WordPress...")
  success = publish_post(topic, blog_content)

  print(f"[{datetime.now()}] ✅ Blog published: {success}")


if __name__ == "__main__":
  main()
