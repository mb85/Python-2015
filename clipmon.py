#!/usr/bin/env python3
# coding: utf-8

import win32clipboard
import time
import json
import os
import atexit
import sys

if os.path.isfile("settings.json"):
    with open("settings.json") as f:
        settings = json.loads(f.read())
else:
    settings = {}

data_file = settings.setdefault("data_file", "clipboard_data.json")
error_file = settings.setdefault("error_file", "errors.log")
date_format = settings.setdefault("date_format", "%c")
remember_last = settings.setdefault("remember_last", True)

# sys.stderr = open(error_file, "w")


def get_clipboard_text():
    win32clipboard.OpenClipboard()
    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_UNICODETEXT):
        text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return text


def set_clipboard_data(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()


def clean_up():
    with open(data_file, "w") as d_file:
        d_file.write(json.dumps(clipboard_data, indent=4))

    with open("settings.json", "w") as s_file:
        s_file.write(json.dumps(settings, indent=4))

atexit.register(clean_up)

if os.path.isfile(data_file):
    with open(data_file) as f:
        clipboard_data = json.loads(f.read())
else:
    clipboard_data = []

if remember_last and clipboard_data:
    last_item = clipboard_data[-1][-1]
    set_clipboard_data(last_item)

while True:
    cb_text = get_clipboard_text()
    if cb_text:
        timestamp = time.strftime(date_format)
        entry = (timestamp, cb_text)

        if cb_text not in [val[-1] for val in clipboard_data]:
            clipboard_data.append(entry)
            print(cb_text)

    time.sleep(0.25)
