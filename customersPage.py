from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import createCusData


class HelpForCustomerPage():
    def getAllItems(self, driver, itemsOnGrid):
        allItems = driver.find_elements_by_xpath(itemsOnGrid)
        allItemsText = []
        for i in allItems:
            textName = i.text
            allItemsText.append(textName)
        return allItemsText



helpFuncForCustPage = HelpForCustomerPage()

class CustomerPage():
    def getAllCustomers(self, driver):
        return helpFuncForCustPage.getAllItems(driver, createCusData.allCustomersNameOnGrid)

    def getAllEmails(self, driver):
        return helpFuncForCustPage.getAllItems(driver, createCusData.allCustomersEmailOnGrid)


    def searchCreatedCustomer(self, driver, requiredName):
        driver.find_element_by_xpath(createCusData.searchButtonOnCustomerListPage).click()
        driver.find_element_by_xpath(createCusData.customerNameInputOnSearchGrid).send_keys(requiredName)
        driver.find_element_by_xpath(createCusData.searchButtonOnSearchGrid).click()


    def deleteCreatedCustomer(self, driver):
        driver.find_element_by_xpath(createCusData.deleteButtonOnGrid).click()
        driver.find_element_by_xpath(createCusData.applyDelete).click()


    def notificationAfterDeleteCustomer(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.XPATH, createCusData.notificationAfterDelete),
                                                    "Customer was successfully removed."))
        return driver.find_element_by_xpath(createCusData.notificationAfterDelete).text