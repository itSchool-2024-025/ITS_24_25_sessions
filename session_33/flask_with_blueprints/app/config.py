import os
class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # print(SQLALCHEMY_DATABASE_URI)
    SECRET_KEY = "1234567890"
# if __name__ == "__main__":
#     print(os.getcwd())