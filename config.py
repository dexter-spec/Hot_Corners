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


print("DO NOT EDIT THE 'commands.txt' MANUALLY, ONLY USE THIS TOOL")

top_left = input("Command to run if the curser is on the top left corner fore more than 5 secs: ")
top_right = input("Command to run if the curser is on the top right corner fore more than 5 secs: ")
bottom_left = input("Command to run if the curser is on the bottom left corner fore more than 5 secs: ")
bottom_right = input("Command to run if the curser is on the bottom right corner fore more than 5 secs: ")
dump = {"top_left":top_left,"top_right":top_right,"bottom_left":bottom_left,"bottom_right":bottom_right}

with open("commands.txt","w+") as f:
    f.write(f"{dump}")

