import datetime 
def Welcome():
    time_hour=datetime.datetime.now().hour
    wishes="Morning"
    if(time_hour>=23 and time_hour<6):
        print("sorry! The bottles store is closed...\nVisit again...")
        quit()
    if(time_hour>12 and time_hour<16):
        wishes="Afternoon"
    elif(time_hour>=16 and time_hour<23):
        wishes="Evening"
    print("Hi\nGood "+wishes+" !\nWelcome to SAI stores.")
Welcome()
print("This chatbot gives the information about which  different types of bottles in the store and it's capacity,price is available in this chatbot.")
def conversation():
    questions = ["Hi","May I know your name please?","How can I help you?",""
    "we have different types of bottle? what capacity you want?",
    "ok!, what type of material you want(plastic,steel,copper)?",
    "In what price range you need?","yes bottle is available",
    "No bottles not available with this features!","Thank you visit again"]
    c=[500,750,900,1000]
    bottles = [(500,"plastic",100),(500,"steel",100),(500,"copper",100),
                (750,"plastic",150),(750,"steel",150),(750,"copper",150),
                (900,"plastic",200),(900,"steel",200),(900,"copper",200),
                (1000,"plastic",300),(1000,"steel",300),(1000,"copper",300)]
    while True:
        print(questions[0])
        print(questions[1])
        name = input()
        print("Hello "+name+" "+questions[2])
        print(questions[3])
        while True:
                cap = int(input())
                def capacity(cap):
                    for i in c: 
                        if cap == i:
                            print(questions[4])
                            mat=input()
                            if(mat.lower()=="plastic" or mat.lower()=="steel" or mat.lower()=="copper"):
                                print(questions[5])
                                price=int(input())
                                for i in bottles:
                                    if(price==i[2]):
                                        print(questions[6])
                                        print(questions[8])
                                        quit()
                                else:
                                    print(questions[7])
                                    print(questions[8])
                                    quit()
                        else:
                            print("please try to give the exact keyword what you want?")
                            cap=int(input())
                            capacity(cap)
                capacity(cap)            
conversation()