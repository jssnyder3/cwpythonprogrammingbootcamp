__author__ = 'kieranrimmer'




def good_loop():
    x = 0
    print('kicking off good_loop()')
    while x < 10:
        print('x = {}'.format(x))
        if x % 2 == 0:
            print(x)
        x += 1
    print('exiting from good_loop()')

def out_of_order_loop():
    x = 0
    print('kicking off out_of_order_loop()')
    x += 1
    while x < 10:
        print('x = {}'.format(x))
        if x % 2 == 0:
            print(x)
    print('exiting from out_of_order_loop()')

def bad_loop():
    x = 0
    print('kicking off bad_loop()')
    while x < 10:
        print('x = {}'.format(x))
        if x % 2 == 0:
            print(x)
    x += 1
    print('exiting from bad_loop()')

def worse_loop():
    x = 0
    print('kicking off worse_loop()')
    while x < 10:
        print('x = {}'.format(x))
        if x % 2 == 0:
            print(x)
            x += 1
    print('exiting from worse_loop()')

if __name__ == '__main__':
    good_loop()
    # out_of_order_loop()
    # bad_loop()
    # worse_loop()