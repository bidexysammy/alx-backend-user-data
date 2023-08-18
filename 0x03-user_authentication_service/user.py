#!/usr/bin/env python3
""" This creates a class User """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

base = declarative_base()

class User(base):

    """ This class inherits from base"""
    __tablename__ = 'users'
    id = column(Integer, primary_key=True)
    email = column(String(250), nullable=False)
    hashed_password = column(String(250), nullable=False)
    session_id = column(String(250), nullable=True)
    reset_token = column(String(250), nullable=True)
