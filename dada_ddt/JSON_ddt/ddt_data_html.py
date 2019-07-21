import logging
import ddt
import unittest
import traceback
import time
from dada_ddt.JSON_ddt.ReportTemplate import ReportHtml

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式
    format="%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s",
    datefmt="%a,%d %b %Y %H: %M: %S",
    filename="/Users/fanxu/Desktop/fanxu_use/dada_ddt/JSON_ddt/ddt_test.html",
    filemode="w"
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestDemo.trStr = ""

    def setUp(self):
        self.driver = webdriver.Chrome()
        status = None
        flag = 0

    @ddt.file_data("test_data_list.json")
    def test_dataDriverByFile(self, value):
        # 决定测试报告中状态单元格中内容颜色
        flagDict = {0: "red", 1: "#00AC4E"}
        url = "https://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        testdata, expectdata = tuple(value.strip().split("||"))
        self.driver.implicitly_wait(10)
        start = time.time()
        startTime = time.strftime("%Y-%y-%d %H:%M:%S", time.localtime())

        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error("查找的页面元素不存在，异常堆栈信息:{}".format(traceback.format_exc()))
            status = "fail"
            flag = 0
        except AssertionError as e:
            logging.error("搜索:{},期望:{}，结果:失败".format(testdata, expectdata))
            status = "fail"
            flag = 0
        except Exception as e:
            logging.error("未知错误信息：{}".format(str(traceback.format_exc())))
            status = "fail"
            flag = 0
        else:
            logging.error("搜索:{},期望:{}，结果:通过".format(testdata, expectdata))
            status = "pass"
            flag = 1
        wasteTime = time.time() - start -3

        TestDemo.trStr += """
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{:.2f}</td>
                <td style = "color: {}">{}</td>
            </tr><br/>
        """.format(testdata, expectdata, startTime, wasteTime, flagDict[flag], status)
        print(self.trStr)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        ReportHtml().htmlTemplate(TestDemo.trStr)

if __name__ == '__main__':
    unittest.main()