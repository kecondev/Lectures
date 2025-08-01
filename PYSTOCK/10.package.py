# from multimedia import video, audio

# print(video.play_video())
# print(audio.play_audio())

# from package.audio import play_audio as pa
# from package.video import play_video as pv

# print(pa())
# print(pv())

from package import audio as au
from package import video as vi

print(au.play_audio())
print(vi.play_video())