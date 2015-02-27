import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_year, mpaa_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = release_year
        self.ratings = mpaa_rating

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
