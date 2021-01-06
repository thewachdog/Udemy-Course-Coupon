#!/usr/bin/python3
# Don't edit anything
# t.me/new_everything_free
# t.me/no_one_luv_me

import os
import sys
import requests
from bs4 import BeautifulSoup
import time

print('''
\u001b[31m                                        
                                                  
                  ((((                            
                 ((((((          .                
               (((((((         (/(((              
             *((/(((/(       .((/(((              
           ((((((((((       ((((/(((.             
         (((((((/(((.      (((((/(((,             
              ((((((     .(((( (/(((/    ((       
             (((/((/    /(((.  ./(((((((/((       
             (((((((  (((((      ((((((((         
              ((/((((((((                         
               ,((((((.                   
                                                                   
                                                                  
                         \u001b[36m  - t.me/no_one_luv_me
''')
print("")
print("")
print("")
name = input("\u001b[33mEnter Credits : \u001b[32m")
print("")

url = "https://coursevania.com/courses/#"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/83.0.4103.97 Safari/537.36"}

r = requests.get(url, headers=headers)
html = r.text

courselinks1 = []
courselinks2 = []

print("\u001b[36mPlease Wait for Sometimes")
print("")
if r.status_code == 200:

    soup = BeautifulSoup(html, "lxml")
    course1_with_tag = soup.find_all("div", class_="stm_lms_courses__single--info_preview")
    home_link_list = []

    for i in course1_with_tag:
        home_page_link = i.find('a')['href']
        home_link_list.append(home_page_link)

    for i in home_link_list:
        time.sleep(2)
        url = i

        r2 = requests.get(url, headers=headers)
        html_coursepage = r2.text

        if r2.status_code == 200:
            soup2 = BeautifulSoup(html_coursepage, "lxml")
            udmey_link_in_list = soup2.find_all(class_="btn btn-default btn_big text-center no-price")
            x = str(udmey_link_in_list[0])
            find_start = int(x.find('href="')) + 6
            find_end = int(x.find('"', find_start))
            courselinks1.append(x[find_start:find_end])

print(" \u001b[31m50% Completed\u001b[37m")
print("")
print("")
print("")

url2 = "https://coursevania.com/wp-admin/admin-ajax.php?offset=1&template=courses%2Fgrid&args=%7B%22image_d%22%3A" \
       "%22img-480-380%22%2C%22per_row%22%3A%224%22%2C%22posts_per_page%22%3A%2212%22%2C%22class%22%3A%22archive_grid" \
       "%22%7D&action=stm_lms_load_content&sort=date_high "

r2 = requests.get(url2, headers=headers)

if r2.status_code == 200:

    json = r2.json()
    content = json["content"]

    soup = BeautifulSoup(content, 'lxml')
    homelinktags = soup.find_all('a')

    home_link_list_double = []
    home_link_set = {}
    home_link_list = []

    for i in homelinktags:
        y = str(i)
        find_start = int(y.find('href="')) + 6
        find_end = int(y.find('"', find_start))
        home_link_list_double.append(y[find_start:find_end])
    home_link_set = set(home_link_list_double)
    home_link_list = list(home_link_set)

    for i in home_link_list:
        time.sleep(2)
        url = i
        r2 = requests.get(url, headers=headers)
        html_coursepage = r2.text

        if r2.status_code == 200:
            soup2 = BeautifulSoup(html_coursepage, "lxml")
            udmey_link_in_list = soup2.find_all(class_="btn btn-default btn_big text-center no-price")
            x = str(udmey_link_in_list[0])
            find_start = int(x.find('href="')) + 6
            find_end = int(x.find('"', find_start))
            courselinks2.append(x[find_start:find_end])

    print("**🔰 Udemy Course Coupon  🔰**")
    print("")
    print("**🔥➖{}➖🔥**".format(name))
    print("")
    print("#fresh")
    print("")

for i in range(len(courselinks1)):
    courselinkss = courselinks1[i]
    start = courselinkss.find("course/") + 7
    end = courselinkss.find("/", int(start))

    coursename = courselinkss[start:end].replace("-", " ").title()
    print("🌀{}".format(coursename))
    linkwithspace = courselinkss[:end + 1] + "?join:@new_everything_free&" + courselinkss[end + 2:]
    print(linkwithspace)
    print("")

print("")
print("")
time.sleep(2)
print("--------------------------------------------------------------------------------------------------------")

print("")
print("")

print("**🔰 Udemy Course Coupon  🔰**")
print("")
print("**🔥➖{}➖🔥**".format(name))
print("")
print("#may_be_old (But still Working 🤩)")
print("")
for i in range(len(courselinks2)):
    courselinkss = courselinks2[i]
    start = courselinkss.find("course/") + 7
    end = courselinkss.find("/", int(start))

    coursename = courselinkss[start:end].replace("-", " ").title()
    print("🌀{}".format(coursename))
    print("")
    linkwithspace = courselinkss[:end + 1] + "?join:@new_everything_free&" + courselinkss[end + 2:]
    print(linkwithspace)
    print("")

# t.me/new_everything_free
# t.me/no_one_luv_me

