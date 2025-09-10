#codechallenge5
#mangarecommender

print("Welcome to Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, romance, horror): ").lower()

duration = input("How long should the manga be? (long, medium, short): ").lower()

time = input("From which decade? (2000s, 2010s): ").lower()

if genre == "action":
    if duration == "long":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Naruto, Bleach, Gantz.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: My Hero Academia, Seven Deadly Sins, & Black Clover.")
    if duration == "medium":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Fullmetal Alchemist, Air Gear, & Claymore.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Attack on Titan, Blue Exorcist, & Scraph of the End.")
    if duration == "short":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Black Lagoon, Afro Samurai, & Battle Royale.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Akame ga Kill, Tokyo ESP, & World Trigger.")
        
if genre == "romance":
    if duration == "long":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Boys Over Flowers, & Itazura na Kiss.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Domestic Girlfriend, & Nisekoi.")
    if duration == "medium":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Fruits Basket, & Nana.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Kimi ni Todoke, Horimiya, Say I Love You, & A Town Where You Live.")
    if duration == "short":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Bokura ga Ita, & Kare Kano.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Ao Haru Ride, Strobe Edge, & Orange.")
            
if genre == "horror":
    if duration == "long":
        if time == "2000s" or time == "2000":
            print("There are no mangas available, I'm sorry.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Higanjima, & Berserk.")
    if duration == "medium":
        if time == "2000s" or time == "2000":
            print("The only available manga is: Doubt.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Tokyo Ghoul, Tokyo Ghoul:re, Attack on Titan, & Terra Formars.)
    if duration == "short":
        if time == "2000s" or time == "2000":
            print("The available mangas are: Dragon Head, I Am a Hero, MPD Psycho, & Alive: The Final Evolution.")
        elif time == "2010s" or time == "2010":
            print("The available mangas are: Ajin: Demi-Human, Pupa, Fort of Apocalypse, & Franken Fran.")