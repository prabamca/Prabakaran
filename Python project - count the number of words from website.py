from bs4 import BeautifulSoup
import requests
 
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
        vn = cn.count(wd)
        so.append(vn)
    Sum = sum(so)
    print(Sum)
    
else:
    print("Invalid URL / URL not loaded successfully...")


    
