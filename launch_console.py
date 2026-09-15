name = input("What is your name")
print("Hello "+ name+ ", welcome to my Launch Console!!")
print("Here are some options to choose from:\n" \
"1)About me\n" \
"2)My goals \n" \
"3)My favorite anime \n" \
"4)Exit")
choose = input("Type a number 1-4 please.")
if(choose=="1"):
    print("Hi there "+name+"!, I'm Nobel Yemane, a Brookwood High School student from Lilburn, Georgia! My favorite pasttime is playing the cello, watching the series The Rookie, and playing Video Games!")
if(choose=="2"):
    print("Hi there"+name+"My Computer Science oriented goal is to plan out and code the baseline for my upcoming startup!")
if(choose=="3"):
    print("Hi there"+name+". Now im not gonna tell your my favorite Anime that easily bucko; first I want your opinion.")
    favanime = input("Whats your favorite anime")
    if(favanime=="Naruto"):
        print("Me too! Not bad champ!")
    else:
        print("Huh.. its not what I would've chosen.")
if(choose=="4"):
    print("Goodbye!")
