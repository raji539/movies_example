import webbrowser

#This file defines the movie data that will be stored.
class Movie():
    """
    Store all relavent movie data and
    display the trailer   
    """
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):

        # store data passed when object is created.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    
    # display the you tube trailer when called.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

