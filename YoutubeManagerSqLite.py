import sqlite3


conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()


cursor.execute(
    """
    create table if not exists videos (
                id integer primary key,
                name text not null,
                time text not null
    )
"""
)


def list_videos():
    cursor.execute("Select * from videos")
    for row in cursor.fetchall():
        print(row)
    else:
        print("Empty database")


def add_video(name, time):
    cursor.execute("Insert into videos(name, time) values (?,?)", (name, time))
    conn.commit()


def update_video(new_name, new_time, video_id):
    cursor.execute(
        "Update videos set name=?, time=?  where id=?", (new_name, new_time, video_id)
    )
    conn.commit()


def delete_video(video_id):
    cursor.execute("Delete from videos where id=?", (video_id,))
    conn.commit()


def main():

    while True:
        print("\n youtube manager app with DB")
        print("\n 1. List Videos")
        print("\n 2. Add Videos")
        print("\n 3. Update Videos")
        print("\n 4. Delete Videos")
        print("\n 5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
