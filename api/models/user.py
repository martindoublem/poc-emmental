from sqlalchemy import BigInteger, Column, String

from utils.db import Model


class User(Model):

    id = Column(String, primary_key=True)

    email = Column(String)
