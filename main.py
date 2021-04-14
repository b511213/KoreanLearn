from hanspell import spell_checker
import selenium
from selenium import webdriver

result = spell_checker.check([u'서룰특별시.', u'사울특별시.'])
print(result)

options = webdriver.ChromeOptions()
options.add_argument('headless')
wd = webdriver.Chrome('chromedriver', options=options)


def ch_spell(stc):
    wd.get('http://speller.cs.pusan.ac.kr/')
    wd.implicitly_wait(time_to_wait=1)
    wd.find_element_by_xpath('//*[@id="text1"]').send_keys(stc)
    wd.find_element_by_xpath('//*[@id="btnCheck"]').click()
    wd.implicitly_wait(time_to_wait=1)
    num = 0
    while True:
        try:
            wd.find_element_by_xpath('//*[@id="tdReplaceWord_' + str(num) + '"]/ul/li/a').click()
            num += 1
        except:
            break
        text = wd.find_element_by_xpath('//*[@id="tdCorrection1stBox"]').text
        return text
    return stc


result = ch_spell("안녕 하세요")
print(result)

