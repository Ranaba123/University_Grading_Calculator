# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20221241(IIT ID)/20527772(UOW Number)
# Date: 12/7/2023



#Part one
print("************************************************************************University Grading Calculator*****************************************************************")
print("\n\n")
class Invalidrange(Exception):  #creating a exception for range
    pass
# Initializing Gobal variables
pass_credit=0   #Use for store pass credit
defer_credit=0  #Use for store defer credit
fail_credit=0   #Use for store fail credit



from graphics import *

def main():
    """This is the main function that rruns the entire program"""
    #Initializing local variables
    Total_progress_count=0              #use to store total number of students got progress
    Total_trailer_count=0               #use to store total number of students got module trailer
    Total_retriever_count=0             #use to store total number of students got module retrieve
    Total_exclude_count=0               #use to store total number of students got exclude
    
    attempt="y"    #use to store the attempt
    while(attempt=="y"): #Main loop of the program
        def input_grading(grading):
            """This function is use to store each of the gradings and validate them"""
            while True:#Checking the validity of the pass credit(is it a integer or out of range)
                try:
                    credit=int(input(f"Please enter your credits at {grading} : "))
                    if credit!=0 and credit!=20 and credit!=40 and credit!=60 and credit!=80 and credit!=100 and credit!=120:
                        raise Invalidrange("Out of range\n")
                    break
                except ValueError:
                    print("Integer required\n")
    
                except Invalidrange as e:
                    print(e)
            return credit
        
        pass_credit=input_grading("pass")
        defer_credit=input_grading("defer")
        fail_credit=input_grading("fail")
        
        if pass_credit+defer_credit+fail_credit!=120:#Checking the validity of the total(pass+fail+defer==120)
            print("Total incorrect")
            print("\n")
            while True:#checking the validity of the attempt(If the total is incorrect program asking a from the need a attempt or not)
                print("Would you like to enter a another data set ?")
                attempt=str(input("Enter 'y' for yes or 'q' to quit and view results : "))
                print("\n")
                if attempt=="q" or attempt=="y":  #Giving a opportunity for the 
                    break
                else:
                    print("Wrong character.Please enter 'q' or 'y' ")
            if attempt=="y":
                continue
            elif attempt=="q":
                break
        elif(pass_credit==120):          #Conditions and calculating the count of the students each grading has 
            print("Progress\n")
            Total_progress_count+=1
        elif(pass_credit==100 and (defer_credit==20 or fail_credit==20)):
            print("Progress (module trailer)\n")
            Total_trailer_count+=1
        elif(fail_credit==120 or fail_credit==80 or fail_credit==100):
            print("Exclude\n")
            Total_exclude_count+=1
        else:
            print("Do not Progress – module retriever\n")
            Total_retriever_count+=1
        
          
        while True:#checking the validity of the attempt
            print("Would you like to enter a another data set ?")
            attempt=str(input("Enter 'y' for yes or 'q' to quit and view results : "))
            print("\n")
            if attempt=="q" or attempt=="y":    #Giving a another opportunity to enter another data set or quit the program
                break
            else:
                print("Wrong character.Please enter 'q' or 'y' ")
        if attempt=="y":
            continue
        elif attempt=="q":
            break
        
#--------------------------------------Histogram-------------------------------------------------#


    def histogram():
        """This is the histogra, function"""
        win = GraphWin("Histogram", 500, 320)
        win.setBackground("#EDF2EC")
    


        progress_bar = Rectangle(Point(9, 250), Point(105, 250-(Total_progress_count*10)))
        trailer_bar = Rectangle(Point(110, 250), Point(205, 250-(Total_trailer_count*10)))
        retriever_bar = Rectangle(Point(210, 250), Point(305, 250-(Total_retriever_count*10)))
        exclude_bar= Rectangle(Point(310, 250), Point(405, 250-(Total_exclude_count*10)))
        aLine = Rectangle(Point(0, 250), Point(430, 250))
#adding texts to the graphic
        progress_message = Text(Point(95,265), "Progress")
        trailer_message= Text(Point(195,265), "Trailer")
        retriever_message=Text(Point(300,265), "Retriever")
        exclude_message=Text(Point(404,265), "Excluded")
        topic_message=Text(Point(141,20), "Histogram Results")
        progress_count_message=Text(Point(99,250-((Total_progress_count*10)+10)), f"{Total_progress_count}")
        trailer_count_message=Text(Point(199,250-((Total_trailer_count*10)+10)), f"{Total_trailer_count}")
        retriever_count_message=Text(Point(299,250-((Total_retriever_count*10)+10)), f"{Total_retriever_count}")
        excluded_count_message=Text(Point(403,250-((Total_exclude_count*10)+10)), f"{Total_exclude_count}")
        outcome_message=Text(Point(163,295),f"{Total_progress_count+Total_trailer_count+Total_retriever_count+Total_exclude_count} outcomes in the total")

#making the bars colours
        progress_bar.setFill("#AEF8A1")
        trailer_bar.setFill("#A0C689")
        retriever_bar.setFill("#A7BC77")
        exclude_bar.setFill("#D2B6B5")
        aLine.setFill("black")
#Moving the bars to correct positions
        aLine.move(40, 0)
        retriever_bar.move(45, 0)
        exclude_bar.move(47, 0)
        trailer_bar.move(43, 0)
        progress_bar.move(41, 0)

#Styling the texts(make the text bold and changing the colour of the text and changing the size of the font)
        progress_message.setStyle("bold")
        progress_message.setTextColor("#778792")

        trailer_message.setStyle("bold")
        trailer_message.setTextColor("#778792")

        retriever_message.setStyle("bold")
        retriever_message.setTextColor("#778792")

        exclude_message.setStyle("bold")
        exclude_message.setTextColor("#778792")

        topic_message.setStyle("bold")
        topic_message.setTextColor("#4F4F4F")
        topic_message.setSize(14)

        progress_count_message.setTextColor("#778792")
        progress_count_message.setStyle("bold")

        trailer_count_message.setTextColor("#778792")
        trailer_count_message.setStyle("bold")

        retriever_count_message.setTextColor("#778792")
        retriever_count_message.setStyle("bold")

        excluded_count_message.setTextColor("#778792")
        excluded_count_message.setStyle("bold")
                     
        outcome_message.setStyle("bold")
        outcome_message.setTextColor("#778792")
        outcome_message.setSize(14)


        progress_bar.draw(win)
        trailer_bar.draw(win)
        retriever_bar.draw(win)
        exclude_bar.draw(win)
        aLine.draw(win)
        progress_message.draw(win)
        trailer_message.draw(win)
        retriever_message.draw(win)
        exclude_message.draw(win)
        topic_message.draw(win)
        progress_count_message.draw(win)
        trailer_count_message.draw(win)
        retriever_count_message.draw(win)
        excluded_count_message.draw(win)
        outcome_message.draw(win)
        win.getMouse()  
        win.close()

    histogram()

    return Total_progress_count,Total_trailer_count,Total_retriever_count,Total_exclude_count
    
#Calculation of total number of module trailers,module retrievers and excluders
        
main()


    
   




    




    
    



    


