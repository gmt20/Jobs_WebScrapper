# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:00:40 2019

@author: gmt20
"""


import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

title_list =[]
company_list = []
salary_list = []
loc_list = []
link_list = []
summary_list = []
page_no = 0
job_name = "machine+learning+internship"
loc_name = "New+Delhi"
state_name = "Delhi"
for i in range(2):
    
    url = "https://www.indeed.co.in/jobs?q=" + job_name +"&l=" + loc_name + "%2C+" + state_name + "&start="+str(page_no)
    print(url)
    page =  urllib.request.urlopen(url)

    soup = BeautifulSoup(page,"lxml")
    res = soup.select(".row")
    if res is not None:
        for container in res:
            #title
            title_class = container.select(".row .jobtitle")[0]
            print(title_class)
            if title_class is not None and title_class != []:
                link_class = title_class.find("a")
                print(link_class)
                if link_class is not None and link_class != []:
                    title_desc = link_class.get("title")
                    link_desc= "https://www.indeed.co.in"+ link_class.get("href")
                    title_list.append(title_desc)
                    link_list.append(link_desc)
                    print(title_desc)
                    print(link_desc)
            else:
                title_list.append("No Information available")
                link_list.append("No Information available")
        
                
            #company
            company_class = container.select(".row .company")
                
            if company_class is not None and company_class != []:
                print(company_class)
                company_desc = company_class[0].text.lstrip()
                company_list.append(company_desc)
                print(company_desc)
            else:
                company_list.append("No Information available")
            
            #location
            location_class = container.select(".row .location")
                
            if location_class is not None and location_class != []:
                print(location_class)
                location_desc = location_class[0].text
                loc_list.append(location_desc)
                print(location_desc)
            else:
                loc_list.append("No Information available")
            
            #salary
            salary_class = container.select(".row .salarySnippet .salary")
                
            if salary_class is not None and salary_class != []:
                print(salary_class)
                salary_desc = salary_class[0].text.lstrip()
                salary_list.append(salary_desc)
                print(salary_desc)
            else:
                salary_list.append("No Information available")
        
            
        
            #summary
            summary_class = container.select(".row .snip .summary")
                
            if summary_class is not None and summary_class != []:
                print(summary_class)
                summary_desc = summary_class[0].text.lstrip()
                summary_list.append(summary_desc)
                print(summary_desc)
            else:
                summary_list.append("No Information available")
    time.sleep(10)
    page_no += 10           
print(company_list)
            
print( len(title_list))
print( len (link_list))
print( len(company_list))
print(len(loc_list))
print(len(salary_list))
print(len(summary_list))
cols = ['Title', 'Company', 'Location', 'Link', 'Salary', 'Summary']
jobs = pd.DataFrame({'Title': title_list,
                           'Company': company_list,
                           'Location': loc_list,
                           'Link': link_list,
                           'Salary': salary_list,
                           'Summary': summary_list
                           })[cols]

jobs.to_excel(r'D:jobs.xls', index=None, header=True)

fromaddr = "******"
toaddr = "******"
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Daily Job Update from Indeed"
body = "Please find attched the latest top 20 jobs posted on Indeed.com"
msg.attach(MIMEText(body, 'plain')) 
filename = "jobs.xls"
attachment = open("D:\jobs.xls", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "*******") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 

                
                   
            



            
    
           


