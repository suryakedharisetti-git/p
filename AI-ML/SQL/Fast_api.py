from fastapi import FastAPI
import pandas as pd
from fastapi.responses import HTMLResponse

app = FastAPI()

students_df = pd.read_csv("./students.csv")
courses_df = pd.read_csv("./courses.csv")
enrollments_df = pd.read_csv("./enrollments.csv")

#1.Write a Python program to connect to MySQL and print the list of all available databases.


