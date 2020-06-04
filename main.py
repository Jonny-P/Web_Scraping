import bs4 as bs
from urllib.request import Request, urlopen
import pickle
import os
import sys



#INIT Var
project_path = os.getcwd()
data_pickle_path = project_path + "\\data_pickle\\instance_data.pickle"


try:
    with open(data_pickle_path, "rb") as f:
        sauce = pickle.load(f)
    print("Instance Pickle File Loaded!")
except:
    req = Request('https://www.standvirtual.com/carros/bmw/?search%5Bfilter_enum_engine_code%5D=serie-1&search%5Bnew_used%5D=all', headers={'User-Agent': 'XYZ/3.0'})

    sauce = urlopen(req, timeout=10).read()

    #Serialize request instance (TEST CASE ONLY)
    with open(data_pickle_path , "wb") as f:
        pickle.dump((sauce), f)



# sauce = urlopen(req, timeout=10).read() #source code for webpage

soup = bs.BeautifulSoup(sauce,'lxml') #create soup object from the extracted source code
# soup = bs.BeautifulSoup(sauce,'html') 






#Example Soup Functionalities
#--------------------------------------
# print(soup.title.text) 

# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# print(soup.get_text())

# print(soup.find_all('p'))

# for url in soup.find_all('a'): 
#     print(url.get('href'))

#----------------------------------------

title_list = []
specs_list = []
price_list = []



div = soup.find_all("div", {"class": "offers list"})

for article in div:
    art = article.find_all("article")
    for div in art:
        title = div.find("div", {"class": "offer-item__title"}).find('a').text.strip()
        title_list.append(title)


        specs = div.find("ul", {"class": "ds-params-block"})

        fuel_type = specs.find('li' , {"data-code": "fuel_type"}).find('span').text.strip()
        first_registration_month = specs.find('li' , {"data-code": "first_registration_month"}).find('span').text.strip()
        first_registration_year = specs.find('li' , {"data-code": "first_registration_year"}).find('span').text.strip()
        mileage = specs.find('li' , {"data-code": "mileage"}).find('span').text.strip()
        power = specs.find('li' , {"data-code": "power"}).find('span').text.strip()
        specs_list.append([fuel_type,first_registration_month,first_registration_year,mileage,power])

   
        price_list.append(div.find("div", {"class": "offer-price ds-price-block"}).find('span').text.strip().splitlines()[0])


        # print(title_list)
        # print(specs_list)
        # print(price_list)
        # break


print(title_list)
print(specs_list)
print(price_list)