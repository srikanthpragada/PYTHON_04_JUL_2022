# course with title, duration and fee

class Course:
    # static or class attribute
    taxrate = 8

    @staticmethod
    def get_taxrate():
        return Course.taxrate

    def __init__(self, title, duration, fee):
        # Object attributes
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

    @property
    def net_fee(self):
        return self.fee + (self.fee * Course.taxrate / 100)

    def show(self):
        print(f"Title    : {self.title}")
        print(f"Duration : {self.duration}")
        print(f"Fee      : {self.fee}")


print(Course.get_taxrate())  # call static method
c1 = Course("React", 12, 2000)
c1.set_fee(3000)
c1.show()
print(c1.net_fee)   # Property
