from kivy.lang import Builder
from pydub import AudioSegment
from path_fixer import PathFixer
from pydub.utils import mediainfo
import os

Builder.load_file("audio_editor.kv")


class AudioEditor():
    """Class for editing audio files"""

    def __init__(self, audio_path):


        self.audio_path = audio_path
        self.path_fixer = PathFixer(audio_path)
        self.fixed_audio_path = self.path_fixer.path_converter()
        self.audio_length = AudioSegment.from_file(self.fixed_audio_path, format="mp3").duration_seconds
        self.afc_path = ""

    def audio_cutter(self, first_cut_point, last_cut_point):
        """Function for cuting audio files"""

        audio_file = AudioSegment.from_file(self.fixed_audio_path, format="mp3")

        cut_points = self._start_ending_converter(first_cut_point, last_cut_point)
        audio_file_cut = audio_file[cut_points[0]:cut_points[1]]
        self.afc_path = self._mp3_eddited_tagger_("(cut)") #giving directory to edited (cut) audio file

        audio_file_cut.export(self.afc_path)

        return self.afc_path

    def audio_volume_editor(self, amount):
        """Function for editing volume of audio files"""

        audio_file = AudioSegment.from_file(self.fixed_audio_path, format="mp3")

        audio_file_ve = audio_file[:] + float(amount)
        afve_path = self._mp3_eddited_tagger_("(edited volume)")

        audio_file_ve.export(afve_path)


    def _mp3_eddited_tagger_(self, statement):
        """Edit audio file name by adding '-edited' tag to the name"""

        edited_audio_path = list(self.fixed_audio_path)
        del edited_audio_path[-4:]
        edited_audio_path.append(f"_edited{(statement)}.mp3")
        edited_audio_path = "".join(edited_audio_path)

        return edited_audio_path

    def _start_ending_converter(self, first, last):
        """converse user input into milisecs understandable for python"""

        f_list = first.split(":")
        l_list = last.split(":")

        f_min = float(f_list[0])
        f_sec = float(f_list[-1])

        l_min = float(l_list[0])
        l_sec = float(l_list[-1])

        f_point = (f_min * 60 + f_sec) * 1000
        l_point = (l_min * 60 + l_sec) * 1000

        result_list = [f_point, l_point]

        return result_list


#Do testowania!
# mp3_path = input("Wprowadź ścieżkę do pliku audio: ")
# str = input("Decybele: ")
# test_extr = AudioEditor(mp3_path)
# test_extr.audio_volume_editor(str)
