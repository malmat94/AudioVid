from settings import Settings
from audio_editor import AudioEditor
from downloader_n_extractor import Downloader, Extractor
import json

while True:
    print("Witamy w programie AudioVid")
    print("")
    print("Menu główne:")

    print("""  1. Pobierz film z YouTube
  2. Wygeneruj plik audio z pliku video
  3. Edytuj plik audio
  4. Ustawienia""")
    print("")
    main_action = input("      Wybór: ")

    if main_action == "1":

        while True:

            link = input("Podaj link do filmu: ")
            settings_file = "settings.json"
            with open(settings_file) as sf:
                path = json.load(sf)

            download = Downloader(link, path)
            download.yt_downloader()

            acc_1 = input("Ściągamy dalej? (t/n): ")

            if acc_1 == "t":
                link = input("Podaj link do filmu: ")
                settings_file = "settings.json"
                with open(settings_file) as sf:
                    path = json.load(sf)

                download = Downloader(link, path)
                download.yt_downloader()

            else:
                break

    elif main_action == "2":

        vid_location = input("Podaj lokalizację pliku video: ")

        extract = Extractor(vid_location)
        extract.mp3_extractor()

    elif main_action == "3":

        audio_path = input("Podaj lokalizację pliku audio: ")
        cut_start = input("Podaj początkowy czas przycięcia (min:sec): ")
        cut_ending = input("Podaj końcowy czas przycięcia (min:sec): ")

        cutter = AudioEditor(audio_path)
        cutter.audio_cutter(cut_start, cut_ending)

    elif main_action == "4":

        save_path = input("Wprowadź ścieżkę gdzie chcesz zapisywać ściągane filmy, lub wciśnij 'Enter' dla domyślnej ścieżki (/Dwonloads): ")

        save = Settings()
        save.downolad_settings(save_path)

    elif main_action == "":
        break

close = input("Wcisnij Enter żeby zaknąć program")

