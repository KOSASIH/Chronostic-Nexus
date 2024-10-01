import unittest
from robotics.robotics import Robotics

class TestRobotics(unittest.TestCase):
    def test_robotics(self):
        robotics = Robotics()
        self.assertIsNotNone(robotics.model)

    def test_train(self):
        robotics = Robotics()
        robotics.train(["action1", "action2"])
        self.assertIsNotNone(robotics.model)

    def test_predict(self):
        robotics = Robotics()
        robotics.train(["action1", "action2"])
        self.assertIsNotNone(robotics.predict("action1"))

if __name__ == '__main__':
    unittest.main()
