global_msg = "Greeting Globally"

def greet():
    global_msg = 'Change is good'
    if True:
        message_local = "Greeting local"
    print(message_local)


greet()
print(global_msg)

evil_global_msg = "You were warned"

def evil_function():
    global evil_global_msg
    evil_global_msg = "You should have listened "

print(evil_global_msg)
evil_function()
print(evil_global_msg)
