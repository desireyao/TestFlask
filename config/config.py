class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:asdf1234@127.0.0.1:3306/test'
    SQLALCHEMY_POOL_TIMEOUT = 60
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:asdf1234@127.0.0.1:3306/tnews'


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:asdf1234@127.0.0.1:3306/tnews'

Config = {
    'testing': TestingConfig,
    'procuction': ProductConfig
}

# 只需改变此处 配置当前的环境
CurConfig = {
    "CONFIG": Config['procuction']
}
