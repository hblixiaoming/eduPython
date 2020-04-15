import threading


def sayHello(name, address):
    print('hello {0}, welcome to {1}'.format(name, address))
    print(threading.current_thread().name)


# 方法二通过继承实现一个
class MyThread(threading.Thread):
    def __init__(self, name, address):
        super().__init__(name='Thread2')
        self.__name = name
        self.__address = address

    def run(self):
        print('hello {0}, welcome to {1}'.format(self.__name, self.__address))
        print(threading.current_thread().name)


if __name__ == '__main__':
    # 方法一开启一个线程
    thread1 = threading.Thread(target=sayHello, args=('mike', 'China',), name='thread1')
    thread1.start()

    thread2 = MyThread('jack', 'USA')
    thread2.start()
