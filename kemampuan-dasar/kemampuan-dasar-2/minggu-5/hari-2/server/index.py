import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Sugeng Enjing Cak !!!")
        
class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "bejo" if n % 2 else "even"
        self.write("nomere " + str(n) + " adalah " + r)
        
class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write("Kedah menika nomer " + id )
        
class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    

if __name__ == '__main__':
    app = tornado.web.Application([
            (r"/", basicRequestHandler), 
            (r"/site", staticRequestHandler),
            (r"/isEven", queryStringRequestHandler),
            (r"/togel/([0-9]+)", resourceRequestHandler)
        ])
    
    app.listen(8881)
    print("I'm listening on port 8881")
    tornado.ioloop.IOLoop.current().start()

































# import motor.motor_tornado
# import tornado.ioloop
# import tornado.web

# client = motor.motor_tornado.MotorClient()
# client = motor.motor_tornado.MotorClient('localhost', 27017)

# # start with connection url
# # client = motor.motor_tornado.MotorClient('mongodb://localhost:27017')
# # client = motor.motor_tornado.MotorClient('mongodb://host1,host2/?replicaSet=my-replicaset-name')

# db = client.test_database
# db = client["test_database"]
# db = motor.motor_tornado.MotorClient().test_database

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
        
# application = tornado.web.Application([
#     (r'/', MainHandler)
# ], db=db)

# application.listen(8888)
# tornado.ioloop.IOLoop.current().start()

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         db = self.settings['db']