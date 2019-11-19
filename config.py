#config.py

class Config(object):
	"""
	Common config
	"""

	#any config common for all env

class DevelopmentConfig(Config):
	"""
	Develop config
	"""

	DEBUG = True


class ProductionConfig(Config):
	"""
	Production Config
	"""
	
	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'prodction': ProductionConfig
}
