# Customer Churn & Revenue Risk Analysis

#----------------------------------------------------------------------------#

"""Business Problem
A telecom company is losing customers.
Analyze customer behavior, identify churn drivers, estimate revenue at risk,
and provide retention recommendations."""

#----------------------------------------------------------------------------#

"""Analyzed 7,000+ telecom customers,
identified contract type, tenure, and monthly charges as key churn drivers,
and proposed retention strategies that could reduce customer loss."""

#----------------------------------------------------------------------------#


import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df[df["gender"]== "Female"])