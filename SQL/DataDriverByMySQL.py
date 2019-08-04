from selenium import webdriver
import unittest, time
import logging, traceback
import ddt
from SQL.MysqlUtil import MyMySQL
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式
    format="%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s",
    datefmt="%a,%d %b %Y %H: %M: %S",
    filename="/Users/fanxu/Desktop/fanxu_use/dada_ddt/db_data_test.log",
    filemode="w"
)

def getestData():
    db = MyMySQL(
        host="localhost",
        port=3306,
        dbName="gloryroad",
        username="root",
        password="123456",
        charset="utf8"
    )
    data = db.getDataFromDataBases()
    # print(db.getDataFromDataBases())
    db.closeDatabase()
    return data


@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(*getestData())
    def test_dataDrivenByDatabase(self, data):
        testData, expectData = data
        url = "https://www.baidu.com"
        self.driver.get(url=url)

        self.driver.maximize_window()
        print(testData, expectData)

        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element_by_id("kw").send_keys(testData)
            self.driver.find_element_by_id("su").click()
            time.sleep(2)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            print(e)
            logging.error("查找页面元素不存在，异常堆栈信息：", str(traceback.format_exc()))
        except AssertionError as e:
            logging.error("搜索:{},期望:{}，结果:失败".format(testData, expectData))
        except Exception as e:
            logging.error("未知错误信息：{}".format(str(traceback.format_exc())))
        else:
            logging.error("搜索:{},期望:{}，结果:通过".format(testData, expectData))

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()