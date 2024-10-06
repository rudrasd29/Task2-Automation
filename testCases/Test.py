from selenium.webdriver.support.wait import WebDriverWait
from utils.readProperties import ReadProperties
from utils.customLogger import logGen
from pageObjects.HomePage import HomePage as homePage

class Test_sign_document:
    baseUrl = ReadProperties.getBaseUrl()
    logger = logGen.loggen()

    def test_TC001_verify_title(self, setup):
        self.logger.info("**************TC001_title is started****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actualTitle = self.driver.title
        expectedTitle = 'Scrive'
        if actualTitle == expectedTitle:
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "TC001_title_Homepage.png")
            assert False
        self.logger.info("**************TC001_title is finished***************")

    def test_TC002_capture_confirmation_modal_screenshot(self, setup):
        self.logger.info("**************TC002_capture_confirmation_modal_screenshot is started**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        name = str(ReadProperties.getData_Name())
        homePage(self.driver).enter_name(name)
        homePage(self.driver).click_next_btn()
        homePage(self.driver).screenshot()
        self.logger.info("**************TC002_capture_confirmation_modal_screenshot is finished**************")

    def test_TC003_verify_document_signed(self, setup):
        self.logger.info("**************TC003_verify_document_signed**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        name = str(ReadProperties.getData_Name())
        homePage(self.driver).enter_name(name)
        homePage(self.driver).click_next_btn()
        WebDriverWait(self.driver, 10)
        homePage(self.driver).click_sign_btn()
        element_text = homePage(self.driver).label_document_sign()
        WebDriverWait(self.driver, 10)
        if element_text == 'Document signed!':
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "TC003_Failed_document_signed.png")
            self.logger.error("*************Document is not signed******************")
            assert False
        self.logger.info("**************TC003_verify_document_signed is finished**************")