import os

class Config(object):
   """Base configuration."""
   BCRYPT_LOG_ROUNDS = 13
   ASSETS_DEBUG = False
   DEBUG_TB_ENABLED = False  # Disable Debug toolbar
   DEBUG_TB_INTERCEPT_REDIRECTS = False
   CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
   SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
   """Production configuration."""
   ENV = 'prod'
   DEBUG = False
#   SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/txmo'
   DEBUG_TB_ENABLED = False  # Disable Debug toolbar

class DevConfig(Config):
   """Development configuration."""
   ENV = 'dev'
   DEBUG = True
   # Put the db file in project root
   SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/txmo'
   DEBUG_TB_ENABLED = True
   ASSETS_DEBUG = True  # Don't bundle/minify static assets
   CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.