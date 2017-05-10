import fresh_tomatoes
import media

remember_the_titans = media.Movie("Remember the Titans",\
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BYThkMzgxNjEtMzFiOC00MTI0LWI5MDItNDVmYjA4NzY5MDQ2L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR0,0,182,268_AL_.jpg",\
                                  "https://www.youtube.com/watch?v=UsbZmCGteXU")

miracle = media.Movie("Miracle",\
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTk1OTcyNV5BMl5BanBnXkFtZTYwNjMzNDU3._V1_UX182_CR0,0,182,268_AL_.jpg",\
                      "https://www.youtube.com/watch?v=GjctJFuKy3Y")

field_of_dreams = media.Movie("Field of Dreams",\
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BNzk5OWY0YjAtYWU3ZS00Y2Q4LWFlNjItMzgwMTQ2MjIyMDFmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",\
                              "https://www.youtube.com/watch?v=vlTX_ckJ4nM")

friday_night_lights = media.Movie("Friday Night Lights",\
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/Friday_night_lights_ver2.jpg/220px-Friday_night_lights_ver2.jpg",\
                                  "https://www.youtube.com/watch?v=O-mI9GajrBc")

moneyball = media.Movie("Moneyball",\
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxOTU3Mzc1M15BMl5BanBnXkFtZTcwMzk1ODUzNg@@._V1_UX182_CR0,0,182,268_AL_.jpg",\
                        "https://www.youtube.com/watch?v=RAG74hfW4pM")

cinderella_man = media.Movie("Cinderella Man",\
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BODEyYmQxZjUtZGQ0NS00ZTAwLTkwOGQtNGY2NzEwMWE0MDc3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",\
                             "https://www.youtube.com/watch?v=VZzqbaYPV6E&t=65s")

cool_runnings = media.Movie("Cool Runnings",\
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxMTQ3MzMwMV5BMl5BanBnXkFtZTgwNTYxNzYxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg",\
                            "https://www.youtube.com/watch?v=1OW_43xMMB0")

we_are_marshall = media.Movie("We are Marshall",\
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwNDczNTg5MF5BMl5BanBnXkFtZTcwNDMwMzEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",\
                              "https://www.youtube.com/watch?v=y3V6Qz3zz4s&t=37s")

space_jam = media.Movie("Space Jam",\
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDgyZTI2YmYtZmI4ZC00MzE0LWIxZWYtMWRlZWYxNjliNTJjXkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UY268_CR8,0,182,268_AL_.jpg",\
                        "https://www.youtube.com/watch?v=IzU0x1tlfSQ")


movies = [remember_the_titans, miracle,\
          field_of_dreams, friday_night_lights,\
          moneyball, cinderella_man, cool_runnings,\
          we_are_marshall, space_jam]

fresh_tomatoes.open_movies_page(movies)
