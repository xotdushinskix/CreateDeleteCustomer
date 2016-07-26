import unittest
import createCusData
from selenium import webdriver


from customerCreateFunc import CustomerCreateFunc
from customersPage import CustomerPage
from textFileWorker import FileWorker


custCreateFunc = CustomerCreateFunc()
custListPage = CustomerPage()
fileWorker = FileWorker()

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(createCusData.createCustomerURL)


    def tearDown(self):
        self.driver.close()


class TestCreateAndDeleteCustomer(MyTestCase):

    def testCustomerCreate(self):
        driver = self.driver

        custCreateFunc.login(driver)

        custCreateFunc.fillCustomerName(driver)

        custCreateFunc.selecShipAddress(driver)

        custCreateFunc.fillAddressAndCity(driver)

        custCreateFunc.selectCountryInShipAddress(driver)

        custCreateFunc.selectShippingConditions(driver)

        custCreateFunc.fillContactName(driver)

        custCreateFunc.fillContactPhone(driver)

        custCreateFunc.fillEmail(driver)

        custCreateFunc.clickOnCreateButton(driver)

        succesNotifAfterCreateCustomer =  custCreateFunc.notificationAfterCreateCustomer(driver)
        self.assertEquals(succesNotifAfterCreateCustomer, "Customer was successfully saved.")




    def testCustomerDelete(self):
        driver = self.driver

        driver.get(createCusData.customerGrid)

        custCreateFunc.login(driver)

        allCustomers = custListPage.getAllCustomers(driver)
        self.assertIn(fileWorker.customerName(), allCustomers)

        allCustomersEmail = custListPage.getAllEmails(driver)
        self.assertIn(fileWorker.customerEmail(), allCustomersEmail)

        custListPage.searchCreatedCustomer(driver, fileWorker.customerName())

        custListPage.deleteCreatedCustomer(driver)

        succesNotifAfterDeleteCustomer = custListPage.notificationAfterDeleteCustomer(driver)
        self.assertEquals(succesNotifAfterDeleteCustomer, "Customer was successfully removed.")

        driver.get(createCusData.customerGrid)

        allCustomers = custListPage.getAllCustomers(driver)
        self.assertNotIn(fileWorker.customerName(), allCustomers)

        allCustomersEmail = custListPage.getAllEmails(driver)
        self.assertNotIn(fileWorker.customerEmail(), allCustomersEmail)



if __name__ == '__main__':
    unittest.main()
