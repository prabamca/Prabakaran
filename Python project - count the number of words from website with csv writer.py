from bs4 import BeautifulSoup
import requests
import csv
 
url = input()
wd = input()
gt = requests.get(url)
if gt.status_code==200:
    soup = BeautifulSoup(gt.text, 'lxml')
    so = []
    for link in soup.find_all('a'):
        
        nv = (link.get('href'))
        ft = (url + nv)
        #print(ft)
        p = requests.get(ft, allow_redirects=True)
        soup = BeautifulSoup(p.text, 'lxml')
        tn = soup.get_text().lower()
        cn = tn.split()

        with open("Test.csv", "a", newline='') as f:
                w = csv.writer(f)
                for x in cn:
                    ex = x.encode('utf8')
                    w.writerow([ex])

        f1 = open("Test.csv", "r")
        rd = f1.read()
        f1.close()
        
        vn = cn.count(wd)
        so.append(vn)                
        
    Sum = sum(so)
    print(Sum)
else:
    print("Invalid URL / URL not loaded successfully...")


    
