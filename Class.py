class Robot:
    population = 0

    def __init__(self, name):
        """Initialized the data."""
        self.name = name
        print("(Initializing {self.name})")
        Robot.population += 1

    def die(self):
        """I am dying"""
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was last one.")
        elif Robot.population == 1:
            print(f"There are still {Robot.population} robot working")
        elif Robot.population >1:
            print(f"There are still {Robot.population} robots working")

    def sai_hi(self):
        """Greeting by the robot

        Yeah, they can do that"""
        print(f"Greeting, my master call me {self.name}")

    @classmethod
    def how_many(cls):
        """Print the current population."""
        print(f"We have {cls.population}")


droid1 = Robot("R2-D2")
droid1.sai_hi()
Robot.how_many()


droid2 = Robot("R-CP0")
droid2.sai_hi()
Robot.how_many()


droid3 = Robot("T-10")
droid3.sai_hi()
Robot.how_many()

print("my check of images")
droid1.how_many()
droid2.how_many()
droid3.how_many()
Robot.how_many()

print("\nRobots can do some work\n")

droid2.die()
Robot.how_many()
droid2.die()
Robot.how_many()
droid3.die()
