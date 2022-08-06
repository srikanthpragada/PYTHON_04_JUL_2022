import threading


class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(f'Child {i}')


print(threading.current_thread())
pt = PrintThread()
pt.start()

for i in range(1, 11):
    print(f'Main {i}')


def print_numbers():
    print("Another thread!")


t = threading.Thread(target=print_numbers)
t.start()
