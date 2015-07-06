from selenium import webdriver

driver = webdriver.Firefox()
print "opened"
driver.get("https://www.google.com")
print "found"
driver.close()
print "closed"
