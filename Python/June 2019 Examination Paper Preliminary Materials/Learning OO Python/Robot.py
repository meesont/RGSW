import time as t

class Robot:
    population = 0
    id = 0

    def __init__(self, name, lifetime, displayInitDetails):
        self.name = name
        self.lifetime = lifetime
        self.id = Robot.id+1
        self.displayInitDetails = displayInitDetails

        Robot.population += 1

        if displayInitDetails:
            print('Initialising...')
            t.sleep(0.5)
            print(f'Robot initialised')
            t.sleep(2)
            print(f'Robot Name: {self.name}')
            print(f'Robot Lifetime: {self.lifetime}')
            print(f'Robot ID: {self.id}')
        else:
            print('Robot Created')


    def die(self):
        Robot.population -= 1

        if Robot.population == 0:
            print(f'The population is now {Robot.population}, all robots have died!')
        else:
            print(f'Calculating current robot population...')
            t.sleep(0.5)
            print(f'There are a total of: {Robot.population} still working.')

    def say_hi(self):
        print(f'Greetings, my name is: {self.name}')
        print(f'Robot ID: {self.id}')

    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getLifetime(self):
        return self.lifetime
