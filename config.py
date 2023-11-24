import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6f5c393b-5e8a-4f1e-8960-90b253ca3254'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'vietnv17storeaged'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'PAIHJyE7ULf/Ni2NddoUSJ1l1yrkYxNIjwLzFFCFVKOHRbpBihegYHDsx/OHS3OphUMMYvsl4xfw+AStLhnUmA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'vietnv17-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'vietnv17'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "c6D8Q~9AQ6B84GoLB-E_xJLMfVPW-PRhFMApFdjd"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"
    AUTHORITY = "https://login.microsoftonline.com/9ed2a902-c505-4d83-99b7-2392ad0599f2"

    CLIENT_ID = "7a9a07e8-e8aa-4b27-8f84-c49fb0bef743"

    REDIRECT_PATH = "https://udacity-azure-vietnv17.azurewebsites.net/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
    