from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

import os
import sqlite3

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt,question])
    return response.text

def read_sql_query(sql,db):
    forbidden = False
    rows = []
    
    if contains_forbidden_words(sql):
        forbidden = True
    else:
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute(sql)
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        for row in rows:
            print(row)
    
    return rows, forbidden

def contains_forbidden_words(sql):
    forbidden_words = ["delete","alter","drop","truncate"]
    for word in forbidden_words:
        if word in sql.lower():
            return True
    return False


prompt="""
Generate only SQL database query based on the English question. Do not generate any text other than SQL query.
There is a Student database with two tables: Student and Fees. Student table has column Id, Name, Class,
Section, Marks. Fees table has columns StudentId, Month, Amount.
Do not include ``` at the start or end of query. Also do not put sql keyword in the query
"""

st.set_page_config(page_title="I can query your question")
st.header("Sql query generator using Gemini Pro")
question = st.text_input("Question ",key="input")
submit=st.button("Ask Now")

if submit:
    query=get_gemini_response(question,prompt)
    print(query)
    rows, forbidden=read_sql_query(query,"student.db")
    st.subheader("The output is:")

    if forbidden == True:
        st.header("Could not execute delete or alter or drop or truncate query")
    else:
        for row in rows:
            print(row)
            st.header(row)
