
import json
from kivy.lang import Builder
from path_fixer import PathFixer

Builder.load_file("settings.kv")

class Settings():
    """App setting's class"""

    def __init__(self):

        self.settingsname = "settings.json"

    def downolad_settings(self, vid_path):

        if vid_path == "":

            with open(self.settingsname, "w") as sf:
                json.dump("Downloads/", sf)

        else:
            fix = PathFixer(vid_path)
            fixed_vid_sp = fix.path_converter()

            with open(self.settingsname, "w") as sf:
                json.dump(fixed_vid_sp, sf)

# raw_path = input("Wprowadź ścieżkę:  ")
# test = Settings()
# test.downolad_settings(raw_path)


