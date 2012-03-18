from django.conf import settings

HOTKEYS = getattr(settings, 'HOTKEYS', list())

KEY_CODES = {
                'BACKSPACE': 8,
                'TAB': 9,
                'ENTER': 13,
                'SHIFT': 16,
                'CTRL': 17,
                'ALT': 18,
                'PAUSE': 19,
                'CAPSLOCK': 20,
                'ESC': 27,
                'PAGE UP': 33,
                'PAGE DOWN': 34,
                'END': 35,
                'HOME': 36,
                'LEFT ARROW': 37,
                'UP ARROW': 38,
                'RIGHT ARROW': 39,
                'DOWN ARROW': 40,
                'INSERT': 45,
                'DELETE': 46,
                '0': 48,
                '1': 49,
                '2': 50,
                '3': 51,
                '4': 52,
                '5': 53,
                '6': 54,
                '7': 55,
                '8': 56,
                '9': 57,
                'A': 65,
                'B': 66,
                'C': 67,
                'D': 68,
                'E': 69,
                'F': 70,
                'G': 71,
                'H': 72,
                'I': 73,
                'J': 74,
                'K': 75,
                'L': 76,
                'M': 77,
                'N': 78,
                'O': 79,
                'P': 80,
                'Q': 81,
                'R': 82,
                'S': 83,
                'T': 84,
                'U': 85,
                'V': 86,
                'W': 87,
                'X': 88,
                'Y': 89,
                'Z': 90,
                '0 (NUMPAD)': 96,
                '1 (NUMPAD)': 97,
                '2 (NUMPAD)': 98,
                '3 (NUMPAD)': 99,
                '4 (NUMPAD)': 100,
                '5 (NUMPAD)': 101,
                '6 (NUMPAD)': 102,
                '7 (NUMPAD)': 103,
                '8 (NUMPAD)': 104,
                '9 (NUMPAD)': 105,
                '*': 106,
                '+': 107,
                '-': 109,
                '.': 110,
                '/': 111,
                'F1': 112,
                'F2': 113,
                'F3': 114,
                'F4': 115,
                'F5': 116,
                'F6': 117,
                'F7': 118,
                'F8': 119,
                'F9': 120,
                'F10': 121,
                'F11': 122,
                'F12': 123,
                'NUMLOCK': 144,
                'SCROLL': 145,
                '=': 187,
                'COMMA': 188,
                'SLASH /': 191,
                'BACKSLASH \\': 220,
                'META': 224,
            }
