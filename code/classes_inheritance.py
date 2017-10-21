__author__ = 'kieranrimmer'

class A():

    # static variable with default value
    n_A = 0

    def __init__(self, x = None):
        """
        Constructor for A
        :param x:
        :return:
        """
        # increment static variable
        A.n_A += 1
        # declare and initialise instance variable
        self.x = x

    def print_out(self):
        print('n_A = ', A.n_A)
        print('x = ', self.x)


class B(A):

    def __init__(self, x = None):
        """
        Constructor for B
        :param x:
        :return:
        """
        super().__init__(x)

    def print_out(self):
        print('printing B...')
        super().print_out()





def do_stuff():
    a1 = A()
    a1.print_out()
    a2 = A('hello world')
    a2.print_out()
    b1 = B(55)
    b1.print_out()
    for x in [a1, a2, b1]:
        x.print_out()

if __name__ == '__main__':
    do_stuff()


