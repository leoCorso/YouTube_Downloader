
import pytube.exceptions
import os
from pytube import YouTube
from pytube import Playlist
import time
class YouTubeDownloader:
    url = None
    file_path = None
    download_type = None

    def menu(self):
        choice = None
        while choice != '3':
            choice = input(f'[1] - DOWNLOAD SINGLE VIDEO\n[2] - DOWNLOAD PLAYLIST\n[3] - QUIT\n> ').strip()
            if choice == '1':
                self.download_single()
            elif choice == '2':
                self.download_playlist()
            elif choice == '3':
                return
            else:
                print('PLEASE ENTER A VALID OPTION ONLY!')

    def download_single(self):
        os.system('cls')
        self.url = input(f'ENTER YOUTUBE URL: ').strip()
        self.file_path = input(f'ENTER SAVE PATH:').strip()

        os.system('cls')
        self.download_type = input(f'[1] - VIDEO + AUDIO\n[2] - AUDIO ONLY\n> ').strip()

        if self.download_type == '1':
             self.download_video()
        elif self.download_type == '2':
             self.download_audio()

    def download_playlist(self):
        os.system('cls')
        self.url = input(f'ENTER YOUTUBE PLAYLIST URL: ').strip()
        self.file_path = input(f'ENTER SAVE PATH: ').strip()
        os.system('cls')
        self.download_type = input(f'[1] - VIDEO + AUDIO\n[2] - AUDIO ONLY\n> ').strip()

        if self.download_type == '1':
            self.download_playlist_video()
        elif self.download_type == '2':
            self.download_playlist_audio()

    def download_playlist_video(self):
        resolutions = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']

        while True:
            os.system('cls')
            res_choice = input('ENTER [1] - TO DOWNLOAD HIGHEST RESOLUTION\n'
                               'OR\nENTER DESIRED RESOLUTION IN THIS FORM 1080p\n> ').strip()
            os.system('cls')
            try:
                time.sleep(2)
                if res_choice == '1':
                    video_playlist = Playlist(self.url)
                    #  Catch an invalid playlist here if not done already
                    for video in video_playlist.videos:
                        video = video.streams.filter().get_highest_resolution()
                        video.download(self.file_path)
                        print(f'DOWNLOADED [{video.title}]')
                    os.system('cls')
                    print(f'FINISHED DOWNLOADING [{video_playlist.title}]')
                    time.sleep(2)
                    os.system('cls')
                    return True
                else:
                    res_change = False
                    if res_choice in resolutions:
                            video_playlist = Playlist(self.url)
                            for video in video_playlist.videos:
                                while not video.streams.filter(res=res_choice):
                                    res_choice = input(f'INVALID RESOLUTION FOR [{video.title}]\n'
                                                       f'ENTER ANOTHER IN THE FORM 1080p:').strip()
                                    os.system('cls')
                                    res_change = True
                                else:
                                    video = video.streams.filter(res=res_choice).first()
                                    video.download(self.file_path)
                                    print(f'DOWNLOADED [{video.title}]')

                                    if res_change:
                                        res_choice = input('ENTER RESOLUTION FOR THE REMAINING VIDEOS: ').strip()
                                    res_change = False
                            os.system('cls')
                            print(f'FINISHED DOWNLOADING [{video_playlist.title}]')
                            time.sleep(2)
                            os.system('cls')
                            return True
                    else:
                        raise AttributeError

            except KeyError:
                os.system('cls')
                print(f'COULD NOT FIND PLAYLIST: [{self.url}]')
                time.sleep(2)
                os.system('cls')
                return False
            except pytube.exceptions.RegexMatchError:
                os.system('cls')
                print(f'COULD NOT FIND PLAYLIST [{video_playlist.playlist_url}]')
                time.sleep(2)
                os.system('cls')
                return False
            except AttributeError:
                os.system('cls')
                print(f'RESOLUTION {res_choice} NOT FOUND FOR [{self.url}]!')
                time.sleep(2)
                os.system('cls')

    def download_playlist_audio(self):
        qualities = ['384kbps', '192kbps', '160kbps', '128kbps', '70kbps', '48kbps']

        while True:
            os.system('cls')
            quality_choice = input('ENTER [1] - TO DOWNLOAD HIGHEST RESOLUTION\n'
                               'OR\nENTER DESIRED RESOLUTION IN THIS FORM 384kbps\n> ').strip()
            os.system('cls')

            try:
                if quality_choice == '1':
                    audio_playlist = Playlist(self.url)
                    for audio in audio_playlist.videos:
                        for quality in qualities:
                            if audio.streams.filter(abr=quality, only_audio=True):
                                audio = audio.streams.filter(abr=quality, only_audio=True).first()
                                break
                        audio.download(self.file_path)
                        print(f'DOWNLOADED [{audio.title}]')
                    os.system('cls')
                    print(f'FINISHED DOWNLOADING [{audio_playlist.title}]')
                    time.sleep(2)
                    return True
                else:
                    quality_change = False
                    if quality_choice in qualities:
                            audio_playlist = Playlist(self.url)
                            for audio in audio_playlist.videos:
                                while not audio.streams.filter(abr=quality_choice, only_audio=True):
                                    quality_choice = input(f'INVALID RESOLUTION FOR [{audio.title}]\n'
                                                       f'ENTER ANOTHER IN THE FORM 384kbps:').strip()
                                    quality_change = True
                                else:
                                    audio = audio.streams.filter(abr=quality_choice, only_audio=True).first()
                                    audio.download(self.file_path)
                                    print(f'DOWNLOADED [{audio.title}]')
                                    if quality_change:
                                        quality_choice = input('ENTER RESOLUTION FOR THE REMAINING VIDEOS: ').strip()
                                    quality_change = False
                            os.system('cls')
                            print(f'FINISHED DOWNLOADING [{audio_playlist.title}]')
                            time.sleep(2)
                            os.system('cls')
                            return True
                    else:
                        raise AttributeError

            except KeyError:
                os.system('cls')
                print(f'COULD NOT FIND PLAYLIST: [{self.url}]')
                time.sleep(2)
                os.system('cls')
                return False
            except pytube.exceptions.RegexMatchError:
                os.system('cls')
                print(f'COULD NOT FIND PLAYLIST [{audio_playlist.playlist_url}]')
                time.sleep(2)
                os.system('cls')
                return False
            except AttributeError:
                os.system('cls')
                print(f'QUALITY {quality_choice} NOT FOUND FOR [{self.url}]!')
                time.sleep(2)
                os.system('cls')

    def download_video(self):
        os.system('cls')
        resolutions = ['2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p']

        while True:
            res_choice = input('ENTER [1] - TO DOWNLOAD HIGHEST RESOLUTION\n'
                               'OR\nENTER DESIRED RESOLUTION IN THIS FORM 1080p\n> ').strip()
            try:
                if res_choice == '1':
                    video = YouTube(self.url).streams.filter().get_highest_resolution()
                    video.download(self.file_path)
                    os.system('cls')
                    print(f'DOWNLOADED [{video.title}]')
                    time.sleep(2)
                    os.system('cls')
                    return True
                else:
                    if res_choice in resolutions:
                        video = YouTube(self.url).streams.filter(res=res_choice)
                        video = video.first().download(self.file_path)
                        os.system('cls')
                        print(f'DOWNLOADED [{video.title}]')
                        time.sleep(2)
                        os.system('cls')
                        return True
                    else:
                        raise AttributeError
            except pytube.exceptions.RegexMatchError:
                os.system('cls')
                print(f'COULD NOT FIND VIDEO [{self.url}]')
                time.sleep(2)
                os.system('cls')
                return False
            except AttributeError:
                os.system('cls')
                print(f'RESOLUTION {res_choice} NOT FOUND FOR [{self.url}]!')
                time.sleep(2)
                os.system(2)

    def download_audio(self):
        qualities = ['384kbps', '192kbps', '160kbps', '128kbps', '70kbps', '48kbps']

        while True:
            audio_choice = input('ENTER [1] - TO DOWNLOAD HIGHEST QUALITY\n'
                                 'OR\nENTER DESIRED QUALITY IN THIS FORM 384kbps\n> ').strip()
            try:
                if audio_choice == '1':
                    for audio in qualities:
                        try:
                            yt = YouTube(self.url).streams.filter(only_audio=True, abr=audio)
                            return True
                        except pytube.exceptions.RegexMatchError:
                            pass
                else:
                    if audio_choice in qualities:
                        yt = YouTube(self.url).streams.filter(abr=audio_choice, only_audio=True)
                        yt.first().download(self.file_path)
                        return True
                    else:
                        raise AttributeError
            except pytube.exceptions.RegexMatchError:
                print('COULD NOT FIND VIDEO')
                return False
            except AttributeError:
                print(f'RESOLUTION {audio_choice} NOT FOUND!')


Instance = YouTubeDownloader()
Instance.menu()
