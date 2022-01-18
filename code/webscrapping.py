import requests
from bs4 import BeautifulSoup as BS


url = "https://jumia.com.ng/smartphones/"
headers = requests.utils.default_headers()
headers.update({
   "user-agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
})

my_response = requests.get(url, headers)
# print(my_response)
# print(my_response.status_code)

first_soup = BS(my_response.content, features = "lxml")
# print(first_soup)
# second_soup = first_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})

# list_of_soups = second_soup.find_all("article", attrs = {"class" : "prd _fb col c-prd"})

# for soup in list_of_soups:
#     print(soup.prettify())
#     phone_details = soup.find("a")
#     ###FOR PHONE BRAND
#     try:
#         phone_brand = phone_details.get("data-brand")
#         # print(phone_brand)
#     except:
#         phone_brand = None

#         ###FOR PHONE SPECIFICATION
#     try:
#         phone_description = phone_details.get("data-name")
#         # print(phone_description)
#     except:
#         phone_description = None

#         ###FOR OLD PRICE
#     try:
#         old_div = soup.find("div", attrs = {"class" : "old"})
#         phone_old_price = int((old_div.text).lstrip("₦ ").replace(",", ""))
#         print(phone_old_price)
#     except:
#         phone_old_price = None

#         ##FOR NEW PRICE
#     try:
#         prc_div = soup.find("div", attrs = {"class" : "prc"})
#         phone_old_price = int((prc_div.text).lstrip("₦ ").replace(",", ""))
#         print(phone_old_price)
#     except:
#         phone_old_price = None

#         ###FOR DISCOUNT
#     try:
#         tag_dsct_sm_div = soup.find("div", attrs = {"class" : "tag _dsct _sm"})
#         tag = tag_dsct_sm_div.text
#         print(tag)
#     except:
#         tag_dsct_sm_div = None

#         ##for ratings
#     try:
#         star = soup.find("div", attrs = {"class" : "stars _s"})
#         ars = (star.text).strip(" out of 5")
#         rs = float(ars)
#         print(rs)
#     except:
#         star = None

#     break

