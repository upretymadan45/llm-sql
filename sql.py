from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os 
import sqlite3

import google.generativeai as genai

##Configure GenAI Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide queries as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#Function to retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Define your prompt

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - Id, Name, Class,
    Section \n\n For example, \n Example 1 - How many entries of records are present?,
    the SQL command will be something like this Select Count(*) from Student;
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this Select * from student where
    class="Data Science";
    There is another table called Fees linked with student table using foreign key StudentId. One student can have multiple Fees. Fees table will have\n 
    columns like - StudentId, Month and Amount.\n
    also the sql code should not have ``` in the beginning or end and sql word in 
    output

    """
]

#Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Geminni App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

#If submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)