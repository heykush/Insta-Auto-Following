from selenium import webdriver
from getpass import getpass
from time import sleep
driver=webdriver.Chrome(r"C:\Python\chromedriver.exe")
driver.maximize_window()
driver.get('https://instagram.com')
sleep(1)

user=input("Enter the Username: ")
pwd=getpass("Enter the Password: ")
sleep(1)
id_user=driver.find_element_by_xpath('//input[@name="username"]').send_keys(user)
pas=driver.find_element_by_xpath('//input[@name="password"]').send_keys(pwd)
log=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
sleep(2)
pop=driver.find_element_by_xpath('//button[(text()="Not Now")]').click()

s=input("search for the person: ")
sleep(1)
search=driver.find_element_by_xpath('//input[@type="text"]').send_keys(s)
sleep(3)
in_search=driver.find_element_by_xpath(f'//a[@href="/{s}/"]').click()
sleep(2)
folow=driver.find_element_by_xpath(f'//a[@href="/{s}/followers/"]').click()
sleep(2)

scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
for n in range(1, 1000):
    sleep(1)
    follow =driver.find_element_by_xpath('(//button[text()="Follow"])[position()>=2 and position()<1000]').click()
    sleep(1)
    ht = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
        return arguments[0].scrollHeight;
        """, scroll_box)
