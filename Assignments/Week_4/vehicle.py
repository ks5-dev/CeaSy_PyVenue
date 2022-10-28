'''
Tạo 1 lớp là Phương tiện giao thông (Vehicle) có các phương thức sau:
Vận tốc tối đa (km/h) (max_speed)
Quãng đường có thể đi được nếu đầy nhiên liệu (milage)

Tạo phương thức run cho lớp, trong đó hỏi người dùng input muốn chạy khoảng cách bao nhiêu và trừ đi để lấy được milage mới là khoảng cách nó có thể chạy sau khi chạy quãng vừa rồi
Tất nhiên không cho chạy nếu khoảng cách lớn hơn quãng đường đi được

Tạo phương thức nạp nhiên liệu (fefuel) mà quãng đường có thể đi sẽ trở về con số ban đầu trước khi chạy

Tạo phương thức info để lấy dữ liệu về quãng đường mà phương tiện có thể đi

Tạo 1 lớp con là Bus thừa hưởng của lớp vừa rồi
Lớp này có điểm khác đó là có 1 thuộc tính là lượng khách chứa (capacity) mà thuộc tính này bị đóng gói lại. Sẽ có phương thức setCapaciy bị thay thế.
Phương thức info của lớp này sẽ print trên máy lượng khách chứa được cũng như là quãng đường có thể đi
'''

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = self.max_milage = mileage
    def run(self):
        distance = int(input("Enter the number of kilometers you want this to run: "))
        if self.mileage >= distance:
            self.mileage -= distance
            print("Done travelling")
        else:
            print("Can't run that much distance as it will be out of fuel")
    def refuel(self):
        self.mileage = self.max_milage

    def info(self):
        print(f"This vehicle can run for {self.mileage} kilometers before it runs out of fuel")

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.__capacity = 40 #default
    def info(self):
        print(f"There can be {self.capacity} passengers on this bus and this bus can run for {self.mileage} kilometers before it runs out of fuel" )
    def set_capacity(self, capacity):
        self.__capacity = capacity

vehicle = Vehicle(50, 5000)
vehicle.run()

bus = Bus(60, 7000)
bus.run()
bus.refuel()