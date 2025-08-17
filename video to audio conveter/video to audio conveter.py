import moviepy as py

video = py.editor.VideoFileClip("video.mp4")
audio = video.audio
audio.write_audiofile("audio.mp3")
video.close()
audio.close()