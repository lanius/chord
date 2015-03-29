# -*- coding: utf-8 -*-

import contextlib
import multiprocessing as mp

import pyHook
import pythoncom


def hook_keys(pressed_keys):

    def on_key_down(event):
        if event.Key not in pressed_keys:
            pressed_keys.append(event.Key)
        return True

    def on_key_up(event):
        if event.Key in pressed_keys:
            pressed_keys.remove(event.Key)
        return True

    hm = pyHook.HookManager()

    hm.KeyDown = on_key_down
    hm.KeyUp = on_key_up

    hm.HookKeyboard()
    pythoncom.PumpMessages()


@contextlib.contextmanager
def capture():
    # todo: implement the proxy object that work as 'set'
    pressed_keys = mp.Manager().list()
    hook = mp.Process(target=hook_keys, args=(pressed_keys,))
    hook.start()
    yield pressed_keys
    hook.terminate()
    hook.join()
