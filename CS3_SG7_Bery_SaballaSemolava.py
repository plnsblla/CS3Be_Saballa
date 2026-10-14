class Machine:

    def __init__(self, serial_number):
        self.serial_number = serial_number

    def show_info(self):
        print("Serial Number: ", self.serial_number)

class DeliveryRobot(Machine):

    def __init__(self, serial_number, cargo_capacity):
        super().__init__(serial_number)
        self.cargo_capacity = cargo_capacity
        self.control_board = ControlBoard()

    def show_info(self):
        super().show_info()
        print("Cargo Capacity: ", self.cargo_capacity)

class ControlBoard:

    def work(self):
        print("Control Board is working.")

class RoboticsRoom:

    def __init__(self):
        self.robot = None

    def assign_robot(self, robot: DeliveryRobot):
        self.robot = robot

class DiagnosticTool:

    def scan(self, robot: DeliveryRobot):
        print("Scanning robot ", robot.serial_number, "...")

class Technician:

    def inspect(self, robot: DeliveryRobot, tool: DiagnosticTool):
        tool.scan(robot)

robot1 = DeliveryRobot("014", 50)
robot1.show_info()
robot1.control_board.work()

room = RoboticsRoom()
room.assign_robot(robot1)
print("Assigned robot to room:", room.robot.serial_number)
del room
# proving the robot still works after deleting room
robot1.control_board.work()

tool = DiagnosticTool()
tech = Technician()
tech.inspect(robot1, tool)
