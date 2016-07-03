import youtube_dl
import gi
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def downloadVideo(video_url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonClicked(self, button):
        text = builder.get_object("urlField")
        print(text.get_text())
        threading.Thread(target=downloadVideo, args=(text.get_text(),)).start()

builder = Gtk.Builder()
builder.add_from_file("window.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()
