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

def conversation():
    questions = ["Hi","May I know your name please?","How can I help you?",
    "we have different types of bottles? what capacity you want?",
    "ok!, what type of material you want(plastic,steel,copper...)?",
    "In what price range you need?","yes bottle is available",
    "No bottles not available with this features!","Thank you visit again","bye","Bye"]
    keywords = ["bottle","Bottle","BOTTLE","btl","botl","bttl","bottles","BOTTLES","Bottles"]
    bottles = [(500,"plastic",120),(500,"steel",250),(500,"copper",500),
                (750,"plastic",180),(750,"steel",350),(750,"copper",650),
                (900,"plastic",200),(900,"steel",450),(900,"copper",780),
                (1000,"plastic",240),(1000,"steel",500),(1000,"copper",880)]
    x = 0
    while True:
        if x == 0:
            print(questions[0])
            print(questions[1])
            name = input()
            print("Hello "+name+" "+questions[2])
            s = input()
            j = 0
            flag = 0
        while j<3 :
            for word in s.split():
                if word in keywords:
                    print(questions[3])
                    cap = int(input())
                    print(questions[4])
                    mat = input()
                    print(questions[5])
                    price = int(input())
                    for i in bottles:
                        if cap == i[0] and mat == i[1] and price>=i[2]:
                            print(questions[6]+"here are the details ")
                            print("capacity: "+str(i[0]))
                            print("type of material :"+str(i[1]))
                            print("cost : "+str(i[2]))
                            flag = 1
                            print(questions[8])
                            break
                    else:
                        print(questions[7])
                        print(questions[8])
                        break
            else:
                if flag != 1:
                    print("please try to give the exact keyword what you want?")
                    s = input()
                j = j + 1
                if flag == 1:
                	break
        else:
            print("Thank you! your search is not available")
        if flag == 1:
            break
        else:
        	x = 1
        	print("Thank you! please check for the other products")
        
    
conversation()
