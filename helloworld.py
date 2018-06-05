import lib-hello-world as li

def helloworld():
  return "Hello World!"
  
  
li.many(10, li.hello()+li.world())
print(helloworld())
