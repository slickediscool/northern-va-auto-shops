# Northern Virginia Auto Shops Scraper

This project scrapes data about the best-rated automotive shops in Northern Virginia and stores it in AWS DynamoDB. It's designed to help users find high-quality auto repair services for any type of car.

## Features
- Scrapes data from Google's local search results
- Extracts shop name, rating, address, and specialties (when available)
- Stores data in AWS DynamoDB for easy retrieval and analysis

## Setup
1. Install required packages: `pip install -r requirements.txt`
2. Configure AWS credentials
3. Create a DynamoDB table named `AutoShops` with primary key `name` (string)

## Usage
Run `python auto_shop_scraper.py` to start scraping and storing data.

## Next Steps
- Implement a user interface to query the stored data based on car type or specific repair needs
- Add more detailed information about each shop's specialties and services
- Implement regular updates to keep the data current
