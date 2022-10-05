import datetime
from tokenize import Double
import pyttsx3
import speech_recognition
import requests
import bs4
import selenium 
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")  # to open the chromebrowser
driver.get("https://www.google.com/maps/@23.232512,77.430784,12z")
sleep(2)

def searchplace():
    place = driver.find_element_by_class_name("tactile-searchbox-input" )
    place.send_keys("Funcity")
    submit= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()

    searchplace()

    def direction():
        sleep(6)
        direction= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")

        direction.click()

        direction()

        def find():
            sleep(5)
            find= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
            find.send_keys("D mart")
            search_btn= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
            search_btn.click()

            find()


