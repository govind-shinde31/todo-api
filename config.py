import os
import psycopg2

class Config:
    SQLALCHEMY_DATABASE_URI ='postgresql://postgres:Govind31@localhost:5432/todoapp'
    

# conn = psycopg2.connect(database="postgres", user="postgres",
#                         password="Govind31", host="localhost", port="5432")