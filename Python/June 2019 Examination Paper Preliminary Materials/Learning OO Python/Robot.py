import time as t

class Robot:
    population = 0
    robotID = 0

    def __init__(self, name, displayInitDetails):
        self.name = name
        self.id = Robot.id+1

        Robot.population += 1

        if displayInitDetails:
            print(f'Created robot with name "{self.name}"')
            print(f'Robot ID: {self.id}')
        else:
            print('Robot created!')

    def getId(self):
        return self.id
    def getName(self):
        return self.name


class BuilderRobot(Robot):
    def build(self, object):
        
