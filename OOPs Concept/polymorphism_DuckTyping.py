class JioCaller():
    def call(self):
        print("Calling")

class Truecaller():
    def call(self):
        print("Ringing")
        print("Caller data")

class Phone:
    def callFunc(self,phoneApp):
        phoneApp.call()

phoneApp=JioCaller()
# phoneApp=Truecaller()
p1=Phone()
p1.callFunc(phoneApp)