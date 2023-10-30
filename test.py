import webbrowser

def main_menu():
    print("1. Add song to playlist")
    print("2. Show playlist")
    print("3. Play song")
    print("4. Exit")  # Added an option to exit
    # This function is created to display the menu of our console app


playlist = []
def add_song_to_playlist():
    song_name = input("Hãy nhập tên bài hát:")
    song_url = input("Hãy nhập URL của bài hát:")
    playlist.append(song_url)
    with open("data.txt", "a") as data_file:
        data_file.write(f"Song Name: {song_name}\n")
        data_file.write(f"Song URL: {song_url}\n")
    
    print(f"{song_name} đã được thêm vào.")
    # Require the user to enter the name of the song and URL
    # Save the data to the text file
    # Add the song url to array 

def show_playlist():
    try:
        with open("data.txt", "r") as data_file:
            song_data = data_file.read()

        song_list = song_data.split("\n\n")

        if song_list:
            print("Songs in the Playlist:")
            for entry in song_list:
                print(entry)
        else:
            print("The playlist is empty. Please add songs first.")
    except FileNotFoundError:
        print("The playlist is empty. Please add songs first.")


def play_song():
    entered_song = input("Hãy chọn nhạc bạn muốn phát:").strip().lower()
    
    try:
        with open("data.txt", "r") as data_file:
            song_data = data_file.read()

        song_list = song_data.split("\n\n")

        found = False  # Flag to track whether the song is found in the playlist.

        for entry in song_list:
            if entered_song in entry.lower():
                webbrowser.open(entry)
                break

        if not found:
            print("Không có trong playlist.")
    
    except FileNotFoundError:
        print("Không có trong playlist.")

def user_option():
    while True:
        main_menu()
        chon = input("Hãy lựa chọn 1->4: ")
        if chon == '1':
            add_song_to_playlist()
        elif chon == '2':
            show_playlist()
        elif chon == '3':
            play_song()
        elif chon == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không có, hãy chọn lựa chọn khác")

def main():
    print("Chào mừng bạn đã đến với app của Nhynhi:")
    user_option()


if __name__ == "__main__":
    main()
