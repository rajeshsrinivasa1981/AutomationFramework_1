from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


from Frameworks.Pages.Loginpage import Loginpage
from Frameworks.Pages.Homepage import Homepage
from Frameworks.utils import utils
class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self,test_setup):
        driver.get(utils.URL)

        login = Loginpage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()


    def test_logout(self,test_setup):
        # try:
         homepage = Homepage(driver)
         homepage.click_welcome()
         homepage.click_logout()
            # driver.find_element_by_id("welcome").click()
            # driver.find_element_by_link_text("Logout").click()
        #     x = driver.title
        #     assert x == "abc"
        # except AssertionError as error:
        #     print("Assertion error occurred")
        #     print(error)
        #     raise
        #
        # except:
        #     print("some exception occured")
        #
        # else:
        #     print("No exceptions occured")
        #
        # finally:
        #     print("this block will always execute")
        #






