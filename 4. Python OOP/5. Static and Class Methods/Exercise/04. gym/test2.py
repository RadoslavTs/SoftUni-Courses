from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

g = Gym()
s = Subscription("10.02.2020", 1, 1, 1)
p = ExercisePlan(1, 1, 10)
e = Equipment("Pesho")
t = Trainer("Pesho")
c = Customer("Pesho", "addr.", "pesho@gmail.com")
g.add_subscription(s)
g.add_customer(c)
g.add_equipment(e)
g.add_plan(p)
g.add_trainer(t)

print(g.subscription_info(1).strip())
# "Subscription <1> on 10.02.2020\nCustomer <1> Pesho; Address: addr.; Email: pesho@gmail.com\nTrainer <1> Pesho\nEquipment <1> Pesho\nPlan <1> with duration 10 minutes"