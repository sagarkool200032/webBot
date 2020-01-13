from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstaBot:
    def __init__(self,username,pwd):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a""").click()
        sleep(3)
        self.driver.find_element_by_xpath\
        ("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input""").send_keys(username)
        self.driver.find_element_by_xpath\
        ("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input""").send_keys(pwd)
        self.driver.find_element_by_xpath\
        ("""//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div""").click()
        sleep(3)
        self.driver.find_element_by_class_name("HoLwm").click()
        sleep(3)

    def followers(self):
        self.driver.find_element_by_xpath\
        ("""//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a""").click()
        sleep(3)
        self.driver.find_element_by_xpath\
        ("""//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a""").click()
        sleep(3)

#         For Suggestions
#         sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
#         self.driver.execute_script('arguments[0].scrollIntoView()', sugs)

        followers = self._getNames_()
        print(followers)
        print("\n\n")

    def following(self):
        self.driver.find_element_by_xpath\
        ("""//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a""").click()
        sleep(3)
        following = self._getNames_()
        print(following)
        print("\n\n")

    def _getNames_(self):
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;""", scroll_box)

        links = scroll_box.find_elements_by_tag_name("a")
        names = [x.text for x in links if(x.text!=" " and x.text!="")]
        scroll_box.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names

    def close(self):
        self.driver.close()

# creating an instance of the class and calling its functions
# replace userId and password with user's id and password (important)
bot = InstaBot("userId","password")
bot.followers()
bot.following()
bot.close()
