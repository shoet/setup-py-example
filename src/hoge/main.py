from _input import MyInput
from _manager import MyManager
from _output import MyOutput

from call import call

def main():
    input = MyInput()
    call(input)

    manage = MyManager()
    call(manage)

    output = MyOutput()
    call(output)

if __name__ == '__main__':
    main()
