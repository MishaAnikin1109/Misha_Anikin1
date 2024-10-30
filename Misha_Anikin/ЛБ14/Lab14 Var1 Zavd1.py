import requests
from bs4 import BeautifulSoup

url = "https://statti.in.ua/"

try:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    text = soup.get_text()
    
    with open("text.txt", "w", encoding="utf-8") as file:
        file.write(text)
        
    print("Текст успішно збережено в файл text.txt")
    
except requests.exceptions.RequestException as e:
    print(f"Помилка завантаження сторінки: {e}")