import requests
import pandas as pd
from bs4 import BeautifulSoup

Name    = []
Ratings = []
A_Price = []
D_Price = []
Discount= []
Property= [] 

for i in range(1,21):
    url = "https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_e43eecab-5426-48e5-830c-25a3e817318d_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&page="+str(i)
    response = requests.get(url)
    print(f"Page{i} is has {response}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    #soup = souper.find("div", class_="DOjaWF gdgoEp")
    #Extracting name of the product
    name = soup.find_all("div", class_="KzDlHZ")
    for n in name:
        Name.append(n.text)
    print("NAME",len(Name))
    #Extracting star-rating of the product
    stars = soup.find_all("div",class_="XQDdHH")
    for r in stars:
        Ratings.append(r.text)
    #print("RATING",len(Ratings))
    #Extracting the actual price before any discount
    a_prices = soup.find_all("div",class_="yRaY8j ZYYwLA")
    for a in a_prices:
        A_Price.append(a.text)
    print("A_PRICE",len(A_Price))
    #Extracting the discouted price
    d_prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")
    for d in d_prices:
        D_Price.append(d.text)
    print("D_PRICE",len(D_Price))
    #Extracting the discount on the price
    discount = soup.find_all("div", class_="UkUFwK")
    for di in discount:
        Discount.append(di.span.text)
    #print("DISCOUNT",len(Discount))
    #Extracting the other details
    ul_tags = soup.find_all('ul', class_='G4BRas') #properties
    for ul in ul_tags:
        Property.append([li.get_text() for li in ul.find_all('li')])
    print("PROPERTY",len(Property))
 

""" print("NAME",len(Name))
print("RATING",len(Ratings))
print("A_PRICE",len(A_Price))
print("D_PRICE",len(D_Price))
print("DISCOUNT",len(Discount))
print("PROPERTY",len(Property)) """

#print(Name)
#print(Ratings)
#print(A_Price)
#print(D_Price)
#print(Discount)
#print(Property)


data = {
    "NAME": Name,
    #"RATINGS": Ratings,
    "ACTUAL PRICE": A_Price,
    "DISCOUNTED PRICE": D_Price,
    #"DISCOUNT": Discount,
    "OTHER PROPERTIES": Property
}
    
df = pd.DataFrame(data)

df.to_csv("Flipkart laptop data.csv")
