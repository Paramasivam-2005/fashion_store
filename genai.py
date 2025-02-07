import google.generativeai as genai
import os
import pymysql
import mysql.connector
import pyodbc
from sqlalchemy import create_engine
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase 
from langchain_experimental.sql import SQLDatabaseChain
os.environ['GOOGLE_API_KEY']="AIzaSyC2t5DAhMdlO81QFZd1clO17TUbT9X0uRQ"


user='root'
pas='root'
host='localhost'

con=mysql.connector.connect(host='localhost',port='3306',user='root',password='root',database='fashion')
uri = f"mysql+pyodbc://root:root@localhost/fashion?driver=MySQL ODBC 9.2 Unicode Driver"

db = SQLDatabase.from_uri(uri)
llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.6)
db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)



