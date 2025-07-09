from selenium import webdriver
from selenium.webdriver.common.by import By
#keeping chrom browser open
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# #Finding element by class
# # price_dollar=driver.find_element(By.CLASS_NAME,value="a-price-whole").text
# # price_cents=driver.find_element(By.CLASS_NAME,value="a-price-fraction").text
# # print(f"The price is {price_dollar}.{price_cents}")
#
# #Gives the field name
# #Finding element By name
# search_bar=driver.find_element(By.NAME,value="q")
# print(search_bar.tag_name)
# print(search_bar.get_property("placeholder"))
#
#
# #Finding element by ID
# button=driver.find_element(By.ID,value="submit")
# print(button.size)
#
#
# #Finding element by CSS Selectors
# documentation_link=driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documentation_link.text)
#
# #Finding element By XPATH
# bug_link=driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# #Close a particular tab
# # driver.close()
# # #Close the entire Chrome browser
# driver.quit()
#


#Practice Question1


dates=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
# for date in dates:
#     print(date.text)




event_name=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
# for event in event_name:
#     print(event.text)

events={}

for n in range(len(dates)):
    events[n]={
        "time":dates[n].text,
        "event":event_name[n].text
    }

print(events)




driver.quit()