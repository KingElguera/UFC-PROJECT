import requests
from bs4 import BeautifulSoup

url = "https://www.ufc.com/athletes/all?gender=1&search=&page=1"
response = requests.get(url)
# print(response.status_code)


if response.status_code == 200: 
    html_doc = response.text 
    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup) 
    fighters = soup.find_all('span', class_="c-listing-athlete__name")
    
    names = []
    for fighter in fighters:
        names.append(fighter.text.strip())

# unique_names = list(dict.fromkeys(names))
# for name in unique_names:
#     print(name)   

all_names = []

for page_num in range(2, 255):
    url = f"https://www.ufc.com/athletes/all?gender=1&search=&page={page_num}"
    response = requests.get(url)
    print(f'page{page_num}: {url}')
    if response.status_code == 200: 
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        fighters = soup.find_all('span', class_="c-listing-athlete__name")
        for fighter in fighters:
            name = fighter.text.strip()
            if name not in all_names: 
                all_names.append(name) 
                # print(name)
                # print("______________________"*9)
                # print(len(name))
                print("\nTotal de combattants uniques :", len(all_names))