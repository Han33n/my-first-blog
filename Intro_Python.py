def hi():
    print('Hi there!')
    print('How are you?')
hi()    
def bye():
    print('goodbye')
bye()    
def greeting(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

greeting(name='Nina')
greeting(name='Ola')
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
def hello(name):
    print("hello " + name + "!")
for name in girls:
    hello(name)
print('Next girl')   