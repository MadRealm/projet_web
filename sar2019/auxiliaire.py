def parsing (string):
    l =[]
    mot = ""
    for i in range(len(string)):
        mot += string[i]
        if string[i] == " " :
            l.add(mot)
            mot = ""
    return l