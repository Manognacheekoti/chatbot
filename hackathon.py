import random
print('how can i help you?')
greetings=['hola','hello','hii','hi','hai','hey','hey!','hye','heya']
random_greeting=random.choice(greetings)
ques1=['hi,how are you?','hwru','hw r u','how r u','hii,hw r u','how are you','how are you?']
resp1=['i am good! how can i help you?']
ques2=['wh','i am new to the city help me to find a way','help me with the routes','i want ur help in finding routes']
resp2=['where do you want to go?,if you are not feeling secure then https://www.hyderabadpolice.gov.in/Importantcontacts.html']
ques3=['gitam location','gitam hyd location','gitam','get me the address of gitam','gitam address']
resp3=['we have two ways to reach gitam-metro/bus']
ques4=['suggest me the best one','which is good','which is advisable','which is the best one']
ques6=['mtro','metro','metro train']
resp4=['suggest me the best one','which is good','which is advisable','which is the best one']
resp31=['mtro','metro','metro train']
ques5=['bus','buss','buse','buses']
resp51=['bus']
while True:
    user=input(">>>")
    if user in greetings:
        print(random_greeting)
    elif user in ques1:
        print(resp1)
    elif user in ques2:
        print(resp2)
    elif user in ques3:
        print(resp3)
    elif user in ques4:
        print(resp31)       
    if(user in ques6):
        user2=input("enter metro travelling")
        ques31=['hw to reach']
        resp5=['take an auto , cab or walk 200meters to reach  metro station']
        ques7=['aa','guid me','okay','ok tell me the route','done',' i took auto','i will walk','i book cab','i want to go in cab','i want to go in auto','i want to walk']
        resp6=['now you arrived at metro station so follow my steps']
           
        ques8=['okay','ok tell me the next steps','ok','what i want to do next','what i have to do next?','next']
        resp7=['at present u r the ground floor ,now u have go to the concourse by lift']
        ques9=['okay','ok','then','ok ok','next','iam going','im gng']
        resp8=['then u will find the ticket counter at right side']
        ques10=['okay,i got it','okay','ok','ok ok','fine','found that','found it','i found it']
        resp9=[' go and deposit the money and ask the ticket for miyapur']
        ques11=['ok fine','iam gng','ok iam going','ok ok','done','fine','ok','okay']
        resp10=['put u r bags along with u r phone at security check which is infront of u']
        ques12=['iam done','fine','done with it','okay','ok','okiam going','iam going','ok find it']
        resp11=['after security check, scan the coin then gates will open and pass through them']
        ques13=['iam done','fine','done with it','okay','ok','ok iam going','iam going','ok find it']
        resp12=['find the platform number and get in to the train']
        ques14=['iam done','fine','done with it','okay','ok','ok iam going','iam going','ok find it','ok i got in to the train']
        resp13=['after get in to the train ,exactly after 9 stations u have to get down the train,keep hearing the audio']
        ques15=['where should i get down','what is the station name','station name','which station','okay','iam done','fine','done with it','okay','ok','ok iam going','iam going','ok find it']
        resp14=['after reaching miyapur metro station,get down the stairs u will find miyapur busstop and find the bus 219,218,and any other bus going to patencheruvu']
        ques16=['iam done','fine','done with it','okay','ok','ok iam going','iam going','ok find it','ok fine','iam gng','ok iam going','ok ok','done','fine','ok','okay']
        resp15=['then after reaching  patancheruvu ,u have to find the auto to go to u r destination(rudraram)']
        ques17=['iam done','fine','done withit','okay','ok','ok iam going','iam going','ok find it','still how much tme to take to reach my destination','how long should i travel','still how may kilometres to travel','kilometres']
        resp16=['at last after 15 to 20 minutes u will be reaching u r destination']
        ques18=['thank you','thank you so much','it helped me a lot','thank u','tq','thanks alot','thank you very much','thank u so much','thank u very much','tq so much','tq very much','bye']

        if(user2 in ques31):
            print(resp5)
            user3=input("ques7")
            if(user3 in ques7):
                print(resp6)
                user4=input("ques8")
                if(user4 in ques8):
                    print(resp7)
                    user5=input("ques9")
                    if(user5 in ques9):
                        print(resp8)
                        user6=input("ques10")
                        if(user6 in ques10):
                            print(resp9)
                            user7=input("ques11")
                            if(user7 in ques11):
                                print(resp10)
                                user8=input("ques12")
                                if(user8 in ques12):
                                    print(resp11)
                                    user9=input("ques13")
                                    if(user9 in ques13):
                                        print(resp12)
                                        user10=input("ques14")
                                        if(user10 in ques14):
                                            print(resp13)
                                            user11=input("ques15")
                                            if(user11 in ques15):
                                               print(resp14)
                                               user12=input("ques16")
                                               if(user12 in ques16):
                                                  print(resp15)
                                                  user13=input("ques17")
                                                  if(user13 in ques17):
                                                     print(resp16)
                                                     user14=input("ques18")
                                                     if(user14 in ques18):
                                                        print(resp17)
                                                        
             

    resp20=['find patancheruvu bus']
    ques20=['i boarded the bus ','i got into the bus','iam done','okay','ok','ok iam going','iam going','ok find it','ok i got in to thebus']
    resp21=['then after reaching  patancheruvu ,u have to find the auto to go to u r destination(rudraram)']
    ques22=['iam done','fine','done withit','okay','ok','ok iam going','iam going','ok find it','still how much tme to take to reach my destination','how long should i travel','still how may kilometres to travel','kilometres']
    resp22=['at last after 15 to 20 minutes u will be reaching u r destination']
    ques23=['thank you','thank you so much','it helped me a lot','thank u','tq','thanks alot','thank you very much','thank u so much','thank u very much','tq so much','tq very much','bye']
    if(user in ques5):
        print(resp20)
        user16=input("ques20")
        if(user16 in ques20):
            print(resp21)
            user17=input("ques22")
            print(resp22) 

  
              
         
                   
        
        
              
         

