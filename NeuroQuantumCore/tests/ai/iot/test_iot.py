import unittest
from iot.iot import IoT

class TestIoT(unittest.TestCase):
    def test_iot(self):
        iot = IoT()
        self.assertIsNotNone(iot.model)

    def test_train(self):
        iot = IoT()
        iot.train(["device1", "device2"])
        self.assertIsNotNone(iot.model)

    def test_predict(self):
        iot = IoT()
        iot.train(["device1", "device2"])
        self.assertIsNotNone(iot.predict("device1"))

if __name__ == '__main__':
    unittest.main()
