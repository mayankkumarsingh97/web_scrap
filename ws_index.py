from bs4 import BeautifulSoup
import requests
from csv import writer
# url='https://www.yellowpages.com/'
url='https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New+York%2C+NY'
res=requests.get(url)
soup_res = BeautifulSoup(res.content,'html.parser')
lists=soup_res.find_all('div',class_='result')


with open('data.csv','w',encoding='utf8',newline='') as fi:

    thewriter=writer(fi)
    header=['TotalRevies','Comments']
    hading_one=['Restro in NewYork city']
    thewriter.writerow(hading_one)
    thewriter.writerow(header)

    # print(lists)
    for item in lists:
        # restaurants_name=item.find('span',class_="business-name").text
        # category=item.find('a',class_="categories").text
        yearsinbussness=item.find('div',class_="number").text
        rating=item.find('span',class_="count").text.replace('(','').replace(')','')
        comment=item.find('p',class_="body with-avatar").text

        all_data=[yearsinbussness,rating,comment]
        thewriter.writerow(all_data)
        # print(all_data)






