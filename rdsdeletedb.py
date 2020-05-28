import boto3
import os
import logging
import pymysql
from urllib2 import build_opener, HTTPHandler, Request

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#rds settings
host  = "rds_host_name"
username = "username"
password = "password"
db_start_with = "test"


def dboperation(host,username,password):
    host = str(host)
    try:
        conn = pymysql.connect(host, user=username, passwd=password, connect_timeout=5)
       
        with conn.cursor() as cur:
            dbs = cur.execute("show databases like '%s%%'" %db_start_with)
            print(dbs)
            databaseCollection = cur.fetchall()
            for database in databaseCollection:
                cur.execute("drop database %s" %database)
        return "Success"
    except Exception as e:
        logger.error(e)
        return "Faliure"
def lambda_handler(event, context):
    try:
        dboperation(host, username, password)
    except Exception as e:
        logger.error(e)
         
        
        
        




