#COPYRIGHT(LICENSE)

# MIT License

# Copyright (c) 2022 dexter-spec

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pyautogui
import time
import os
import ast
##defs##
def get_corners():
    X, Y = pyautogui.position()
    width, height = pyautogui.size()
    W = (int(width))-10
    H = (int(height))-20
#    print("x",X)
#    print("h",H)
#    print("Y",Y)
#    print("w",W)
    if X<20 and Y<20:
        
        return "top left"
    elif X<20 and Y>H:
        
        return "bottom left"
    

    elif X>H and Y<20:
        
        return "top right"
    elif X>H and Y>H:
        
        return "bottom right"
    return "NotACorner"


###logic###
###getting the commands###
with open("commands.txt", "r") as f:
    command = f.readline()

commands = ast.literal_eval(command)
top_l = commands["top_left"]
top_r = commands["top_right"]
bottom_l = commands["bottom_left"]
bottom_r = commands["bottom_right"]

###running##

print("Running...")
while True:
    time.sleep(10)
    corn = get_corners()
###command to run if the curser is on top left###
    if corn == "top left":
        os.system(top_l)
###command to run if the curser is on top right###
    elif corn == "top right":
        os.system(top_r)
###command to run if the curser is on bottom right###
    elif corn == "bottom right":
        os.system(bottom_r)
###command to run if the curser is on bottom left###
    elif corn == "bottom left":
        os.system(bottom_l)
##if not a corner, do nothing###
    else:
        print("nothing to do")
