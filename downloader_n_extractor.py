from pytube import YouTube
from path_fixer import PathFixer
import moviepy.editor as mp
import json


class Downloader():

    """Class for downloading YouTube viedos"""

    def __init__(self, link, save_location):

        self.link = link
        self.save_location = save_location
        self.path_fixer = PathFixer(save_location)
        self.fixed_save_location = self.path_fixer.path_converter()
        self.vid_path_list = []
        self.vid_path =""

    def yt_downloader(self):
        """Download YT highest resolution video into specific location"""

        yt = YouTube(self.link)
        vid_name = yt.title
        ys = yt.streams.get_highest_resolution()

        ys.download(self.fixed_save_location)

        self.vid_path = self._vid_name_generator(vid_name)

        return self.vid_path

    def _vid_name_generator(self, vid_name):
        """Generates path to downloaded video"""
        vid_path_list = [self.fixed_save_location, "/", vid_name, ".mp4"]
        vid_path = "".join(vid_path_list)

        return vid_path

class Extractor():

    """Class for extracting audio files (mp3) from videos (mp4)"""
    def __init__(self, vid_path):

        self.vid_path = vid_path
        self.path_fixer = PathFixer(vid_path)
        self.fixed_vid_path = self.path_fixer.path_converter()

    def mp3_extractor(self):
        """Extract mp3 file from mp4 file"""

        audio_file = mp.VideoFileClip(self.fixed_vid_path)
        audio_file_path = self._mp4_to_mp3_name_changer_(self.fixed_vid_path)
        audio_file.audio.write_audiofile(audio_file_path)

    def _mp4_to_mp3_name_changer_(self, vid_path):
        """Exchange file extention from .mp4 to .mp3"""

        audio_name = list(vid_path)
        audio_name.pop()
        audio_name.append("3")
        audio_name = "".join(audio_name)

        return audio_name



# settings_file = "settings.json"
# with open(settings_file) as sf:
#     path = json.load(sf)
#
# test_down = Downloader("https://www.youtube.com/watch?v=Ue3x6nbke1s&ab_channel=SamC.", path)
# test_down.yt_downloader()
#
# mp4_path = input("Wprowadź ścieżkę do filmu: ")
# test_extr = Extractor(mp4_path)
# test_extr.mp3_extractor()


