# Creating te youtube manager app with sqlite3 or using database sqlite this time

import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    con.commit()       


def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES (?, ?)",(name, time))
    con.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, video_id))
    con.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    con.commit()


def main():
    while True:
        print(" \n YOUTUBE MANAGER app with DB ")
        print("1. List videos ")
        print("2. Add videos")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:     # We can also use if else
            case "1":
                list_videos()

            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name,time)

            case "3":
                video_id = input("Enter the video id to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id,name,time)
                
            case "4":
                video_id = input("Enter the video id to update: ")
                delete_video(video_id)
                
            case "5":
                break

            case _:
                print("Invalid Choice")

    con.close()


if __name__ == "__main__":
    main()

