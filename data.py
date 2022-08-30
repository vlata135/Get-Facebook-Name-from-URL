from __future__ import print_function
from time import sleep
from turtle import title
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlsxwriter
import requests
name = []
z = 0

def creatName(content):

    workbook = xlsxwriter.Workbook('Example2.xlsx')
    worksheet = workbook.add_worksheet()
    
    # Start from the first cell.
    # Rows and columns are zero indexed.
    row = 0
    column = 0
    
    
    # iterating through content list
    for item in content :
    
        # write operation perform
        worksheet.write(row, column, item)
    
        # incrementing the value of row by one
        # with each iterations.
        row += 1
        
    workbook.close()

def appearName(url):
    global name
    # url = "https://www.facebook.com/groups/thongtinmuaban.vn/permalink/2599183286879603/"
    r = requests.get(url)
    html = r.text
    #parse the HTML
    soup = BeautifulSoup(html,"lxml")
    # html = BeautifulSoup(urlopen(url))
    # soup = BeautifulSoup(html, 'lxml')
    # type(soup)

    title = soup.find("meta", {"property": "og:title"})
    title = title["content"]  
    # print(title["content"] if title else "No meta title given")

    namePre = title.split(" |",1)[0]
    # name.append(namePre)
    
def getName(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

sheet = pd.read_excel("src/test1.xlsx")
x = sheet[{"LINK"}]

for i in range(40,50):
    y = x.iloc[i,0]
    y = y.split("permalink",1)[0]
    a = getName(y)
    if a == " ": a = "1"
    print(a)
    # name.append(a)
    sleep(2)

creatName(name)
    
    
    



    


    

