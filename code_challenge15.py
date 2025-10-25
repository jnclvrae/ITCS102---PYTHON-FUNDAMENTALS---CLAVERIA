#codechallenge15
#animelistingprogram

anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")

    if anime.lower() == "exit":
        print("You have exited the anime entry program.")
        break  # stop the loop

    anime_list.append(anime) 
    print(f"'{anime}' has been added to your anime list.")

print("\nYour anime list includes:")
for x in anime_list:
    print(f"- {x}")
