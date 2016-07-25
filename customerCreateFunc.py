import random

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import createCusData

from customerHelper import RandomHelper
randValue = RandomHelper()



class HelpFunctionForCustomerCreate():
    def stringAction(self, driver, reqValue):
        helpName = randValue.random_string_generator()
        helpName = helpName[reqValue:]
        return helpName.upper()

    def intAction(self, driver, reqValue):
        helpIntValue = randValue.random_int_generator()
        helpIntValue = helpIntValue[reqValue:]
        return helpIntValue



helpFunc = HelpFunctionForCustomerCreate()

class CustomerCreateFunc(HelpFunctionForCustomerCreate):
    helpFunc = HelpFunctionForCustomerCreate()


    def login(self, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable((By.XPATH, createCusData.loginButton)))
        driver.find_element_by_xpath(createCusData.emailField).send_keys(createCusData.emailData)
        driver.find_element_by_xpath(createCusData.passwordField).send_keys(createCusData.passwordData)
        driver.find_element_by_xpath(createCusData.loginButton).click()




    def fillCustomerName(self, driver):
        driver.implicitly_wait(10)
        helpName = helpFunc.stringAction(driver, 6)
        driver.find_element_by_xpath(createCusData.customerNameInput).send_keys(createCusData.customerName + helpName)
        return createCusData.customerName + helpName



    def selecShipAddress(self, driver):
        select  = Select(driver.find_element_by_xpath(createCusData.cutomerAddressDD))
        select.select_by_visible_text("Shipping Addresses")




    def fillAddressAndCity(self, driver):
        helpShipAddress = helpFunc.stringAction(driver, 6)
        helpInt = helpFunc.intAction(driver, 7)
        driver.find_element_by_xpath(createCusData.addressLine).send_keys("ship_address_" + helpShipAddress + " " + helpInt)

        helpCity = helpFunc.stringAction(driver, 6)
        driver.find_element_by_xpath(createCusData.cityLine).send_keys("City_" + helpCity)




    def selectCountryInShipAddress(self, driver):
        driver.find_element_by_xpath(createCusData.countryDD2ShipAddress).click()
        allCountries = driver.find_elements_by_xpath(createCusData.allCountiesInDD2)
        randCountry = random.choice(allCountries).text
        driver.find_element_by_xpath(createCusData.countryDD2ShipAddressInputField).send_keys(randCountry)
        driver.find_element_by_xpath(createCusData.selectedContryNotif).click()




    def selectShippingConditions(self, driver):
        select = Select(driver.find_element_by_xpath(createCusData.shippingConditionsDD2))
        a = [o.get_attribute('text') for o in select.options]
        randomText = (random.choice(a))
        select.select_by_visible_text(randomText)
        if randomText == 'Minimum order value':

            intMin = range(0, 100)
            varForMovMinimum = random.choice(intMin)
            driver.find_element_by_xpath(createCusData.min).send_keys(varForMovMinimum)
            intMax = range(101, 200)
            varForMaxValue = random.choice(intMax)
            driver.find_element_by_xpath(createCusData.maximum).send_keys(varForMaxValue)
            intShipCosts = range(200, 400)
            varFoxShipCosts = random.choice(intShipCosts)
            driver.find_element_by_xpath(createCusData.shipCost).send_keys(varFoxShipCosts)
            intFreeFrom = range(100, 300)
            varForFreeFrom = random.choice(intFreeFrom)
            driver.find_element_by_xpath(createCusData.freeShipFrom).send_keys(varForFreeFrom)

        elif randomText == 'Item based shipping (price per item)':
            intPerItem = range(100, 200)
            pricePerItem = random.choice(intPerItem)
            driver.find_element_by_xpath(createCusData.pricePerItem).send_keys(pricePerItem)

        elif randomText == 'Flat fee per order':
            intFlatFeePerOrder = range(10, 100)
            flatFee = random.choice(intFlatFeePerOrder)
            driver.find_element_by_xpath(createCusData.flatFee).send_keys(flatFee)

        elif randomText == 'Item based shipping and flat fee per order':
            intPerItemSecond = range(10, 200)
            pricePerItemSecond = random.choice(intPerItemSecond)
            driver.find_element_by_xpath(createCusData.pricePerItemFF).send_keys(pricePerItemSecond)
            intFlatFeeSecond = range(50, 100)
            flatFeeSecond = random.choice(intFlatFeeSecond)
            driver.find_element_by_xpath(createCusData.flatFeePPI).send_keys(flatFeeSecond)




    def fillContactName(self, driver):
        driver.find_element_by_xpath(createCusData.contactInfoArrow).click()
        helpName = helpFunc.stringAction(driver, 6)
        driver.find_element_by_xpath(createCusData.contactNameInput).send_keys("Contact_name_" + helpName)




    def fillContactPhone(self, driver):
        driver.find_element_by_xpath(createCusData.contactPhoneInput).send_keys(randValue.random_int_generator())




    def fillEmail(self, driver):
        helpEmail = helpFunc.stringAction(driver, 5)
        driver.find_element_by_xpath(createCusData.contactEmailInput).send_keys("contact_email_" + helpEmail +
                                                                                "@gmail.com")
        return "contact_email_" + helpEmail +"@gmail.com"




    def clickOnCreateButton(self, driver):
        driver.find_element_by_xpath(createCusData.createButton).click()




    def notificationAfterCreateCustomer(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, createCusData.notificationAfterCreateCustomer),
                                                    "Customer was successfully saved."))
        return driver.find_element_by_xpath(createCusData.notificationAfterCreateCustomer).text








