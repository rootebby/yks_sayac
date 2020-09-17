from selenium import webdriver
import time
import os

url = "https://matematikdelisi.com/yks/sayac/tyt-yks-ne-zaman-kac-gun-kaldi-sayaci.html"

browser = webdriver.Firefox()

browser.get(url)

time.sleep(5)
"""
gün = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[2]/p[1]')
saat = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[2]/p[1]')
dakika = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div/div/div[2]/p[1]')
saniye = browser.find_element_by_xpath('//p[@class="val pulse"]')
"""
while True:
    gün = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[2]/p[1]')
    saat = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[2]/p[1]')
    dakika = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div/div/div[2]/p[1]')
    saniye = browser.find_element_by_xpath('//p[@class="val pulse"]')
    if os.name == "posix":
        time.sleep(1)            
        os.system("clear")
        print(f"""
        *************************
        | coded by root@ebby:~# |
        *************************
                   GÜN          
        *************************
                {gün.text}     
        *************************
                   SAAT         
        *************************
                {saat.text}     
        *************************
                  DAKİKA        
        *************************
                {dakika.text}         
        *************************
                  SANİYE        
        *************************
                {saniye.text}
        *************************  
""")
    
    elif os.name == "nt":
        time.sleep(1)        
        os.system("cls")
        print(f"""
        *************************
        | coded by root@ebby:~# |
        *************************
                   GÜN          
        *************************
                {gün.text}     
        *************************
                   SAAT         
        *************************
                {saat.text}     
        *************************
                  DAKİKA        
        *************************
                {dakika.text}         
        *************************
                  SANİYE        
        *************************
                {saniye.text}
        *************************  
""")
    
    else:
        time.sleep(1)
        print(f"""
        *************************
        | coded by root@ebby:~# |
        *************************
                   GÜN          
        *************************
                {gün.text}     
        *************************
                   SAAT         
        *************************
                {saat.text}     
        *************************
                  DAKİKA        
        *************************
                {dakika.text}         
        *************************
                  SANİYE        
        *************************
                {saniye.text}
        *************************  
""")





