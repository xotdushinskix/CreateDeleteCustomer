import unittest
import createCusData
from selenium import webdriver

from customerCreateFunc import CustomerCreateFunc
from customersPage import CustomerPage


custCreateFunc = CustomerCreateFunc()
custListPage = CustomerPage()

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(createCusData.createCustomerURL)


    def tearDown(self):
        self.driver.close()


class TestCreateAndDeleteCustomer(MyTestCase):

    def testCustomerCreateAndDelete(self):
        driver = self.driver

        custCreateFunc.login(driver)

        customerName = custCreateFunc.fillCustomerName(driver)

        custCreateFunc.selecShipAddress(driver)

        custCreateFunc.fillAddressAndCity(driver)

        custCreateFunc.selectCountryInShipAddress(driver)

        custCreateFunc.selectShippingConditions(driver)

        custCreateFunc.fillContactName(driver)

        custCreateFunc.fillContactPhone(driver)

        customerEmail = custCreateFunc.fillEmail(driver)

        custCreateFunc.clickOnCreateButton(driver)

        succesNotifAfterCreateCustomer =  custCreateFunc.notificationAfterCreateCustomer(driver)
        self.assertEquals(succesNotifAfterCreateCustomer, "Customer was successfully saved.")

        driver.get(createCusData.customerGrid)

        allCustomers = custListPage.getAllCustomers(driver)
        self.assertIn(customerName, allCustomers)

        allCustomersEmail = custListPage.getAllEmails(driver)
        self.assertIn(customerEmail, allCustomersEmail)

        custListPage.searchCreatedCustomer(driver, customerName)

        custListPage.deleteCreatedCustomer(driver)

        succesNotifAfterDeleteCustomer = custListPage.notificationAfterDeleteCustomer(driver)
        self.assertEquals(succesNotifAfterDeleteCustomer, "Customer was successfully removed.")

        driver.get(createCusData.customerGrid)

        allCustomers = custListPage.getAllCustomers(driver)
        self.assertNotIn(customerName, allCustomers)

        allCustomersEmail = custListPage.getAllEmails(driver)
        self.assertNotIn(customerEmail, allCustomersEmail)




if __name__ == '__main__':
    unittest.main()
