from bs4 import BeautifulSoup
import requests
from csv import writer
# url='https://www.yellowpages.com/'
# url='http://localhost:8000/'
url='https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New+York%2C+NY'
# url='https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20York%2C%20NY&page=2'

# for i in range(1,7):
#     url=f'https://www.yellowpages.com/search?search_terms=electric+motor+repair&geo_location_terms=New+York%2C+NY&page-{0}'.format(i)

# url='http://localhost:3000/'
# url='http://localhost:8080/test'

try:
    res=requests.get(url)
    soup_res = BeautifulSoup(res.content,'html.parser')
    all_info_div= soup_res.find_all('div',class_='info')
except Exception as e:
    print(e)
else:

    for tagsobject in all_info_div:
        try:
            name= tagsobject.find(attrs={"class":"business-name"}).span.get_text()
            website= tagsobject.find(attrs={"class":"links"}).a.get['href']
            phone_no= tagsobject.find(attrs={"class":"phones phone primary"}).get_text().strip('')
            address_1= tagsobject.find(attrs={"class":"adr"}).find('div',{'class':'street-address'}).text
            address_2= tagsobject.find(attrs={"class":"adr"}).find('div',{'class':'locality'}).text
        except Exception as e:
            print(e)
        else:
            print('\n')
            print(name,website,phone_no,address_1,address_2)
            print('\n')
           
























# list1 = []

# name1={'Name':'Ajay',"Address":'178 Shiv Durga Vihar, Lakkarpur','pin':'121008','houseColor':'lightblue'}
# name2={'Name':'Rajnath',"Address":'H-150 Mohan Durga Vihar, Shivpur','pin':'621008','houseColor':'cyan'}
# name3={'Name':'Vijay kumar',"Address":'G-196 Noida, UP','pin':'121008','houseColor':'green'}
# name4={'Name':'Neeraj Sharma',"Address":'M block Shimla, Himachal','pin':'761008','houseColor':'blue'}
# name5={'Name':'Varun',"Address":'158 Shiv Mohan Coloney, Lakkarpur Fhatak','pin':'121008','houseColor':'lightblue'}
# name6={'Name':'Mohan kumar alowalia',"Address":'D-187 Duwarka , Delhi','pin':'881099','houseColor':'lightblue'}
# name7={'Name':'Arivind kejriwal',"Address":'P-187 CM_Awas , Delhi','pin':'950033','houseColor':'White'}
# name8={'Name':'Amit Singh',"Address":'D-187 Khelpur , Patna','pin':'899099','houseColor':'lightblue'}
# name9={'Name':'Kumar awiswas',"Address":'!189 Mohanpura , Delhi','pin':'881099','houseColor':'lightblue'}
# name10={'Name':'Shankar singh',"Address":'N-38 Houskhas , Delhi','pin':'651099','houseColor':'blue'}
# name11={'Name':'Rahul Jaiswal',"Address":'D-187 Duwarka , Delhi','pin':'231099','houseColor':'green'}
# name12={'Name':'Mohan Rao',"Address":'D-187 Duwarka , Delhi','pin':'881099','houseColor':'lightyellow'}
# name13={'Name':'Rithic Andkhar',"Address":'A-145 Mangolpuri , Delhi','pin':'651099','houseColor':'white'}
# name14={'Name':'Kumar yadirapa',"Address":'U-77 Blackpur , Cheenai','pin':'871099','houseColor':'yellow'}
# name15={'Name':'Mini kumari',"Address":'I 178 Nawabpura , Faridabad Haryana','pin':'871099','houseColor':'salmon'}
# name14={'Name':'Medha rani',"Address":'R-179 Mandanpur khadar, Delhi','pin':'871099','houseColor':'yellow'}
# name16={'Name':'Kumar yadirapa',"Address":'U-77 Greenpur, Mumbai','pin':'871099','houseColor':'lightyellow'}
# name17={'Name':'Arjun kumar singh',"Address":'U-77 Whitepur ,Madyapardesh','pin':'871099','houseColor':'skygreen'}
# name18={'Name':'Rani devi',"Address":'J-189 Mathura, Uttarpardesh','pin':'871099','houseColor':'yellow'}
# name19={'Name':'Somit Das',"Address":'U-77 Gorakhpur , Gitapressh','pin':'871099','houseColor':'seagreen'}
# name20={'Name':'Yogi Adityanath',"Address":'R-998 Masuri ,Utrakhand','pin':'871099','houseColor':'lightskygreen'}



# list2= ['1',3,'Nine']
# res= 'Raju' not in list1
# con=list1 + list2
# list1.append(name1)
# list1.append(name2)
# list1.append(name3)
# list1.append(name4)
# list1.append(name5)
# list1.append(name6)
# list1.append(name7)
# list1.append(name8)
# list1.append(name9)
# list1.append(name10)
# list1.append(name11)
# list1.append(name12)
# list1.append(name13)
# list1.append(name14)
# list1.append(name15)
# list1.append(name16)
# list1.append(name17)
# list1.append(name18)
# list1.append(name19)
# list1.append(name20)


# print('\n')
# print(list1[2:6])
# print(list1)

# name='Ajay is a good boy'
# print(name[-3:])
# print('\n')
# print(list1[-1].get('Name'))
# print(list1[-1].get('Address'))
# print(list1[-1].get('pin'))




# res=requests.get(url)
# soup_res = BeautifulSoup(res.content,'html.parser')

# all_data= soup_res.find_all('div',class_='info-section info-secondary')
# s_no=[]
# company_name=[]
# company_address=[]
# print("The length of i",len(all_data))
# for i in all_data:
#     try:
#         address=i.find(attrs={'class':'adr'}).find(attrs={'class':'street-address'}).string
#         address2=i.find(attrs={'class':'adr'}).find(attrs={'class':'locality'}).string
#         phones=i.find(attrs={'class':'adr'}).parent.find(attrs={'class':'phones phone primary'}).string
#         name=i.find(attrs={'class':'adr'}).parent.parent.find(attrs={'class':"business-name"}).span.text
#         website=i.parent
#     except Exception as e:
#         print(e)
#     else:
#         print('\n')
#         combine_add=address + address2


#         print("Contact_no", phones)
#         print("Name",name)
#         print("Address", combine_add)
#         print("website", website)
        # break
    

    


    
    # s_1=i.span.text.strip('.)')
    # s=i.find(attrs={'class':"address"}).parent.span.text.strip('.)')
    # name=i.find(attrs={'class':"company_name"}).text
    # address=i.find(attrs={'class':"address"}).text.strip()

    # print(s_1)

    # print(f's_no',s_no,'copany_name',company_name,'address',company_address)
    # s_no.append(s)
    # company_name.append(name)
    # company_address.append(address)




# print("Serial_no",s_no)
# print("Company_name",company_name)
# print("Address",company_address)








# print(soup_res.find(attrs={'class':'para'}).span.text.strip('.)'))
# print(soup_res.find(attrs={'class':'address'}).text.strip())
# print(soup_res.find(attrs={'class':'company_name'}).text.strip())
# print(type(soup_res.find('div',{'class':'address'})))



# print(type(soup_res.ul.text))
# print(soup_res.ul.li.parent.find('li',{"class":"link_para"}))
# print(soup_res.ul.li.parent.find_all('p'))

# for item in soup_res.ul.li.parent.find_all('p'):
#     print(item.text.strip(' '))


# for item in soup_res.find_all('p'):
#     print(item.text.strip(' '),'\n')




# myList = [
# 	{
# 		'name':"Mayank",
# 		'stadard':"Graduate",
#         'lastname':'Singh',
# 	},
# 	{
# 		'Area':"178 Shiv Durga Vihar,lkd fbd",
# 		'car':'Baleno Sigma Model',
#         'varient':'petrol',
#         'normsFollow':'bs6',
# 	},
# 	{
# 		'bhai':'ansk',
# 		'dost':'veeru'
# 	}
# ]

# print(myList[0]['name'])
# print(myList[0]['stadard'])
# print(myList[2]['bhai'])
# print(myList[2]['dost'])
# print(myList[1]['normsFollow'])

# print(myList[2].get('dost'))


# try:
#     res=requests.get(url)
# except:
#     print("server did't respond..")    
# else:
#     soup_res = BeautifulSoup(res.content,'html.parser')
#     one_res= soup_res.find_all(attrs={'class':"info"})
#     # print(one_res)
#     for i in one_res:
#         print(i.find(attrs={'class':"business-name"}).contents[0].string)
#         address=i.find(attrs={'class':"street-address"}).contents[0].string
#         Street_address=i.find(attrs={'class':"street-address"}).contents[0].string
#         Street_locality=i.find(attrs={'class':"locality"}).contents[0].string
#         address=Street_address+Street_locality
#         if len(address)>0:
#             print(address)
#         break
        
        
    

    # for item in one_res:
    #     one= item.find(attrs={"class":"business-name"})
    #     rating= item.find(attrs={"class":"count"}).string.replace('(','').replace(')','')
    #     yearsinbusi= item.find(attrs={"class":"number"})
    #     comments= item.find(attrs={"class":"body with-avatar"})
        
        


    #     final= one.select("span")
        
    #     try:
    #         print('\n\n')
    #         if len(final)>0:
    #             print("Name of Restro ||",final[0].string)
    #         if len(rating)>0:
    #             print("customerRating",rating)
    #         if len(yearsinbusi)>0:
    #             print("duration",yearsinbusi)
    #         if len(comments)>0:
    #             print("Comments =>>",comments)
    #         print('\n\n')
    #     except Exception as e:
    #         # print("An error has just occured..")
    #         print(e)

        


    # lists=soup_res.find_all(attrs={'class':'nav_link_btn'})
    # for item in lists:
    #     a=item.find('a')['href']
    #     print(a)
    #     if a=='#':
    #      a.replace('#','Id links')
        # print(['href'])

        # find('a')['href']

    # print(type(lists))
    




# lists=soup_res.find_all('div',class_='v-card')


# with open('data.csv','w',encoding='utf8',newline='') as fi:

#     thewriter=writer(fi)
#     header=['TotalRevies','Comments']
#     hading_one=['Restro in NewYork city']
#     thewriter.writerow(hading_one)
#     thewriter.writerow(header)

    # print(lists)
    # for item in lists:
        # restaurants_name=item.find('span',class_="business-name").text
        # category=item.find('a',class_="categories").text
        # yearsinbussness=item.find('div',class_="number").text
        # rating=item.find('span',class_="count").text.replace('(','').replace(')','')
        # comment=item.find('p',class_="body with-avatar").text

        # all_data=[yearsinbussness,rating,comment]
        # thewriter.writerow(all_data)







