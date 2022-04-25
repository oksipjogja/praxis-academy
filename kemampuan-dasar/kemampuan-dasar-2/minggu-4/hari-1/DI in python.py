# class Api:
#     def fetch_remote_data(self):
#         print('Api called')
#         return 42
    
# class BusinessLogic:
#     def __init__(self,api: Api):
#         self.api = api
    
#     def do_stuff(self):
#         api_result = self.api.fetch_remote_data()
#         print(f'the api returned a result; {api_result}')
        # do something with the data and return a result

# # ---

# if __name__ == '__main__':
#     api = Api()
#     logic = BusinessLogic(api=api)
    
#     # ...
    # print(logic.do_stuff())
      
# output
# '''
# Api called
# the api returned a result; 42
# None
# '''
#  pip install injector
# output
# """
# Collecting injector
#   Downloading injector-0.19.0-py2.py3-none-any.whl (19 kB)
# Requirement already satisfied: typing-extensions>=3.7.4; python_version < "3.9" in /home/donie/.local/lib/python3.8/site-packages (from injector) (4.2.0)
# Installing collected packages: injector
# Successfully installed injector-0.19.0
# """

from injector import Injector, singleton, provider, Module

class Api:
    def fetch_remote_data(self):
        print('Api called')
        return 42
    
class BusinessLogic:
    def __init__(self,api: Api):
        self.api = api
    
    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f'the api returned a result: {api_result}')
        # do something with the data and return a result

class Appmodule(Module):

    @singleton
    @provider
    def provide_business_logic(self, api: Api) -> BusinessLogic:
        return BusinessLogic(api=api)
    
    @singleton
    @provider
    def provide_api(self) -> Api:            
        ## --> there is no complex logic in our case
        ## --> e.g when instantiating a particular DB connector
        ## --> but you can use this method to hide the complexity of intial configuration 
        return Api()   
                          
if __name__ == '__main__':
    injector = Injector(Appmodule())  
    
    logic = injector.get(BusinessLogic)
    logic.do_stuff()
    
class TestApi(Api):
    def fetch_remote_data(self):
        print('Demo Api Called')
        return 24

class TestAppModule(Module):
    
    @singleton
    @provider
    def provide_api(self) -> Api:
        return TestApi()  
    
if __name__ == '__main__':
    real_injector = Injector(Appmodule())
    test_injector = Injector([Appmodule(), TestAppModule()])
    
    real_logic = real_injector.get(BusinessLogic)
    real_logic.do_stuff()
    
    test_logic = test_injector.get(BusinessLogic)
    test_logic.do_stuff()
    