import fresh_tomatoes
import movie

# Base links
wiki_base = "https://upload.wikimedia.org/wikipedia/en/"
youtube_base = "https://www.youtube.com/watch?v="

# Movie objects
drive = movie.Movie("Drive",
                    "An unnamed Hollywood stunt driver moonlights as a "
                    + "getaway driver. After he becomes attracted to a female "
                    + "neighbor whose husband owes money to local gangsters, "
                    + "he is drawn deeper into the dangerous underworld.",
                    wiki_base + "1/13/Drive2011Poster.jpg",
                    youtube_base + "KBiOF3y1W0Y")

creed = movie.Movie("Creed",
                    "Adonis Johnson never knew his famous father, boxing "
                    + "champion Apollo Creed, who died before Adonis was born "
                    + "However, boxing is in his blood, so he seeks out Rocky "
                    + "Balboa and asks the retired champ to be his trainer." ,
                    wiki_base + "2/24/Creed_poster.jpg",
                    youtube_base + "Uv554B7YHk4")

civil_war = movie.Movie("Captain America: Civial War",
                        "Disagreement over international oversight of the "
                        + "Avengers fractures them into opposing factions one "
                        + "led by Steve Rogers and the other by Tony Stark",
                        wiki_base + "5/53/Captain_America_Civil_War_poster.jpg",
                        youtube_base + "dKrVegVI0Us")

spider_man = movie.Movie("The Amazing Spider-Man",
                         "Peter Parker, a teenager from New York who becomes "
                         + "Spider-Man after being bitten by a genetically "
                         + "altered spider",
                         wiki_base +
                         "0/02/The_Amazing_Spider-Man_theatrical_poster.jpeg",
                         youtube_base + "oX9ZT3RbYE4")

the_dark_knight = movie.Movie("The Dark Knight",
                              "Batman has been able to keep a tight lid on "
                              + "crime in Gotham City, but the Joker suddenly "
                              + "throws the town into chaos",
                              wiki_base + "8/8a/Dark_Knight.jpg",
                              youtube_base + "EXeTwQWrcwY")

x_men = movie.Movie("X-Men: Days of Future Past",
                    "Convinced that mutants pose a threat to humanity, "
                    + "Dr. Bolivar Trask develops the Sentinels, enormous "
                    + "robotic weapons that can detect a mutant gene and "
                    + "zero in on that person.",
                    wiki_base + "0/0c/X-Men_Days_of_Future_Past_poster.jpg",
                    youtube_base + "pK2zYHWDZKo")

fight_club = movie.Movie("Fight Club",
                         "An 'everyman' who is discontented with his "
                         + "white-collar job forms a 'fight club' with "
                         + "soap maker Tyler Durden.",
                         wiki_base + "f/fc/Fight_Club_poster.jpg",
                         youtube_base + "SUXWAEX2jlg")

the_matrix = movie.Movie("The Matrix",
                         "A dystopian future in which reality as perceived "
                         + "by most humans is actually a simulated reality "
                         + "called 'the Matrix', created by sentient machines "
                         + "to subdue the human population",
                         wiki_base + "c/c1/The_Matrix_Poster.jpg",
                         youtube_base + "vKQi3bBA1y8")

john_wick = movie.Movie("John Wick",
                        "John Wick, a retired hitman seeking vengeance for "
                        + "the theft of his vintage car and the killing of "
                        + "his puppy, a gift from his recently deceased wife.",
                        wiki_base + "9/98/John_Wick_TeaserPoster.jpg",
                        youtube_base + "C0BMx-qxsP4")

inception = movie.Movie("Inception",
                        "A professional thief who commits corporate espionage "
                        + "by infiltrating the subconscious of his targets. "
                        + "is offered a chance to have his criminal history "
                        + "erased as payment for a task considered to be "
                        + "impossible: 'inception'",
                        wiki_base + "7/7f/Inception_ver3.jpg",
                        youtube_base + "8hP9D6kZseM")

the_nice_guys = movie.Movie("The Nice Guys",
                            "Holland March is a down-on-his-luck private eye "
                            + "in 1977 Los Angeles. Jackson Healy is a hired "
                            + "enforcer who hurts people for a living. Fate "
                            + "turns them into unlikely partners after a "
                            + "young woman named Amelia disappears.",
                            wiki_base + "e/e9/The_Nice_Guys_poster.png",
                            youtube_base + "MxW4LZCYfvs")

shutter_island = movie.Movie("Shutter Island",
                             "The implausible escape of a brilliant murderess "
                             + "brings U.S. Marshal Teddy Daniels and his new "
                             + "partner to Ashecliffe Hospital, a "
                             + "fortress-like insane asylum located on a "
                             + "remote, windswept island.",
                             wiki_base + "7/76/Shutterislandposter.jpg",
                             youtube_base + "5iaYLCiq5RM")
world_war_z = movie.Movie("World War Z",
                          "Gerry Lane, a former United Nations investigator "
                          + "who must travel the world to find a way to stop "
                          + "a zombie pandemic.",
                          wiki_base + "d/dc/World_War_Z_poster.jpg",
                          youtube_base + "HcwTxRuq-uk")

tropic_thunder = movie.Movie("Tropic Thunder",
                             "When their frustrated director decides to drop "
                             + "them in the middle of a jungle, they are "
                             + "forced to rely on their acting skills in "
                             + "order to survive the real action and danger.",
                             wiki_base + "d/d6/Tropic_thunder_ver3.jpg",
                             youtube_base + "T-6YhRZowgc")

social_network = movie.Movie("The Social Network",
                             "Harvard undergrad and computer genius "
                             + "Mark Zuckerberg begins work on a new "
                             + "concept that eventually turns into the "
                             + "global social network known as Facebook.",
                             wiki_base + "7/7a/Social_network_film_poster.jpg",
                             youtube_base + "lB95KLmpLR4")

avengers_ultron = movie.Movie("Avengers 2: Age of Ultron",
                              "The Avengers fight Ultron, an artificial "
                              + "intelligence obsessed with causing "
                              + "human extinction",
                              wiki_base + "1/1b/Avengers_Age_of_Ultron.jpg",
                              youtube_base + "JAUoeqvedMo")

toy_story_three = movie.Movie("Toy Story 3",
                              "Toys Woody, Buzz Lightyear, and their friends "
                              + "dealing with an uncertain future as their "
                              + "owner, Andy, prepares to leave for college.",
                              wiki_base + "6/69/Toy_Story_3_poster.jpg",
                              youtube_base + "TNMpa5yBf5o")

simpsons_movie = movie.Movie("The Simpsons Movie",
                             "Homer Simpson, whose irresponsibility gets the "
                             + "better of him when he pollutes the lake in "
                             + "Springfield after the town cleans it up when "
                             + "they had received a warning from the EPA",
                             wiki_base + "a/a0/Simpsons_final_poster.png",
                             youtube_base + "PulHR2LfPVk")

# Store movie objects into an Array
movie_list = [
              drive,
              creed,
              civil_war,
              spider_man,
              the_dark_knight,
              x_men,
              fight_club,
              the_matrix,
              john_wick,
              inception,
              the_nice_guys,
              shutter_island,
              world_war_z,
              tropic_thunder,
              social_network,
              avengers_ultron,
              toy_story_three,
              simpsons_movie
              ]

# Pass the movie array into 'fresh_tomatoes'
fresh_tomatoes.open_movies_page(movie_list)