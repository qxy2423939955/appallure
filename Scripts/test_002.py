import allure

class Test_002:
    @allure.setp(title='我是test_003的操作步骤名称')
    def test_003(self):
        print('----test_003')
        assert True

    @allure.setp(title='我是test_003的操作步骤名称')
    def test_004(self):
        print('----test_004')
        assert False

