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



con=mysql.connector.connect(host='localhost',port='3306',user='root',password='root',database='fashion')
uri = f"mysql+pyodbc://root:root@localhost/fashion?driver=MySQL ODBC 9.2 Unicode Driver"

db = SQLDatabase.from_uri(uri)
llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.6)
db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True)

PROMPT = """
I will act as a helpful assistant adept at querying databases. When given a natural language question about the data, I will:

Analyze the question to understand the intent and entities. What data fields or tables are being asked about?
Formulate a SQL query that is syntactically correct and will retrieve the requested data. Focus on succinct, valid SQL with minimal unnecessary syntax.
Run the generated SQL query against the provided database to retrieve results.
Interpret the results and summarize or format them in a user-friendly way to answer the original question. Convey the essence clearly and concisely.
If I cannot understand the question or generate a suitable query, be honest and state that more clarification is needed. Ask relevant follow-up questions.
Optimize for informativeness, clarity, accuracy and brevity. Avoid irrelevant details or overly verbose responses.
Given this natural language question:

{question}

Please provide a helpful SQL-based response:
"""
query = "Describe the table"
db_chain.run(PROMPT.format(question=query))

