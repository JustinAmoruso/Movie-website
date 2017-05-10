class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """creates an object of the Movie type
            taking input of title,storyline,image, and trailer"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
