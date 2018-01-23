class Config:
    ''' 
    general configuration  parent class
    '''

    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'



class ProdConfig(Config):
    '''
    production configuration child class
    Args:
    Config: The parent configuration class
    with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    development configurationchild class
    Args:
    Config:The parent configuration class with general
    configuration settings
    '''
    DEBUG = True