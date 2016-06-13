import webbrowser

class Movie():
    """
    Attributes:
        title               (str): Title of the movie
        storyline           (str): Plot of the movie
        poster_image_url    (str): Poster of the movie as a URL link
        trailer_youtube_url (str): Trailer of the movie as a youtube URL link
    """
    # Instantiate movie object
    def __init__(self, title, storyline, poster_image_url, youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = youtube_url

    # Open browser to linked url
    def play_trailer(self):
        webbrowser.open(self.youtube_trailer)
