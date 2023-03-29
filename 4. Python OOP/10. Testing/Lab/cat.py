class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


import unittest

class TestTheCat(unittest.TestCase):
    
    def setUp(self) -> None:
      self.my_cat = Cat('Rado')
      
    def test_size_increase_after_eating(self):
      self.my_cat.eat()
      self.assertEqual(self.my_cat.size, 1)

    def test_cat_is_fed_after_eating(self):
      self.my_cat.eat()
      self.assertTrue(self.my_cat.fed)
      
    def test_cannot_eat_after_eat(self):
      self.my_cat.eat()
      with self.assertRaises(Exception) as context:
        self.my_cat.eat()
      self.assertEqual(str(context.exception), 'Already fed.')

    def test_cannot_sleed(self):
      with self.assertRaises(Exception) as context:
        self.my_cat.sleep()
      self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_not_sleepy(self):
      self.my_cat.eat()
      self.my_cat.sleep()
      self.assertFalse(self.my_cat.sleepy)


if __name__ == '__name__':
  unittest.main()