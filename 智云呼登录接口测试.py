__author__ = 'Administrator'

import requests,json,unittest,HTMLTestRunner
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.url='http://192.168.1.200/manager/login'
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    def testTrue(self):

        params={
    'loginName':'client',
    'password':'abc123'
        }
        r=requests.post(self.url,data=json.dumps(params),headers=self.headers)

        d=json.loads(r.text)

        assert (u'成功' in d['message'])
    def testFalse(self):
        params={
    'loginName':'client',
    'password':'123'
        }
        r=requests.post(self.url,data=json.dumps(params),headers=self.headers)

        d=json.loads(r.text)

        assert (u'成功' not in d['message'])
    def testUserFalse(self):
        params={
    'loginName':'123',
    'password':'abc123'
        }
        r=requests.post(self.url,data=json.dumps(params),headers=self.headers)

        d=json.loads(r.text)

        assert (u'成功' not in d['message'])

    def tearDown(self):
        pass
if __name__=='__main__':
    report_dir =r'智云呼登录接口测试报告.html'
    re_open=open(report_dir,'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(TestLogin)

    runner=HTMLTestRunner.HTMLTestRunner(
        stream=re_open,
        title=u'智云呼登录接口测试报告',
        description=u'智云呼登录接口测试详情'
    )
    runner.run(suite)