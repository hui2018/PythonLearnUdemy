import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn
from scipy.interpolate import interp1d
from scipy.stats import ttest_rel


class looping:
    #constructor
    def __init__(self, first, last):
        self.first = first
        self.last = last

    #display initial values
    def show(self):
        print(self.first + " " + self.last)

    #using a placeholder
    def formating(self,color):
        msg = ("favorite color is: {}")
        print(msg.format(color))

if __name__ == "__main__":
    a = looping("jack", "cheng")
    a.show()
    a.formating("blue")

