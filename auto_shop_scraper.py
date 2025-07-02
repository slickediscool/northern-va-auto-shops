import requests
from bs4 import BeautifulSoup
import boto3
import time

def scrape_auto_shops(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    shops = []
    for shop in soup.find_all('div', class_='VkpGBb'):
        name = shop.find('div', class_='dbg0pd').text
        rating = shop.find('span', class_='YDIN4c').text if shop.find('span', class_='YDIN4c') else 'N/A'
        address = shop.find('div', class_='rllt__details').find_all('div')[1].text
        
        # Try to extract specialties or services offered
        services = shop.find('div', class_='rllt__details').find_all('div')
        specialties = services[2].text if len(services) > 2 else 'General auto repair'
        
        shops.append({
            'name': name,
            'rating': rating,
            'address': address,
            'specialties': specialties
        })
    
    return shops

def store_in_dynamodb(shops):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('AutoShops')
    
    for shop in shops:
        table.put_item(Item=shop)

def main():
    base_url = "https://www.google.com/search?tbm=lcl&q=best+rated+automotive+shops+in+northern+va"
    shops = scrape_auto_shops(base_url)
    
    store_in_dynamodb(shops)
    print(f"Scraped and stored {len(shops)} auto shops.")

if __name__ == "__main__":
    main()
