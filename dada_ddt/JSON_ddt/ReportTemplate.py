# encoding = utf-8

class ReportHtml:
    filename = "/Users/fanxu/Desktop/fanxu_use/dada_ddt/JSON_ddt/ddt_test.html"
    def htmlTemplate(self, trData):
        htmlStr = """
        <!DOCTYPE HTML>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>测试报告</title>
            <style>
                body{
                    width: 80%;
                    margin: 40px auto;
                    font-weight: bold;
                    font-family: 'trebuchet MS';
                    font-size: 18px;
                    color: #000;
                }
                table{
                    * border-collapse: collapse;
                    border-spacing:0;
                    width: 100%;
                }
                .tableStyle{
                    border-style: outset;
                    border-width: 2px;
                    border-color: blue;
                }
                .tableStyle tr:hover{
                    background: rgb(173, 216, 230);
                }
                .tableStyle td, tableStyle th{
                    border-left: solid 1px rgb(146, 208, 80);
                    border-top: 1px solid rgb(146, 208, 80);
                    padding: 15px;
                    text-align: center;
                }
                .tableStyle th{
                    padding: 15px;
                    background-color: rgb(199, 255, 212);
                    background-image: -webkit-gradient(linear, left top, left bottom, from(#92D050), to(#A2D668));
                }
            </style>
        </head>
        <body>
            <conter><h1>测试报告</h1></conter><br/>
                <table class = "tableStyle">
                    <thead>
                    <tr>
                        <th>Search Words</th>
                        <th>Assert Words</th>
                        <th>Start Time</th>
                        <th>Waster Time</th>
                        <th>Status</th>
                    </tr>
                    </thead>
        """
        endStr = """
                    </table>
        </body>
        </html>
        """

        # 拼接完整的测试报告HTML页面代码
        html = htmlStr + trData + endStr

        with open(self.filename, "w") as fp:
            fp.write(html)



hh = """

        <!DOCTYPE HTML>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>测试报告</title>
            <style>
                body{
                    width: 80%;
                    margin: 40px auto;
                    font-weight: bold;
                    font-family: 'trebuchet MS';
                    font-size: 18px;
                    color: #000;
                }
                table{
                    * border-collapse: collapse;
                    border-spacing:0;
                    width: 100%;
                }
                .tableStyle{
                    border-style: outset;
                    border-width: 2px;
                    border-color: blue;
                }
                .tableStyle tr:hover{
                    background: rgb(173, 216, 230);
                }
                .tableStyle td, tableStyle th{
                    border-left: solid 1px rgb(146, 208, 80);
                    border-top: 1px solid rgb(146, 208, 80);
                    padding: 15px;
                    text-align: center;
                }
                .tableStyle th{
                    padding: 15px;
                    background-color: rgb(146, 208, 80);
                    background-image: - webkit -gredient(liner, left top, left botton, from(#92D050), to(#A2D668))
                }
            </style>
        </head>
        <body>
            <conter><h1>测试报告</h1></conter><br/>
                <table class = "tableStyle">
                    <thead>
                    <tr>
                        <th>Search Words</th>
                        <th>Assert Words</th>
                        <th>Start Time</th>
                        <th>Waster Time</th>
                        <th>Status</th>
                    </tr>
                    </thead>
        
            <tr>
                <td>邓肯</td>
                <td>蒂姆</td>
                <td>2019-19-21 20:03:13</td>
                <td>0.23</td>
                <td style = "color: #00AC4E">pass</td>
            </tr><br/>
        
            <tr>
                <td>乔丹</td>
                <td>迈克尔</td>
                <td>2019-19-21 20:03:19</td>
                <td>0.25</td>
                <td style = "color: #00AC4E">pass</td>
            </tr><br/>
        
            <tr>
                <td>库里</td>
                <td>斯蒂芬</td>
                <td>2019-19-21 20:03:36</td>
                <td>7.06</td>
                <td style = "color: read">fail</td>
            </tr><br/>
        
            <tr>
                <td>杜兰特</td>
                <td>凯文</td>
                <td>2019-19-21 20:03:48</td>
                <td>7.02</td>
                <td style = "color: read">fail</td>
            </tr><br/>
        
            <tr>
                <td>詹姆斯</td>
                <td>勒布朗</td>
                <td>2019-19-21 20:04:01</td>
                <td>7.02</td>
                <td style = "color: red">fail</td>
            </tr><br/>
        
                    </table>
        </body>
        </html>
        """
filename = "/Users/fanxu/Desktop/fanxu_use/dada_ddt/JSON_ddt/ddt_test.html"
with open(filename, "w") as fp:
    fp.write(hh)