import sys
import os
import time
from selenium import webdriver

folder_name = str(sys.argv[1])
username = str(sys.argv[2])
password = str(sys.argv[3])


path = "/home/yshgpta/Desktop/MyProjects/"  #Your project folder path
path_of_chrome_driver = '/home/yshgpta/Downloads/chromedriver/chromedriver'  #Your chromedriver path

browser = webdriver.Chrome(path_of_chrome_driver)
browser.get('http://www.github.com/login')

def create():
    try:
        os.mkdir(path+folder_name)
    except OSError:
        print ("Creation of the directory %s failed" % path+folder_name)
    else:
        print ("Successfully created the directory %s " % path+folder_name)
    python_button = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    python_button.click()
    python_button.send_keys(username)
    python_button = browser.find_elements_by_xpath("//*[@id='password']")[0]
    python_button.click()
    python_button.send_keys(password)
    sign_in_button = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[8]")[0]
    sign_in_button.click()
    new_repo = browser.find_elements_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a")[0]
    new_repo.click()
    set_repo = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    set_repo.click()
    set_repo.send_keys(folder_name)
    time.sleep(1)
    create_repo_button = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    create_repo_button.click()

if __name__ == "__main__":
    create()