from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def isDollarVal(char):
    if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "." or char == "$":
        return True
    else:
        return False

def printMinMax(nameList,priceList):
    maxPrice = -99999
    maxName = ""
    minPrice = 99999
    minName = ""
    avrgPrice = 0

    for index in range(len(nameList)):
        avrgPrice += priceList[index]
        if priceList[index] > maxPrice:
            maxPrice = priceList[index]
            maxName = nameList[index]
        if priceList[index] < minPrice:
            minPrice = priceList[index]
            minName = nameList[index]

    avrgPrice = avrgPrice / len(nameList)

    print()
    print("Average Price")
    print("=============")
    print("$"+str(avrgPrice))
    print()
    print("Maximum")
    print("=======")
    print(maxName + " Sold For: $" + str(maxPrice))
    print()
    print("Minimum")
    print("=======")
    print(minName + " Sold For: $" + str(minPrice))

# Entry point
mainMenuLoop = True
while(mainMenuLoop):
    print()
    print("=========")
    print("Main Menu")
    print("=========")
    print("1. Analyze Sold Listings")
    print("2. Analyze Live Listings")
    choice = input("Enter Selection: ")
    print()
    if choice == '1' or choice == '2':
        mainMenuLoop = False


print("What Item would you like to gather info about?")
itemName = input("Item:  ")
print()

# Driver Set up
chromeOptions = Options()
# chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"C:\Users\7stre\Desktop\Sean\Programming\chromedriver" # Must be the path conatining chromdrive.exe
driver = webdriver.Chrome(chrome_driver, options=chromeOptions)
driver.implicitly_wait(10) # the driver will wait up to 10 seconds for each element to apppear on the page before throwing an error

if choice == '1':
    ebayAdvancedSearchLink = "https://www.ebay.com/sch/ebayadvsearch?mkevt=1&mkcid=1&mkrid=711-53200-19255-0&campid=5337590774&customid=&toolid=10001"
    driver.get(ebayAdvancedSearchLink)

    elem = driver.find_element_by_name("_nkw")
    elem.send_keys(itemName)

    elem = driver.find_element_by_name("LH_Sold")
    elem.send_keys(Keys.SPACE)

    elem = driver.find_element_by_class_name("btn-prim")
    elem.send_keys(Keys.RETURN)

    soldListingNames = driver.find_elements_by_class_name("vip")
    soldListingPrices = driver.find_elements_by_class_name("bidsold")

    nameList = []
    priceList = []

    for index in range(len(soldListingNames)):
        priceString = soldListingPrices[index].get_attribute("innerHTML") # Inner html of price might not only contain the price
        price = priceString.split("$")[1] # The price is split after the $
        tempPrice = ""

        for char in price:
            if isDollarVal(char):
                tempPrice += char

        nameList.append(soldListingNames[index].get_attribute("innerHTML")) # Add the title to the nameList
        priceList.append(float(tempPrice)) # Add the price to the price list

    printMinMax(nameList,priceList)

if choice == '2':
    ebayAdvancedSearchLink = "https://www.ebay.com/sch/ebayadvsearch?mkevt=1&mkcid=1&mkrid=711-53200-19255-0&campid=5337590774&customid=&toolid=10001"
    driver.get(ebayAdvancedSearchLink)

    elem = driver.find_element_by_name("_nkw")
    elem.send_keys(itemName)

    elem = driver.find_element_by_class_name("btn-prim")
    elem.send_keys(Keys.RETURN)

    currListingNames = driver.find_elements_by_class_name("vip")
    parentElement = driver.find_element_by_class_name("prc")
    currListingPrices = parentElement.find_elements_by_tag_name("span")

    nameList = []
    priceList = []

    for index in range(len(currListingPrices)):
        priceString = currListingPrices[index].get_attribute("innerHTML") # Inner html of price might not only contain the price
        print(currListingPrices[index].get_attribute("innerHTML"))
        price = priceString.split("$")[1] # The price is split after the $
        tempPrice = ""

        for char in price:
            if isDollarVal(char):
                tempPrice += char

        nameList.append(currListingNames[index].get_attribute("innerHTML")) # Add the title to the nameList
        priceList.append(float(tempPrice)) # Add the price to the price list

    printMinMax(nameList,priceList)

"""
for index in range(len(nameList)):
    print(nameList[index] + " " + str(priceList[index]))
"""
