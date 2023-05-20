from pydub import AudioSegment
from tkinter import filedialog


class Sound:
    def __init__(self):
        self.filePath = None
        self.track = None
        self.queue = []
        self.stack = []
        self.overlayTrack = None

    def speed_change(self, speed=1.0):
        sound_with_altered_frame_rate = self.track._spawn(self.track.raw_data, overrides={
            "frame_rate": int(self.track.frame_rate * speed)
        })
        self.stack.append(self.track)
        self.track = sound_with_altered_frame_rate.set_frame_rate(self.track.frame_rate)

    def save(self):
        save_path = filedialog.asksaveasfilename(initialdir = "/home/", title=
        "Where do you want to save the modified file?", filetypes = (("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.track.export(save_path, bitrate="320k", format="mp3")

    def volume_change(self, vol):
        self.stack.append(self.track)
        self.track = self.track + vol

    def slice(self, begin, end):
        ms1 = begin * 1000
        ms2 = end * 1000
        self.stack.append(self.track)
        self.track = self.track[ms1:ms2]

    def get_duration(self):
        if self.track is not None:
            return self.track.duration_seconds()
        else:
            return 0.0

    def reverse_sound(self):
        self.stack.append(self.track)
        self.track = self.track.reverse()

    def repeat_sound(self, count):
        self.stack.append(self.track)
        self.track = self.track * 2

    def merge(self):
        path = filedialog.askopenfilename(initialdir="/home/", title="What file do you want to import?",
                                                   filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        track = AudioSegment.from_mp3(path)
        self.stack.append(self.track)
        self.track = self.track + track

    def fade_in(self, seconds):
        ms = seconds * 1000
        self.stack.append(self.track)
        self.track = self.track.fade_in(ms)

    def fade_out(self, seconds):
        ms = seconds * 1000
        self.stack.append(self.track)
        self.track = self.track.fade_out(ms)

    def overlay(self):
        self.stack.append(self.track)
        self.filePath = filedialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.overlayTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track.overlay(self.overlayTrack)

    def undo(self):
        self.queue.insert(0, self.track)
        self.track = self.stack.pop()

    def redo(self):
        self.stack.append(self.track)
        self.track = self.queue[0]
        self.queue.pop(0)