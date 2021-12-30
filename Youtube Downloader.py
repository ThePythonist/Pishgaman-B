from pytube import YouTube

#ask for the link from user
link = "https://www.youtube.com/watch?v=Lli99OmkPwM"
video = YouTube(link)

#Showing details
print("Title: ", video.title)
print("Number of views: ", video.views)
print("Length of video: ", video.length)
print("Rating of video: ", video.rating)
#Getting the highest resolution possible
Video = video.streams.get_highest_resolution()

#Starting download
print("Downloading...")
Video.download()
print("Download completed!!")