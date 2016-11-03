import fresh_tomatoes
import media
# Passing Arguments int o the Movie class for avatar instance
avatar = media.Movie(
    "Avatar",
    "http://www.chud.com/wp-content/uploads/2013/08/Avatar-Wallpaper-Neytiri7.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY",
    "avatar movie review")
# Passing Arguments int o the Movie class for toystory instance
toystory = media.Movie(
    "Toy story",
    "http://www.deckchaircinema.com/wp-content/uploads/2016/05/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    "toy-story story line")
# Passing Arguments int o the Movie class for schoolofrock  instance
schoolofrock = media.Movie(
    "schoolofrock",
    "https://thenypost.files.wordpress.com/2016/03/tv_school1a.jpg?quality=90&strip=all&w=978&h=652&crop=1",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
    "school of rock ")
# Passing Arguments int o the Movie class for  tamasha instance
tamasha = media.Movie(
    "Tamasha",
    "http://bollywoodmoviereview.in/wp-content/uploads/2015/09/tamasha.jpg",
    "https://www.youtube.com/watch?v=VN_qxutU_qc",
    "tamashs")
# Passing Arguments int o the Movie class for wolfofwallstreet instance
wolfofwallstreet = media.Movie(
    "Wolf Of Wallstreet",
    "http://dl9fvu4r30qs1.cloudfront.net/ff/4a/63426bb14b9db6eeff05b0e1c441/the-wolf-of-wall-street.jpg",
    "https://www.youtube.com/watch?v=pabEtIERlic",
    "Wolf of Wallstreet")

agent_vinod = media.Movie(
    "Agent Vinod",
    "http://c.saavncdn.com/603/Agent-Vinod-2012-500x500.jpg",
    "https://www.youtube.com/watch?v=OMQro-vPKz0",
    "agent_vinod story line")
# Passing arguments in movies
movies = [
    avatar,
    toystory,
    schoolofrock,
    tamasha,
    wolfofwallstreet,
    agent_vinod]
fresh_tomatoes.open_movies_page(movies)
