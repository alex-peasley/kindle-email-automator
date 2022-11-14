import os

class Preferences():
    def __init__(self):
        self.email = os.environ['KINDLE_ADR']
        self.password = os.environ['KINDLE_PWD']
        self.password = os.environ['KINDLE_DIR']