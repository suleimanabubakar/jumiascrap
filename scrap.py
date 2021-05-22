import csv
from bs4 import BeautifulSoup
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager                                         

# for chrome
# driver = webdriver.Chrome("C:\Users\Admin\Desktop\chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())

# url function 
def  get_url(search_term):
    urlLink = "https://www.jumia.co.ke/catalog/?q={}"
    # removing empty spaces
    search_term = search_term.replace(' ','+')

    # url formating
    return urlLink.format(search_term)

     
 

# url 
url = get_url('monitor')


driver.get(url)

soup = BeautifulSoup(driver.page_source,'html.parser')
results = soup.find_all('article',{'class':'prd _fb col c-prd'})



item = results[0]

name = item.h3.text
price = item.find('div','prc').text
discountblock = item.find('div','s-prc-w')
oldprice = discountblock.find('div','old').text
discount = discountblock.find('div','tag _dsct _sm').text
rating = item.find('div','stars _s').text
revBlock = item.find('div','rev').text
reviews = revBlock.replace(rating,'')
print(reviews)
