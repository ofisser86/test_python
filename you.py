from pytube import YouTube
import pysubs2


yt = YouTube('https://www.youtube.com/watch?v=MukG3jtGZJo')
print(yt.captions.all())
caption = yt.captions.get_by_language_code('ru')
# caption.xml_captions

with open('test3.srt', '+w') as f:
    f.write(caption.generate_srt_captions())
# print(caption.generate_srt_captions())

# subs = pysubs2.load("sub.srt")
# print(subs)
