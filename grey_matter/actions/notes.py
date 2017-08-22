import sqlite3
from datetime import datetime

from grey_matter.utils import clean_message
from grey_matter.voice_module import speak


def note_something(speech_text):
    conn = sqlite3.connect('memory.db')
    message = clean_message(speech_text, 'note')

    conn.execute("INSERT INTO notes (notes, notes_DATE) VALUES (?, ?)",
                 (message, datetime.strftime(datetime.now(), '%d-%m-%Y')))
    conn.commit()
    conn.close()

    speak('Your note has been saved.')


def show_all_notes():
    conn = sqlite3.connect('memory.db')
    speak('Your notes are as follows:')

    cursor = conn.execute("SELECT notes FROM notes")

    for row in cursor:
        speak(row[0])

    conn.close()
