# Some generic utils that can be used in custom nvda scripts.
# This are not mostly new features but convenience for developers
import inputCore
import keyboardHandler

def executeKeyPresses(*keyPresses):
    """ Emulates the execution of a bunch of key presses """
    map(inputCore.manager.emulateGesture,
        [KeyboardHandler.KeyboardInputGesture.fromName(key) for key in keyPresses])


