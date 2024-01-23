# define play function, that prints the given argument, has a default value to its argument
def play(arg1="Speak slower please!"):
    print(arg1)

# define playback variable, gets text input from user, and modifies input with replace(blank spaces to dots)
playback = input("Insert here to slow it down: ")
playback = playback.replace(" ", "...")

# checks if the variable has a text, if true calls play function with the variable as argument
if playback:
    play(playback)
else:
    play()
# if false, else calls the play function without arguments, printing its default value
