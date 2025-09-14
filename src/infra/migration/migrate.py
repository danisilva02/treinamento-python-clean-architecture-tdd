import os
import glob
from src.infra.driver.contract import DriverContract

path_schema = os.path.join(os.path.dirname(__file__), "*.sql")

class Migrate:
    def __init__(self, driver: DriverContract):
        self.driver = driver

    def perform(self):
        ordered_files = sorted(glob.glob(path_schema))
        for file in ordered_files:
            with open(file, "r", encoding="utf-8") as f:
                self.driver.execute(sql=f.read())