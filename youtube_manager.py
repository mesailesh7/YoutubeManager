import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test =  json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)



def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']},"
              f"duration: {video['time']} ")
    print('\n')
    print("*" * 70)

def add_video(videos):
    name = input("enter video name")
    time = input("Enter video time")
    videos.append({"name":name, "time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index < len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")
        videos[index -1] = {"name":name, "time":time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete"))
    if 1 <= index < len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()

    while True:
        print('\n Youtube Manager | Choose an option')
        print('\n 1. List all youtube videos ')
        print('\n 2. Add a video ')
        print('\n 3. Update a youtube video details ')
        print('\n 4. Remove a video ')
        print('\n 5. Exit the app')
        choice = input("Enter your choice: ")
        # print(videos)


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
                # checks everthing else in new python language
            case _:
                print("Invalid choice")

if __name__ == '__main__':
    main()