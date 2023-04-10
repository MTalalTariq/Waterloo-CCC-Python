# Waterloo CCC 2023 Junior 4 (/Senior 1) Trianglane

tape = 0
tiles = input() # num of tiles

# first lane
l1 = input() 
l1 = l1.split(" ")
for i in range(len(l1)):
    l1[i] = int(l1[i])
# second lane
l2 = input() 
l2 = l2.split(" ")
for i in range(len(l2)):
    l2[i] = int(l2[i])

# for lane 1
for x in range(len(l1)):
    
    if l1[x] == 1:
        if x == 0: # first case
            tape += 3
            #print("l1 f case")
        elif l1[x-1] == 1: # triangle w prev
            tape += 1
            #print("l1 prev case")
        elif l1[x-1] == 0: # triangle w no prev
            tape +=3
            #print("l1 no prev case")

# for lane 2
for x in range(len(l2)):
    
    if l2[x] == 1:
        if x == 0: # first case
            if l1[x] == 0: # no top
                tape += 1
                #print("l2 f case no top")
            else: # top
                tape += 3
                #print("l2 f case top")
        elif x % 2 == 1: # even triangle
            if l2[x-1] == 1: # triangle w prev
                tape += 1
                #print("l2 even prev case")
            else: # triange w no prev
                tape += 3
                #print("l2 even no prev case")

        elif x % 2 == 0: # odd triangle
            if l2[x-1] == 1: # triangle w prev
                if l1[x] == 1: # top 
                    tape -= 1
                    #print("l2 odd prev case w top")
                else: # no top
                    tape += 1
                    #print("l2 odd prev case no top")
            else: # triange w no prev
                if l1[x] == 1: # top 
                    tape += 1
                    #print("l2 odd no prev case w top")
                else: # no top
                    tape += 3
                    #print("l2 odd no prev case no top")


print(tape)