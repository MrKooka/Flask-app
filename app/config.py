class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://Mysql:123456789@localhost/test1'
	SECRET_KEY = 'somthing very sdsfwwfwefsdfsdfwf'

	### Flask security 
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'