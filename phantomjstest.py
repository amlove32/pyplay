#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# VARIABLES && ELEMENTS
# testSite = "https://developer.service-now.com"
signOnPage = "https://signon.service-now.com/ssologin.do?RelayState=%2F%2Fapp%2Ftemplate_saml_2_0%2Fk317zlfESMUHAFZFXMVB%2Fsso%2Fsaml%3FSAMLRequest%3DnZPdbuIwEIVfJfI9%252BQOWxSJIKSwqUulGQKtVb5BrT1qrjp31OED36TcJtHCxpdXeer7MnDlnMkJWqLikaeWe9RJ%252BV4DO2xdKIz1UElJZTQ1DiVSzApA6Tlfp4obGfkhLa5zhRhEvRQTrpNETo7EqwK7AbiWHu%252BVNQp6dK5EGgYAtKFOC9fFQ1Wbnc1MQb1rPlZo1DU74CUL5pI32zYtjDR%252BwsgwcFKViDjaN0E28CYOXbjT4o%2FIfq8XddTp7mP1a3F8FiCZoCOLNjOXQLpqQnCkE4s2nCVndTvo85lFPMJHH%2FWGvO8g5sHBYP3zP%252B71H0a9BzBii3MLpU8QK5hod0y4hcRgNOuGwE4Xr6Bvt9mi37w%252BGwwfiZUeLrqQWUj9d9vPxACG9Xq%252BzTvZztW4bbKUAe1vTX7HyHiy2NtYNyXjUxkhbtfY82ctC2FucZPxpGqPgfMZxYkkbvfNpZpTkr16qlNlNLNR5JcTZCto4CuY%252BlhH5UfsiRSdvUQoFkyoVwgIiCd4HHc8WRJttfX8O9s6bmKJkVmLjBOwZd%252B9enGMTVW%252B6hPy%2FnLmIccqb3vVzczk7Y0VzCcBrnWvLNJbGujfn%2FqVofCx%252BsN%252BpfP7rjv8C%26RelayState%3Dhttps%3A%2F%2Fdeveloper.servicenow.com%2Fsaml_redirector.do%253Fsysparm_nostack%253Dtrue%2526sysparm_uri%253D%25252Fnav_to.do%25253Furi%25253D%2525252Fssologin.do%2525253FrelayState%2525253D%252525252Fapp.do%2525252523%21%252525252Fdashboard&redirectUri=&email="
loginTitle = "SIGNON"
loginEmail = "thisisme@gmail.com"


# find_element_by_id IDs
LOGIN_LINK = "dp-hdr-login-link"
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
SIGNIN_BUTTON = "submitButton"
INSTANCE_LINK = "dp-hdr-br-link-instance"
EXTEND_BUTTON = "hp-instance-extend-button-parent"

# FIRE UP PHANTOMJS SELENIUM HEADLESS WEBDRIVER
def fireUpPhantomJSPage(pageUrl):
    """
    Requires page URL param.  Starts PhantomJS and opens that page.
    """
    driver.set_window_size(800, 600) # I don't really need this, but it makes it look prettier in screenshots.
    driver.get(pageUrl)

def GetScreenShot(pageTitle, i):
    """
    int(i):  Increment required for the screenshot filename in numerical order.
    str(pageTitle):  The name you want to give the page for logging purposes.
    """
    # pageTitle = str(pageTitle)
    # i = int(i)
    if i < 10:      # to add a 0 before the i in the filename, because two digit ordering
        snapShotFileName = "screen0{0}.png".format(str(i))
    else:           # to NOT add a 0 in the filename for two digit ordering
        snapShotFileName = "screen{0}.png".format(str(i))
    driver.save_screenshot(snapShotFileName)
    # consoleLogSnapShot = "Grabbed screenshot {0} of {1}: {2}".format(str(i), pageTitle, snapShotFileName)
    print("Grabbed screenshot {0} of {1} page: {2}".format(str(i), str(pageTitle), str(snapShotFileName)))
    return i + 1

snapShotNumber = 0 # initializer
driver = webdriver.PhantomJS() # or add to PATH.
print("Opening the test homepage with PhantomJS.")
fireUpPhantomJSPage(signOnPage)
snapShotNumber = GetScreenShot("index page", snapShotNumber) # get the first screenshot of the index page

print("Logging in the test user.")
driver.find_element_by_id(USERNAME_FIELD).send_keys(loginEmail)
driver.find_element_by_id(PASSWORD_FIELD).send_keys(loginPassword)
driver.find_element_by_id(PASSWORD_FIELD).send_keys(u'\ue007')
wait = WebDriverWait(driver, 30)
snapShotNumber = GetScreenShot("logged in user page", snapShotNumber) # we should be logged in now

print("Navigate to the manage instance page.")
instanceLink = driver.find_element_by_id(INSTANCE_LINK)
instanceLink.click()
snapShotNumber = GetScreenShot("manage instance page", snapShotNumber)

print("Extend the test instance.")
extendButton = driver.find_element_by_id(EXTEND_BUTTON)
extendButton.click()
snapShotNumber = GetScreenShot("extended instance confirmation page", snapShotNumber)

print("Quitting the browser.")
driver.quit()




if __name__ == "__main__":
    unittest.main()


# DO THE WORK
# class PythonOrgSearch(unittest.TestCase):
# driver.save_screenshot('screen01.png') #index page
# logInLink = driver.find_element_by_id(LOGIN_LINK)
# logInLink.click()
# signinButton = driver.find_element_by_id(SIGNIN_BUTTON)
# signinButton.click()
