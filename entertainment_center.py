import media
import fresh_tomatoes

#Starting the movies list
movies = []

#Creating instances of movie
### ADD HERE MORE MOVIES ###

movies.append(media.Movie("Toy Story",
                        "A story of a boy and ggg.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"))

movies.append(media.Movie("Hotel Transilvania 2",
                          " Dracula and his friends try to bring out the monster in his half human, half vampire grandson in order to keep Mavis from leaving the hotel",
                          "http://ia.media-imdb.com/images/M/MV5BMjEzNzc4NzEyMV5BMl5BanBnXkFtZTgwMTAxMDQ2NTE@._V1_UY209_CR0,0,140,209_AL_.jpg",
                          "https://www.youtube.com/watch?v=T3nqmGgnJe8"))

movies.append(media.Movie("Intern",
                    "70-year-old widower Ben Whittaker has discovered that retirement isn't all it's cracked up to be. Seizing an opportunity to get back in the game, he becomes a senior intern at an online fashion site, founded and run by Jules Ostin. ",
                     "http://ia.media-imdb.com/images/M/MV5BMTUyNjE5NjI5OF5BMl5BanBnXkFtZTgwNzYzMzU3NjE@._V1_UY209_CR0,0,140,209_AL_.jpg",
                     "https://www.youtube.com/watch?v=f6dKhzYgksc"))

movies.append(media.Movie("Green Inferno",
                            " A group of student activists travels to the Amazon to save the rain forest and soon discover that they are not alone, and that no good deed goes unpunished. ",
                            "http://ia.media-imdb.com/images/M/MV5BMTE0MjgzMjk5MzdeQTJeQWpwZ15BbWU4MDM5OTM1MTYx._V1_UY209_CR1,0,140,209_AL_.jpg",
                            "https://www.youtube.com/watch?v=FcpYPu9M3bw"))


#Calling the function that will create the html
fresh_tomatoes.open_movies_page(movies)
