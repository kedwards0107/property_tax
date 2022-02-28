import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml
#import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd

#street_name is set manually as only 2 streets being evaluated
street_name = ("XXXX")
#street number is iterated through using address_all list
address_all = []
for i in range(103, 144, 2):
    address_all.append(i)

# removes any numbers in range that have been found to be missing or invalid
address_all.remove(141)
#address_all.remove(250)
# to add additional street numbers 
# for i in range (123, 236, 2):
#     address_all.append(i)
#print(address_all)

# webdriver launches chrome and inputs website address
driver = webdriver.Chrome()
driver.get("http://www.XXXXXXXXX")

# clicks through home screen "Agree" acknowledgement
searchButton = driver.find_element_by_xpath('//*[@id="btAgree"]')
searchButton.click()
# selects "Property Address" tab
address_tab = driver.find_element_by_xpath('//*[@id="thebody"]/table/tbody/tr[1]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/a')
address_tab.click()

searchbox_no = driver.find_element_by_xpath('//*[@id="inpNumber"]')
searchbox_no.send_keys('101')

searchbox_street = driver.find_element_by_xpath('//*[@id="inpStreet"]')
searchbox_street.send_keys(street_name)

search_tab = driver.find_element_by_xpath('//*[@id="btSearch"]')
search_tab.click()

parcel_tab = driver.find_element_by_xpath('//*[@id="searchResults"]/tbody/tr[3]/td[2]')
parcel_tab.click()

summary_tab = driver.find_element_by_xpath('//*[@id="lbPrintAll"]')
summary_tab.click()

window_before = driver.window_handles[0]
window_after = driver.window_handles[1]

driver.switch_to.window(window_after)
time.sleep(5)

p_tab = driver.current_url
#print(p_tab)

driver.quit()

header_info = []
det_info = []
result = requests.get(p_tab)

src = result.content
soup = BeautifulSoup(src, 'lxml')
parcel = soup.find('div')
parcel_info = parcel.find('table',id="Parcel")
for inds in parcel_info.find_all('td', class_='DataletSideHeading'):
    parcel_ind = inds.text
    header_info.append(parcel_ind)

parcel = soup.find('table')
parcel_info = parcel.find('table', id="Residential")
for setts in parcel_info.find_all('td', class_='DataletSideHeading'):
    sett_ind = setts.text
    header_info.append(sett_ind)

parcel = soup.find('table')
parcel_info = parcel.find('table', id="Sale Details")
for setts in parcel_info.find_all('td', class_='DataletSideHeading'):
    sett_ind = setts.text
    header_info.append(sett_ind)

parcel = soup.find('table')
parcel_info = parcel.find('table', id="Estimated Tax Information")
for inds in parcel_info.find_all('td', class_='DataletSideHeading'):
    parcel_ind = inds.text
    header_info.append(parcel_ind)

parcel = soup.find('div')
parcel_info = parcel.find('table',id="Parcel")
for dets in parcel_info.find_all('td',class_='DataletData'):
    det = dets.text
    det_info.append(det)

parcel = soup.find('table')
parcel_info = parcel.find('table', id="Residential")
for dets in parcel_info.find_all('td',class_='DataletData'):
    det = dets.text
    det_info.append(det)

parcel = soup.find('table')
parcel_info = parcel.find('table', id="Sale Details")
for dets in parcel_info.find_all('td',class_='DataletData'):
    det = dets.text
    det_info.append(det)

parcel = soup.find('table')
parcel_info = parcel.find('table', id="Estimated Tax Information")
for dets in parcel_info.find_all('td',class_='DataletData'):
    det = dets.text
    det_info.append(det)

df = pd.DataFrame([header_info, det_info],)
print(df)

time.sleep(5)

for i in address_all:
    driver = webdriver.Chrome()
    driver.get("http://www.XXXXX")

    searchButton = driver.find_element_by_xpath('//*[@id="btAgree"]')
    searchButton.click()
    address_tab = driver.find_element_by_xpath('//*[@id="thebody"]/table/tbody/tr[1]/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/a')
    address_tab.click()
    result = requests.get('http://www.XXXXX')

    searchbox_no = driver.find_element_by_xpath('//*[@id="inpNumber"]')
    searchbox_no.send_keys(i)

    searchbox_street = driver.find_element_by_xpath('//*[@id="inpStreet"]')
    searchbox_street.send_keys(street_name)

    search_tab = driver.find_element_by_xpath('//*[@id="btSearch"]')
    search_tab.click()

    parcel_tab = driver.find_element_by_xpath('//*[@id="searchResults"]/tbody/tr[3]/td[2]')
    parcel_tab.click()

    summary_tab = driver.find_element_by_xpath('//*[@id="lbPrintAll"]')
    summary_tab.click()

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]

    driver.switch_to.window(window_after)
    time.sleep(5)

    p_tab = driver.current_url
    print(p_tab)

    #driver.quit()
    result = requests.get(p_tab)

    det_info = []

    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    parcel = soup.find('div')
    parcel_info = parcel.find('table',id="Parcel")
    for dets in parcel_info.find_all('td',class_='DataletData'):
        det = dets.text
        det_info.append(det)

    parcel = soup.find('table')
    parcel_info = parcel.find('table', id="Residential")
    for dets in parcel_info.find_all('td',class_='DataletData'):
        det = dets.text
        det_info.append(det)

    parcel = soup.find('table')
    parcel_info = parcel.find('table', id="Sale Details")
    for dets in parcel_info.find_all('td',class_='DataletData'):
        det = dets.text
        det_info.append(det)

    parcel = soup.find('table')
    parcel_info = parcel.find('table', id="Estimated Tax Information")
    for dets in parcel_info.find_all('td',class_='DataletData'):
        det = dets.text
        det_info.append(det)

    new_info = pd.Series(det_info,)#index = df.columns
    df = df.append(new_info, ignore_index=True)
    print(df)

df.to_csv(r'/Users/mack/Desktop/export_dataframe.csv',index=False)
time.sleep(5)
