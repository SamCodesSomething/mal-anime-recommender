from app.mal_api import search_anime_by_title, get_client_id

#script for testing

def main():
    client_id = get_client_id()
    # getting the MAL API Client ID
    title = input("Please enter your MAL Anime Title: ")
    # getting the title of the anime to base recommends offs
    result = search_anime_by_title(title, client_id)
    if result and "data" in result:
        anime_list = result["data"]
        if anime_list:
            print("\nSearch Results:")
            for anime in anime_list[:5]:  # show only top 5 results
                print("-" * 40)
                print(f"Title: {anime['node']['title']}")
                print(f"ID: {anime['node']['id']}")
                print(f"Main Picture: {anime['node'].get('main_picture', {}).get('medium', 'N/A')}")
                print(f"Average rating: {anime['node'].get('mean', 'N/A')}")
                print(f"Number of Episodes: {anime['node'].get('num_episodes', 'N/A')}")
                genres_list = anime['node'].get('genres', []) #need to unpack genres here
                genre_names = [genre.get('name', 'N/A') for genre in genres_list]
                genres_str = ", ".join(genre_names) if genre_names else "N/A"
                print(f"Genres: {genres_str}")
        else:
            print("No results found.")
    else:
        print("Something went wrong with the search.")


if __name__ == "__main__":
    main()