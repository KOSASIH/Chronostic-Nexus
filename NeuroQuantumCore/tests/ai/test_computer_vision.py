import unittest
from computer_vision.computer_vision import ComputerVision

class TestComputerVision(unittest.TestCase):
    def test_computer_vision(self):
        computer_vision = ComputerVision()
        self.assertIsNotNone(computer_vision.model)

    def test_train(self):
        computer_vision = ComputerVision()
        computer_vision.train(["image1.jpg", "image2.jpg"])
        self.assertIsNotNone(computer_vision.model)

    def test_predict(self):
        computer_vision = ComputerVision()
        computer_vision.train(["image1.jpg", "image2.jpg"])
        self.assertIsNotNone(computer_vision.predict("image1.jpg"))

if __ name__ == '__main__':
    unittest.main()
