class Movie:
    '''
    movie class to define 
    movie objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):

        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://developers.themoviedb.org/3/getting-started/images'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
