import json

def load_data():
    # there is try except and finally
    try:
        with open('youtubes.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtubes.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']},"
              f"duration: {video['duration']}")

def add_video(videos):
    title = input("Enter your name: ")
    duration = input("Enter your duration: ")
    videos.append({"title": title, "duration": duration})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter index of video to update: "))
    if 1 <= index < len(videos):
        title = input("Enter new video name: ")
        duration = input("Enter new video duration: ")
        videos[index - 1] = {"title": title, "duration": duration}
        save_data_helper(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter index of video to delete: "))
    if 1 <= index < len(videos):
        del videos[index -1]
        save_data_helper(videos)
        print("Video deleted")
        print(videos)
    else:
        print("Invalid index")




def main():
    videos = load_data()

    while True:
        print('\n Youtube Manager | choose an option')
        print('\n 1. List all youtube Videos')
        print('\n 2. Add a video')
        print('\n 3. update a video')
        print('\n 4 remove a video')
        print('\n 5. exit the program')
        choice = input('Enter your choice: ')



        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid choice')


if __name__ == '__main__':
    main()