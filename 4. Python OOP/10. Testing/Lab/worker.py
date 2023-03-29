class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest

class WorkerTests(unittest.TestCase):

    def test_initialization(self):
        worker = Worker('Rado', 1000, 100)
        self.assertEqual(worker.name, 'Rado')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 100)
        self.assertEqual(worker.money, 0)

    def test_rest(self):
        worker = Worker('Rado', 1000, 100)
        worker.rest()
        self.assertEqual(worker.energy, 101)

    def test_work_negative_energy(self):
        worker = Worker('Rado', 1000, -1)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_zero_energy(self):
        worker = Worker('Rado', 1000, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_increase(self):
        worker = Worker('Rado', 1000, 100)
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_decrease_energy(self):
        worker = Worker('Rado', 1000, 100)
        worker.work()
        self.assertEqual(worker.energy, 99)

    def test_string_return(self):
        worker = Worker('Rado', 1000, 100)
        self.assertEqual(worker.get_info(), f'Rado has saved 0 money.')


if __name__ == '__name__':
    unittest.main()
