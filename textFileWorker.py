class FileWorker():

    def customerName(self):
        nameFile = open("cust_name.txt")
        customerName = nameFile.read()
        return customerName

    def customerEmail(self):
        nameFile = open("cust_email.txt")
        customerEmail = nameFile.read()
        return customerEmail