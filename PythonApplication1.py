from tkinter import TRUE
import requests
from bs4 import BeautifulSoup



while True:

    user_search = input('What to seach for: ')
    print()

    website = ["Amazon", "eBay", "Catch"]


    # Amazon Search
    amazon_search = requests.get("https://www.amazon.com.au/s?k=" + user_search)
    amazon_soup = BeautifulSoup(amazon_search.content, 'html.parser')
    amazon_products_list = amazon_soup.findAll('div', {'class': 's-result-item'})

    # eBay Search
    ebay_search = requests.get("https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=" + user_search)
    ebay_soup = BeautifulSoup(ebay_search.content, 'html.parser')
    ebay_products_list = ebay_soup.findAll('li', {'class': 's-item'})

    # Catch Search
    catch_search = requests.get("https://www.catch.com.au/search?query=" + user_search)
    catch_soup = BeautifulSoup(catch_search.content, 'html.parser')
    catch_products_list = catch_soup.findAll('div', {'class': 'css-rnk79g'})


    for item in amazon_products_list:
        name = item.find('a', attrrs={'class': 'a-text-normal'}, href=True).text
        price = item.find('span', {'class': 'a-offscreen'}).text

        product_dict = {
            'name': name,
            'price': price
        }

        print(product_dict['name'] + " | " + product_dict['price'] + " | " + website[0])
        print()
        print()

    for item in ebay_products_list:
        name = item.find('div', {'class': 's-item__title'}).text
        price = item.find('span', {'class': 's-item__price'}).text

        product_dict = {
            'name': name,
            'price': price
        }

        print(product_dict['name'] + " | " + product_dict['price'] + " | " + website[1])
        print()

    for item in catch_products_list:
        name = item.find('span', {'class': 'css-1ggk143'}).text
        price = item.find('div', {'class': 'css-111drvy'}).text

        product_dict = {
            'name': name,
            'price': price
        }

        print(product_dict['name'] + " | " + product_dict['price'] + " | " + website[2])
        print()