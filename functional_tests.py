from selenium import webdriver
from pyvirtualdisplay import Display
xephyr=Display(visible=1, size=(320, 240)).start()

driver = webdriver.Firefox()
print "opened"
driver.get("https://www.google.com")
print "found"
driver.close()
print "closed"
