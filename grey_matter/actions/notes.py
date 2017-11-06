import sqlite3
from datetime import datetime

from grey_matter import speak
from grey_matter.utils import clean_message


def note_something(speech_text, message):
    conn = sqlite3.connect('memory.db')
    message = clean_message(speech_text, 'note')

    conn.execute("INSERT INTO notes (notes, notes_DATE) VALUES (?, ?)",
                 (message, datetime.strftime(datetime.now(), '%d-%m-%Y')))
    conn.commit()
    conn.close()

    speak(message)


def show_all_notes(message):
    conn = sqlite3.connect('memory.db')
    speak(message)

    cursor = conn.execute("SELECT notes FROM notes")

    for row in cursor:
        speak(row[0])

    conn.close()
