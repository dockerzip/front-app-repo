import os

class Config:
  SECRET_KEY='my_super_secret_key_with_random_characters_123!@#'
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SQLALCHEMY_DATABASE_URI='postgresql://lhb:qwe123@database-1.c3ug6g6o4tmt.ap-northeast-2.rds.amazonaws.com/myhouse'
  SQLALCHEMY_ECHO=True
