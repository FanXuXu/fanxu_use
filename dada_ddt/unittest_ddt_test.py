from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from time import sleep
import unittest
import logging, traceback
import ddt


# /Users/fanxu/Desktop/fanxu_use/dada_ddt
logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式
    format="%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s",
    datefmt="%a,%d %b %Y %H: %M: %S",
    filename="/Users/fanxu/Desktop/fanxu_use/dada_ddt/test_log_report.log",
    filemode="w" 
)

@ddt.ddt
class DDT_demo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(
        ["神奇动物在哪里", "叶茨"],
        ["疯狂动物城", "古德温"],
        ["大话西游之月光宝盒", "周星驰"],
    )
    @ddt.unpack
    def test_dataDriverByObj(self, testdata, expectdata):
        url = "https://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchAttributeException as e:
            print(e)
            logging.error("查找页面元素不存在，异常堆栈信息：", str(traceback.format_exc()))
        except AssertionError as e:
            logging.error("搜索:{},期望:{}，结果:失败".format(testdata, expectdata))
        except Exception as e:
            logging.error("未知错误信息：{}".format(str(traceback.format_exc())))
        else:
            logging.error("搜索:{},期望:{}，结果:通过".format(testdata, expectdata))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()