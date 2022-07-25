# course with title, duration and fee

class Course:
    def __init__(self, title, duration, fee):
        self.title = title
        self.duration = duration
        self.fee = fee

    def get_duration(self):
        return self.duration

    def get_fee(self):
        return self.fee

    def set_duration(self, duration):
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError('Invalid Duration')

    def set_fee(self, fee):
        self.fee = fee

    def net_fee(self):
        return self.fee * 1.08

    def show(self):
        print(f"Title    : {self.title}")
        print(f"Duration : {self.duration}")
        print(f"Fee      : {self.fee}")


c1 = Course("React", 12, 2000)
c1.set_fee(3000)
c1.show()
print(c1.net_fee())
