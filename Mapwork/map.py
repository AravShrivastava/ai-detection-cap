import datetime
from ssl import Options
from tokenize import Double
import pyttsx3
import speech_recognition
import requests
import bs4
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("C:\chromedriver")
driver.get("https://www.google.com/maps/@23.232512,77.430784,12z")

def searchplace():
 place = driver.find_element(by=By.CLASS_NAME, value=("tactile-searchbox-input"))
 place.send_keys('Kanha Funcity') 
 submit = driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button"))
 submit.click()
 sleep(2)

def direction():
        sleep(2)
        direction= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button"))
        direction.click()
        sleep(2)

        

def find():
            sleep(2)
            find= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input"))
            find.send_keys("D mart") 
            search_btn= driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]"))
            search_btn.click()
            walk = driver.find_element(by=By.XPATH, value=("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button"))
            walk.click()
            


       
searchplace()
direction()
find()