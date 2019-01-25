import allure

class Test_002:
    @allure.step(title='我是test_003的操作步骤名称')
    def test_003(self):
        print('----test_003')
        assert True

    @allure.step(title='我是test_004的操作步骤名称')
    def test_004(self):
        print('----test_004')
        assert False

