from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        valid_services = ["MainService", "SecondaryService"]
        if service_type not in valid_services:
            raise Exception("Invalid service type!")
        if service_type == "MainService":
            service = MainService(name)
        else:
            service = SecondaryService(name)

        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        valid_robots = ["MaleRobot", "FemaleRobot"]
        if robot_type not in valid_robots:
            raise Exception("Invalid robot type!")
        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
        else:
            robot = FemaleRobot(name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot = [x for x in self.robots if x.name == robot_name][0]
        current_service = [x for x in self.services if x.name == service_name][0]
        if (current_robot.__class__.__name__ == "FemaleRobot" and
            current_service.__class__.__name__ == "MainService") or (
                current_robot.__class__.__name__ == "MaleRobot" and
                current_service.__class__.__name__ == "SecondaryService"):
            return "Unsuitable service."

        if current_service.capacity <= len(current_service.robots):
            raise Exception("Not enough capacity for this robot!")

        current_service.robots.append(current_robot)
        self.robots.remove(current_robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        current_service = [x for x in self.services if x.name == service_name][0]
        current_robot = None
        for robot in current_service.robots:
            if robot.name == robot_name:
                current_robot = robot
                break

        if current_robot is None:
            raise Exception("No such robot in this service!")

        self.robots.append(current_robot)
        current_service.robots.remove(current_robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        current_service = [x for x in self.services if x.name == service_name][0]
        for robot in current_service.robots:
            robot.eating()

        return f"Robots fed: {len(current_service.robots)}."

    def service_price(self, service_name: str):
        current_service = [x for x in self.services if x.name == service_name][0]
        total_price = 0
        for robot in current_service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):

        return_list = [x.details() for x in self.services]

        return '\n'.join(return_list)
