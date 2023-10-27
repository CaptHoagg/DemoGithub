# một cái app có thể đọc ghi file
# có 3 options:

# xem playlist
# file txt lưu tất cả các bài hát đã được người dùng nhập vào từ trước
# thêm bài hát vào playlist
# thêm bài này vào file txt luôn
# chạy một bài trong playlist và nhấn play
# call được browser để chạy

def display_mainmenu():
    print("Welcome to Nhynhi App")
    print("1. Add song to playlist")
    print("2. Show playlist")
    print("3. Play song")
    # this fuction is created to display the menu of our console app
    pass


def add_song_to_playlist():
    song_name = input("Please enter the name of the song:")
    song_url = input("Please enter the url of the song:")
    with open("data.txt", "a") as data_file:
        data_file.write(f"Song Name: {song_name}\n")
        data_file.write(f"Song URL: {song_url}\n")

    print(f"{song_name} has been added to the playlist.")
    # require user to enter the name of the song
    # require user to enter the url of the song
    # save the data to txt file
    pass


def show_playlist():
    # read the txt file
    # print out all name of song in the playlist

    try:
        with open("data.txt", "r") as data_file:
            song = data_file.read()
        
        song_2 = song.split("\n\n")
        
        if song_2:
            print("Songs in the Playlist:")
            for entry in song_2:
                lines = entry.strip().split("\n")
                for line in lines:
                    if line.startswith("Song Name:"):
                        song_name = line[len("Song Name: "):]
                        print(song_name)
    except FileNotFoundError:
        print("The playlist is empty. Please add songs first.")

    pass


def play_song():
    # require user to enter the id of the song
    # play that song
    pass


def user_option():
    # require user to exactly enter the right option (1-2-3)
    # if 1 -> show playlist
    # if 2 -> add song to playlist
    # if 3 -> play a song in playlist
    pass


def main():
    # this is the main function of the app, use this to handle all your application
    pass


main()
