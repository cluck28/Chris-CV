#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:10:34 2018

Working version of database is ONET_db_v1

ONET_db_v2 is going to include alternate titles for SQL search

@author: christopherluciuk
"""

from flask import render_template, request, url_for
from flaskapp import app
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

# Python code to connect to Postgres
# You may need to modify this based on your OS, 
# as detailed in the postgres dev setup materials.
user = 'christopherluciuk' #add your Postgres username here      
host = 'localhost'
dbname = 'website_blogs_v1'
db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
con = None
con = psycopg2.connect(database = dbname, user = user)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template("index.html")    

@app.route('/blog', methods=['GET','POST'])
def blog():
    sql_query = """
    SELECT * FROM blog_table;
    """
    data_out = pd.read_sql_query(sql_query,con)
    titles = []
    intros = []
    for index, row in data_out.iterrows():
        titles.append(row['title'])
        intros.append(row['intro'])
    titles = titles[::-1]
    intros = intros[::-1]
    index = [str(0),str(1),str(2)]
    return render_template("blog.html",data=zip(titles[0:2],intros[0:2],index))

@app.route('/allblogs', methods=['GET','POST'])
def allblogs():
    sql_query = """
    SELECT * FROM blog_table;
    """
    data_out = pd.read_sql_query(sql_query,con)
    titles = []
    intros = []
    for index, row in data_out.iterrows():
        titles.append(row['title'])
        intros.append(row['intro'])
    titles = titles[::-1]
    intros = intros[::-1]
    return render_template("allblogs.html",data=zip(titles,intros))

@app.route('/blog_item/<string:index>',methods=['GET','POST'])
def blog_item(index):
    sql_query = """
    SELECT * FROM blog_table;
    """
    data_out = pd.read_sql_query(sql_query,con)
    bodys = []
    for index, row in data_out.iterrows():
        bodys.append(row['body'])
    bodys = bodys[::-1]
    return render_template("blog_item.html",body=bodys[index])                