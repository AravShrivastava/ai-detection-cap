from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com/maps/@23.232512,77.430784,12z")

<<<<<<< Updated upstream

def searchplace():
    place = driver.find_element(by=By.CLASS_NAME, value=("tactile-searchbox-input"))
    place.send_keys("Mount carmel school baghmugalia") #destination
    submit = driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button"))
    submit.click()
    sleep(3)

def direction():
    sleep(3)
    direction= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button"))
    direction.click()
    sleep(3)

def find():
    sleep(3)
    find= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input"))
    find.send_keys("Kanha Funcity")#current location
    search_btn= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]"))
    search_btn.click()
    walk = driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button"))
    walk.click()

searchplace()
direction()
find()
=======
def btnclick(xpath):
	f = True
	while f:
		btn= driver.find_elements(by=By.XPATH, value=(xpath))
		if len(btn)>0:
			btn[0].click()
			f = False
		else:
			sleep(1)

def searchplace(place2):
	sleep(4)
	place = driver.find_element(by=By.CLASS_NAME, value=("tactile-searchbox-input"))
	place.send_keys(place2)# destination
	btnclick("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	sleep(4)

def direction():
	sleep(4)
	btnclick("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
	sleep(4)

        

def find(place1):
    sleep(4)
    find= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input"))
    find.send_keys(place1)# current
    btnclick("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    btnclick("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button")
>>>>>>> Stashed changes
