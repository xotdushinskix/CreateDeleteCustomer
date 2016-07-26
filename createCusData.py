createCustomerURL = "http:/.com/users/createcustomer"
customerGrid = "http:/.com/users/customerlist"


emailField = '//*[@id="UserLogin_username"]'
emailData = "admin"
passwordData = "admin"
passwordField = '//*[@id="UserLogin_password"]'
loginButton = ".//*[@id='yw0']//div[5]/input"


customerNameInput = ".//*[@id='Customer_customer_name']"
customerName = "Customer_"
cutomerAddressDD = ".//*[@id='Customer_addresses']"
addressLine = ".//*[@id='Customer_shipping_addresses_address_line']"
cityLine = ".//*[@id='Customer_shipping_addresses_city']"
countryDD2ShipAddress = ".//*[@id='select2-Customer_shipping_addresses_shipping_country-container']"
allCountiesInDD2 = ".//*[@id='select2-Customer_shipping_addresses_shipping_country-results']//li"
countryDD2ShipAddressInputField = '//input[@class="select2-search__field"]'
selectedContryNotif = '//li[@class="select2-results__option select2-results__option--highlighted"]'


shippingConditionsDD2 = ".//*[@id='Customer_shipping_conditions']"
#minOrderValue:
min = ".//*[@id='Customer_mov_min']"
maximum = ".//*[@id='Customer_mov_max']"
shipCost = ".//*[@id='Customer_mov_shipping_costs']"
freeShipFrom = ".//*[@id='Customer_free_shipping']"
#Item based shipping
pricePerItem = ".//*[@id='Customer_price_per_item']"
#Flat fee per order
flatFee = ".//*[@id='Customer_flat_fee']"
#Item based shipping and flat fee per order
pricePerItemFF = ".//*[@id='Customer_price_per_item']"
flatFeePPI = ".//*[@id='Customer_flat_fee']"


contactInfoArrow = './/div[@class="enableContact glyphicon glyphicon-chevron-down"]'
contactNameInput = ".//*[@id='Customer_contacts_contact_name']"
contactPhoneInput = ".//*[@id='Customer_contacts_contact_phone']"
contactEmailInput = ".//*[@id='Customer_contacts_contact_email']"


createButton = '//button[@class="controlling_buttons save_form btn btn-success"]'


notificationAfterCreateCustomer = './/div[@class="noty_message"]'


allCustomersNameOnGrid = ".//*[@id='customer-grid']/table[2]//td[2]"
allCustomersEmailOnGrid = ".//*[@id='customer-grid']/table[2]//td[4]"


searchButtonOnCustomerListPage = './/button[@class="search_button btn btn-gepard-wide btn-gepard-default btn-default"]'
customerNameInputOnSearchGrid = ".//*[@id='Customer_customer_name']"
searchButtonOnSearchGrid = ".//button[@id='search-button-customer-grid']"


deleteButtonOnGrid = './/i[@class="fa fa-trash-o fa-lg"]'
applyDelete = ".//*[@id='button-0']"
notificationAfterDelete = './/div[@class="noty_message"]'
