import tkinter as tk
from sound import *
from pygame import mixer

global vol_arg
global speed_arg
global begin
global end
global paused
global incount
global outcount
global times
paused = False


def get_repeat():
    global times
    value = repeat_entry.get()
    times = int(value)
    song.repeat_sound(times)


def get_fade_out():
    global outcount
    value = fade_out_entry.get()
    outcount = int(value) * 1000
    song.fade_out(outcount)


def get_fade_in():
    global incount
    value = fade_in_entry.get()
    incount = int(value) * 1000
    song.fade_in(incount)


def get_slice():
    global begin
    global end
    value1 = first_slice_entry.get()
    begin = int(value1)
    value2 = second_slice_entry.get()
    end = int(value2)
    song.slice(begin, end)


def get_volume():
    global vol_arg
    value = volume_entry.get()
    vol_arg = float(value)
    song.volume_change(vol_arg)


def get_speed():
    global speed_arg
    value = speed_entry.get()
    speed_arg = float(value)
    song.speed_change(speed_arg)


def open_sound():
    path = filedialog.askopenfilename(initialdir="/home/", title="What file do you want to import?",
                                          filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    track = AudioSegment.from_mp3(path)
    song.filePath = path
    song.track = track
    play_btn['state'] = 'normal'
    pause_btn['state'] = 'normal'
    stop_btn['state'] = 'normal'
    undo_btn['state'] = 'normal'
    redo_btn['state'] = 'normal'
    speed_btn['state'] = 'normal'
    speed_entry['state'] = 'normal'
    reverse_btn['state'] = 'normal'
    overlay_btn['state'] = 'normal'
    merge_btn['state'] = 'normal'
    volume_btn['state'] = 'normal'
    volume_entry['state'] = 'normal'
    slice_btn['state'] = 'normal'
    first_slice_entry['state'] = 'normal'
    second_slice_entry['state'] = 'normal'
    fade_in_btn['state'] = 'normal'
    fade_in_entry['state'] = 'normal'
    fade_out_btn['state'] = 'normal'
    fade_out_entry['state'] = 'normal'
    repeat_btn['state'] = 'normal'
    repeat_entry['state'] = 'normal'
    save_btn['state'] = 'normal'
    #time_label.config(text=f'Song duration: {song.get_duration()}')


def play():
    song.track.export("song.mp3", format="mp3")
    mixer.music.load("song.mp3")
    mixer.music.play(loops=0)


def stop():
    mixer.music.stop()


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True


root = tk.Tk()
mixer.init()
root.title('Audio Editor')
root.geometry('700x400')
root.resizable(False, False)
root.config(bg='grey')

song = Sound()

play_img = tk.PhotoImage(file='1.png')
pause_img = tk.PhotoImage(file='2.png')
stop_img = tk.PhotoImage(file='3.png')

play_btn = tk.Button(root, image=play_img, borderwidth=0, command=lambda: play(), state='disabled')
pause_btn = tk.Button(root, image=pause_img, borderwidth=0, command=lambda: pause(paused), state='disabled')
stop_btn = tk.Button(root, image=stop_img, borderwidth=0, command=lambda: stop(), state='disabled')

play_btn.place(x=400,y=200)
pause_btn.place(x=460,y=200)
stop_btn.place(x=520,y=200)

open_btn = tk.Button(root, borderwidth=0, text='Open', command=lambda: open_sound(), width=4)
open_btn.place(x=40,y=40)

undo_btn = tk.Button(root, borderwidth=0, text='Undo', command=lambda: song.undo(), width=4, state='disabled')
undo_btn.place(x=40,y=70)

redo_btn = tk.Button(root, borderwidth=0, text='Redo', command=lambda: song.redo(), width=4, state='disabled')
redo_btn.place(x=40,y=100)

speed_btn = tk.Button(root, borderwidth=0, text='Change\nspeed', command=lambda: get_speed(), width=4, state='disabled')
speed_btn.place(x=40,y=130)

speed_entry = tk.Entry(root, width=6, state='disabled')
speed_entry.place(x=40,y=176)

reverse_btn = tk.Button(root, borderwidth=0, text='Reverse', command=lambda: song.reverse_sound(), width=4,
                        state='disabled')
reverse_btn.place(x=40,y=210)

overlay_btn = tk.Button(root, borderwidth=0, text='Overlay', command=lambda: song.overlay(), width=4, state='disabled')
overlay_btn.place(x=40,y=240)

merge_btn = tk.Button(root, borderwidth=0, text='Merge', command=lambda: song.merge(), width=4, state='disabled')
merge_btn.place(x=40,y=270)

volume_btn = tk.Button(root, borderwidth=0, text='Change\nvolume', command=lambda: get_volume(), width=4, state='disabled')
volume_btn.place(x=40, y=300)

volume_entry = tk.Entry(root, width=6, state='disabled')
volume_entry.place(x=40, y=346)

slice_btn = tk.Button(root, borderwidth=0, text='Slice', command=lambda: get_slice(), width=4, state='disabled')
slice_btn.place(x=120, y=40)

first_slice_entry = tk.Entry(root, width=6, state='disabled')
first_slice_entry.place(x=120, y=70)

second_slice_entry = tk.Entry(root, width=6, state='disabled')
second_slice_entry.place(x=180, y=70)

fade_in_btn = tk.Button(root, borderwidth=0, text='Fade in', command=lambda: get_fade_in(), width=4, state='disabled')
fade_in_btn.place(x=120, y=100)

fade_in_entry = tk.Entry(root, width=6, state='disabled')
fade_in_entry.place(x=120, y=128)

fade_out_btn = tk.Button(root, borderwidth=0, text='Fade out', command=lambda: get_fade_out(), width=4, state='disabled')
fade_out_btn.place(x=120, y=160)

fade_out_entry = tk.Entry(root, width=6, state='disabled')
fade_out_entry.place(x=120, y=188)

repeat_btn = tk.Button(root, borderwidth=0, text='Repeat', command=lambda: get_repeat(), width=4, state='disabled')
repeat_btn.place(x=120, y=220)

repeat_entry = tk.Entry(root, width= 6, state='disabled')
repeat_entry.place(x=120, y=248)

save_btn = tk.Button(root, borderwidth=0, text='Save', command=lambda: song.save(), width=4, state='disabled')
save_btn.place(x=120,y=280)
#time_label = tk.Label(root, borderwidth=2, text=f'Song duration: {song.get_duration()}')
#time_label.place(x=40, y=190)

root.mainloop()