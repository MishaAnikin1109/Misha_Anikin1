import requests
import os

ACCESS_KEY = "your_access_key" #Приклад вашого ключа

def download_images(query="programming languages", count=5):
    url = "https://api.unsplash.com/photos/random"
    headers = {
        "Authorization": f"Client-ID {ACCESS_KEY}"  
    }
    params = {
        "query": query,
        "count": count
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    images = response.json()
    
    os.makedirs("downloaded_images", exist_ok=True)
    
    for i, img in enumerate(images, start=1):
        img_url = img["urls"]["regular"]
        img_data = requests.get(img_url).content
        file_path = f"downloaded_images/image_{i}.jpg"
        
        with open(file_path, "wb") as file:
            file.write(img_data)
        print(f"Зображення {i} завантажено і збережено як {file_path}")
        
try:
    downloaded_images()
except requests.exceptions.RequestException as e:
    print(f"Помилка завантаження сторінки: {e}")
        
        
        