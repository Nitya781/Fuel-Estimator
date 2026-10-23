"""
=========================================================
Configuration Repository

Loads aircraft configuration from JSON.

Author : HAL Fuel Estimation Project
=========================================================
"""

import json


class ConfigRepository:

    def __init__(self, filepath):

        self.filepath = filepath

        self.data = {}

        self.load()

    def load(self):

        with open(self.filepath, "r") as file:

            self.data = json.load(file)

    # ------------------------------------------------

    @property
    def aircraft(self):
        return self.data["aircraft"]

    @property
    def fuel(self):
        return self.data["fuel"]

    @property
    def engine(self):
        return self.data["engine"]

    @property
    def atmosphere(self):
        return self.data["atmosphere"]

    @property
    def mission(self):
        return self.data["mission"]

    @property
    def simulation(self):
        return self.data["simulation"]
