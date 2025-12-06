import Board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
keyboard = KMKKeyboard()
display = Display(
    display=SSD1306(sda=board.D4, scl=board.D5),
    entries=[
        TextEntry(text='REUBENS TUFFPAD'),
    ],
    height=80,
)
keyboard.extensions.append(display)
PINS = [board.D3, board.D2, board.D1]
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)
keyboard.keymap = [
    [KC.MPRV,   KC.MPLY,  KC.MNXT, ]
]
if __name__ == '__main__':
    keyboard.go()