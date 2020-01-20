#!/usr/bin/env python

from dotenv import load_dotenv
import os

load_dotenv()

db_connect = os.getenv('DBCONNECT')

print(db_connect)
