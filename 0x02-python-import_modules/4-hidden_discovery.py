#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for hid in dir(hidden_4):
        if hid[:2] != "__":
            print(hid)
