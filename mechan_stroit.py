from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common import by

driver = webdriver.Firefox()
driver.get('http://ms.enjournal.net/archive')
assert "Архив номеров" in driver.page_source
#driver.find_elements_by_link_text("Архив номеров")

#spisok = driver.find_element_by_xpath("//[@class='post']")
#div = self.driver.find_element_by_class_name('post')
#t = driver.find_element(By.ID('content').find_element(By.TAG_NAME('p')))
# t = driver.find_element_by_xpath('//*[@id="content"]/*[@class="post"]/p')
# m = t.find_elements_by_tag_name('a')
elem = driver.find_elements_by_xpath('//*[@id="content"]/*[@class="post"]/p/*[@href]')
#titles = [x.text for x in elem]
#url = elem.get_attribute("href")
#t = driver.find_element_by_id("content")
table_years = driver.find_element_by_class_name('issues')
links_years = table_years.find_elements_by_tag_name('a')
list_linkyears = []
spisok = []
for i in elem:
    stroki = i.get_attribute('href')
    spisok.append(stroki)
print(spisok)

for i in links_years:
    if i.text:
        new_stroki = i.get_attribute('href')
        list_linkyears.append(new_stroki)
print(list_linkyears)


full_listmonth = []
for i in spisok[28:]:
    new_driver = webdriver.Firefox()
    new_driver.get(i)
    table = new_driver.find_element_by_class_name('issues')
    after_table = table.find_elements_by_tag_name('a')
    for j in after_table:
        if j.text:
            links = j.get_attribute('href')
            full_listmonth.append(links)
    new_driver.close()
print(full_listmonth)


links_articles = []
for t in full_listmonth:
    new_driver_art = webdriver.Firefox()
    new_driver_art.get(t)
    center = new_driver_art.find_element_by_class_name('issue')
    after_center = center.find_elements_by_xpath('//b/a')
    for y in after_center:
        if y.text:
            wh = y.get_attribute('href')
            links_articles.append(wh)
    new_driver_art.close()
print(links_articles)


#print(i.get_attribute('href')[1:3])

driver.quit()