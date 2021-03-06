from settings import Settings
from audio_editor import AudioEditor
from downloader_n_extractor import Downloader, Extractor
import json
import os
print("Witamy w programie AudioVid")

while True:
    print("")
    print("Menu główne:")

    print("""  1. Pobierz film z YouTube
  2. Wygeneruj plik audio z pliku video
  3. Przytnij plik audio
  4. Ustawienia
  ENTER - zamknij program""")
    print("")
    main_action = input("Wybór: ")

    if main_action == "1":

        print("")
        link = input("Podaj link do filmu: ")
        settings_file = "settings.json"
        with open(settings_file) as sf:
            path = json.load(sf)

        download = Downloader(link, path)
        download.yt_downloader()
        dwn_vid_path = os.path.abspath(download.vid_path)

        print("")
        print("GOTOWE!")
        print("Plik znajduje się w: " + dwn_vid_path)
        print("")

    elif main_action == "2":

        vid_location = input("Podaj lokalizację pliku video: ")

        extract = Extractor(vid_location)
        extract.mp3_extractor()

    elif main_action == "3":

        audio_path = input("Podaj lokalizację pliku audio: ")
        cutter = AudioEditor(audio_path)
        print("")
        print("Długośc pliku audio wynosi: " + str(cutter.audio_length) + "s")
        print("")
        cut_start = input("Podaj początkowy czas przycięcia (np. 01:00) : ")
        cut_ending = input("Podaj końcowy czas przycięcia (np. 02:00): ")

        cutter.audio_cutter(cut_start, cut_ending)
        edt_aud_path = os.path.abspath(cutter.afc_path)

        print("")
        print("GOTOWE!")
        print("Plik znajduje się w: " + edt_aud_path)
        print("")


    elif main_action == "4":

        save_path = input("Wprowadź ścieżkę gdzie chcesz zapisywać ściągane filmy, lub wciśnij 'Enter' dla domyślnej ścieżki (/Dwonloads): ")

        save = Settings()
        save.downolad_settings(save_path)

    elif main_action == "":
        break

close = input("Wcisnij Enter żeby potwierdzić zamknięcie programu")

