import os
#print(os.path.relpath(__file__))
#print(os.path.dirname(os.path.dirname(os.path.relpath(__file__))))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"config","data.yaml"))
print(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "data.yaml"))