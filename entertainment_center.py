import fresh_tomatoes
import media


#Movie data repository.

toy_story = media.Movie("Toy Story 3",
                        "An animated sequel about a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

monkey_kingdom = media.Movie("Monkey Kingdom",
                             "A documentary about a family of monkeys livin in ancient temple ruins in Sri Lanka.",
                             "https://upload.wikimedia.org/wikipedia/en/d/d3/Monkey_Kingdom_poster.jpg",
                             "https://www.youtube.com/watch?v=0bi8dOHR6Rw")

mcfarland_usa = media.Movie("McFarland USA",
                            "A cross country coach in a small California town transforms a team of athletes into championship contenders.",
                            "https://upload.wikimedia.org/wikipedia/en/1/12/McFarland%2C_USA_poster.jpg",
                            "https://www.youtube.com/watch?v=j-VAOlHGE6Q")

big_hero = media.Movie("Big Hero 6",
                       "An animated superhero comedy film about a robot.",
                       "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")

planes_fr = media.Movie("Planes: Fire & Rescue",
                        "An animated comedy-adventure film. It is a sequel to the 2013 film Planes.",
                        "https://upload.wikimedia.org/wikipedia/en/c/cc/Planes_Fire_%26_Rescue_poster.jpg",
                        "https://www.youtube.com/watch?v=Uk0D5L0TT30")

cinderella = media.Movie("Cinderella",
                         "A romantic fantasy film based on the fairytale Cinderella.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c2/Cinderella_2015_official_poster.jpg",
                         "https://www.youtube.com/watch?v=20DF6U1HcGQ")
                        
                       
# Store the movie objects in an array.
movies = [toy_story, monkey_kingdom, mcfarland_usa, big_hero, planes_fr, cinderella]

# Initialize web page and display the movies data.
fresh_tomatoes.open_movies_page(movies)


