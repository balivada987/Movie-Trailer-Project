import webbrowser
'''Overview of Movie class the class has methods called 
   show_trailer= to display trailer on click
   new_file= to create  tiles of images of movies
'''


class Movie():

    def __init__(
            self,
            title,
            poster_image_url,
            trailer_youtube_url,
            movie_storyline):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.movie_storyline = movie_storyline

    def show_trailer(self, trailer_youtube_url):
        webbrowser.open(trailer_youtube_url)

    def new_file(self, movietiles):
        self.movietiles = movietiles
