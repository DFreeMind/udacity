import fresh_tomatoes
import media

# create movies

matrix = media.Movie("The Matrix Revolutions",
					"It was the third installment of the Matrix trilogy, released six months following The Matrix Reloaded.",
					"https://upload.wikimedia.org/wikipedia/en/3/34/Matrix_revolutions_ver7.jpg",
					"https://www.youtube.com/watch?v=KSf_D2EubVg",
					"Lana Wachowski",
					"Keanu Reeves",
					"5 November 2003",
					"129 min")

avatar = media.Movie("Avatar",
					"It was the third installment of the Matrix trilogy, released six months following The Matrix Reloaded.",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=dHRIVioj8l0",
					"James Cameron",
					"Sam Worthington",
					"4 January 2010",
					"162 min")

swiss = media.Movie("Swiss Army Man",
					"A hopeless man stranded on a deserted island befriends a dead body and together they go on a surreal journey to get home.",
					"https://upload.wikimedia.org/wikipedia/en/7/72/Swiss_Army_Man_poster.png",
					"https://www.youtube.com/watch?v=yrK1f4TsQfM",
					"Dan Kwan (as Daniel Kwan), Daniel Scheinert",
					"Paul Dano, Daniel Radcliffe",
					"22 September 2017",
					"97 min")

dressmaker = media.Movie("The dressmaker",
					"A glamorous woman returns to her small town in rural Australia. With her sewing machine and haute couture style, she transforms the women and exacts sweet revenge on those who did her wrong.",
					"https://upload.wikimedia.org/wikipedia/en/f/fa/The_Dressmaker_film_poster.jpg",
					"https://www.youtube.com/watch?v=RbQwcCrqwKk",
					"Jocelyn Moorhouse",
					"Kate Winslet, Judy Davis",
					"29 October 2015 (Australia) ",
					"119 min")

watchmen = media.Movie("Watchmen",
					"In 1985 where former superheroes exist, the murder of a colleague sends active vigilante Rorschach into his own sprawling investigation, uncovering something that could completely change the course of history as we know it.",
					"https://upload.wikimedia.org/wikipedia/en/a/a2/Watchmen%2C_issue_1.jpg",
					"https://www.youtube.com/watch?v=PVjA0y78_EQ",
					"Zack Snyder",
					"Jackie Earle Haley, Patrick Wilson",
					"28 March 2009 (Japan)",
					"162 min")

seediq_bale = media.Movie("Warriors of the Rainbow: Seediq Bale I",
					"An indigenous clan-based people living in harmony with nature find their way of life threatened when violent interlopers from another culture arrive, intent on seizing their natural resources and enslaving them.",					
					"https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=169fbdbfc65c10383073c690d378f876/9a504fc2d56285351a126f8490ef76c6a6ef63a1.jpg",
					"https://www.youtube.com/watch?v=u_ocnUbrVd0",
					"Te-Sheng Wei",
					"Masanobu Ando, Jun'ichi Haruta",
					"10 May 2012 (China)",
					"144 min")

# create store movies List
movies = [matrix, avatar, swiss, dressmaker, watchmen, seediq_bale ]

# open movies page
fresh_tomatoes.open_movies_page(movies)









