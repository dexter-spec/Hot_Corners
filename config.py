print("DO NOT EDIT THE 'commands.txt' MANUALLY, ONLY USE THIS TOOL")

top_left = input("Command to run if the curser is on the top left corner fore more than 5 secs: ")
top_right = input("Command to run if the curser is on the top right corner fore more than 5 secs: ")
bottom_left = input("Command to run if the curser is on the bottom left corner fore more than 5 secs: ")
bottom_right = input("Command to run if the curser is on the bottom right corner fore more than 5 secs: ")
dump = {"top_left":top_left,"top_right":top_right,"bottom_left":bottom_left,"bottom_right":bottom_right}

with open("commands.txt","w+") as f:
    f.write(f"{dump}")
