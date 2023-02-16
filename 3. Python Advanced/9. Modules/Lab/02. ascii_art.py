from pyfiglet import figlet_format


def renderer(msg):
    figlet = figlet_format(msg)
    print(figlet)


renderer(input())
