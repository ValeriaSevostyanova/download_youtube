from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print("Download is completed successfully")
    except:
        print("An error has occurred")
    

link = input("Enter the YouTube video URL: ")
print(Download(link))
