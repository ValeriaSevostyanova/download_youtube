from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        return("Download is completed successfully")
    except:
        return("An error has occurred")
    

link = input("Enter the YouTube video URL: ")
try:
    print(Download(link))

except Exception as e:
    print("Error! Try again!")
    
