import media
import fresh_tomatoes
#media - class file for movies
#fresh_tomatoes - code provided to format html and open page in browser

#List of favorite movies
#variables: Title, Description, Box Art Image URL,
# Trailer URL on Youtube, Year released, MPAA Rating

silence_of_the_lambs = media.Movie("The Silence of the Lambs",
                                   """A young F.B.I. cadet must confide in an "
                                   "incarcerated and manipulative killer to "
                                   "receive his help on catching another "
                                   "serial killer who skins his victims.""",
                                   "http://ia.media-imdb.com/images/M/MV5BMTQ2NzkzMDI4OF5BMl5BanBnXkFtZTcwMDA0NzE1NA@@._V1_SX214_AL_.jpg",
                                   "https://www.youtube.com/watch?v=W6Mm8Sbe__o",
                                   "1991",
                                   "R"
                                   )
shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   """Two imprisoned men bond over a number of "
                                   "years, finding solace and eventual "
                                   "redemption through acts of common "
                                   "decency.""",
                                   "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
                                   "https://www.youtube.com/watch?v=NmzuHjWmXOc",
                                   "1994",
                                   "R"
                                   )
godfather = media.Movie("The Godfather",
                        """The aging patriarch of an organized crime dynasty "
                        "transfers control of his clandestine empire to his "
                        "reluctant son.""",
                        "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=o_DEzxd2R3Y",
                        "1972",
                        "R"
                        )
godfather2 = media.Movie("The Godfather Part II",
                         """The early life and career of Vito Corleone in "
                         "1920s New York is portrayed while his son, Michael, "
                         "expands and tightens his grip on his crime syndicate "
                         "stretching from Lake Tahoe, Nevada to pre-revolution "
                         "1958 Cuba.""",
                         "http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl5BMl5BanBnXkFtZTcwMTA5Mzg3OA@@._V1_SX214_AL_.jpg",
                         "https://www.youtube.com/watch?v=qJr92K_hKl0",
                         "1974",
                         "R"
                         )
pulp_fiction = media.Movie("Pulp Fiction",
                           """The lives of two mob hit men, a boxer, a "
                           "gangster's wife, and a pair of diner bandits "
                           "intertwine in four tales of violence and "
                           "redemption.""",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           "1994",
                           "R"
                           )
memento = media.Movie("Memento",
                      """A man creates a strange system to help him remember "
                      "things; so he can hunt for the murderer of his wife "
                      "without his short-term memory loss being an obstacle.""",
                      "http://ia.media-imdb.com/images/M/MV5BMTc4MjUxNDAwN15BMl5BanBnXkFtZTcwMDMwNDg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=ploSYVE0uao",
                      "2000",
                      "R"
                      )
kill_bill = media.Movie("Kill Bill Vol 1",
                        """The Bride wakens from a four-year coma. The child "
                        "she carried in her womb is gone. Now she must wreak "
                        "vengeance on the team of assassins who betrayed her - "
                        "a team she was once part of.""",
                        "http://ia.media-imdb.com/images/M/MV5BMTU1NDg1Mzg4M15BMl5BanBnXkFtZTYwMDExOTc3._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=7kSuas6mRpk",
                        "2003",
                        "R"
                        )
kill_bill2 = media.Movie("Kill Bill Vol 2",
                         """The Bride continues her quest of vengeance against "
                         "her former boss and lover Bill, the reclusive bouncer "
                         "Budd and the treacherous, one-eyed Elle.""",
                         "http://ia.media-imdb.com/images/M/MV5BMTIwNzQ3MDIxMV5BMl5BanBnXkFtZTcwMDIxMzUyMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=WTt8cCIvGYI",
                         "2004",
                         "R"
                         )
unforgiven = media.Movie("Unforgiven",
                         """Retired Old West gunslinger William Munny reluctantly "
                         "takes on one last job, with the help of his old partner "
                         "and a young man.""",
                         "http://ia.media-imdb.com/images/M/MV5BMTkzNTc0NDc4OF5BMl5BanBnXkFtZTcwNTY1ODg3OA@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                         "https://www.youtube.com/watch?v=XDAXGILEdro",
                         "1992",
                         "R"
                         )
casino = media.Movie("Casino",
                     """Greed, deception, money, power, and murder occur between "
                     "two mobster best friends and a trophy wife over a gambling "
                     "empire.""",
                     "http://ia.media-imdb.com/images/M/MV5BMTMzMjkwMTk4Nl5BMl5BanBnXkFtZTYwNjYxMjk5._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=EJXDMwGWhoA",
                     "1995",
                     "R"
                     )
princess_bride = media.Movie("The Princess Bride",
                             """While home sick in bed, a young boy's grandfather "
                             "reads him a story called The Princess Bride.""",
                             "http://ia.media-imdb.com/images/M/MV5BMTkzMDgyNjQwM15BMl5BanBnXkFtZTgwNTg2Mjc1MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=WNNUcHRiPS8",
                             "1987",
                             "PG"
                             )

#List of movies to call
movies = [silence_of_the_lambs, memento, shawshank_redemption, godfather, godfather2, pulp_fiction, kill_bill, kill_bill2, unforgiven, casino, princess_bride]

#Call open_movies_page in fresh_tomatoes.py to render html and open browser
fresh_tomatoes.open_movies_page(movies)
