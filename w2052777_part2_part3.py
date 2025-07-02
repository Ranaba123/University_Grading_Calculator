# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20221241(IIT ID)/20527772(UOW Number)
# Date: 12/7/2023


#Part 2 and Part 3
import datetime
print("************************************************************************University Grading Calculator*****************************************************************")
print("\n\n")
class Invalidrange(Exception):  #creating a exception for range
    pass
# Initializing global variables
Volume_of_credit=0   #Use for store pass credit,defer credit,fail credit

range_of_gradings=[0,20,40,60,80,100,120]#The number of values that needed to be enter for the credits
main_list=[] # this is the main list all the sorted data comes from the grade_list is stored in this list 
from graphics import *

def main():
    
    """This is the main function that rruns the entire program"""
    # Initializing local variables
    Total_progress_count=0              #use to store total number of students got progress
    Total_trailer_count=0               #use to store total number of students got module trailer
    Total_retriever_count=0             #use to store total number of students got module retrieve
    Total_exclude_count=0               #use to store total number of students got exclude
    attempt="y"    #use to store the attempt
    while(attempt=="y"): #Main loop of the program
        grade_list=[] #Looping list
        def input_grading(grading):
            """This function is use to store each of the gradings in the grade list and validate them"""
            
            for i in range(3): #Loop that asks user to enter 3 values 
                while True: # Validating the each value
                    try:
                        Volume_of_credit=int(input(f"Please enter your credits at {grading}: "))
                        if Volume_of_credit not in range_of_gradings:
                            raise Invalidrange("Out of range\n")
                        grade_list.append(Volume_of_credit)  #Store the validated values to the list
                        break
                    except ValueError:
                        print("Integer required\n")
    
                    except Invalidrange as e:
                        print(e)
                return Volume_of_credit
            
        grade_list[0]=input_grading("pass")
        grade_list[1]=input_grading("defer")
        grade_list[2]=input_grading("fail")
        
    
        if grade_list[0]+grade_list[1]+grade_list[2]!=120:#Checking the validity of the total(pass+fail+defer==120)
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


        elif(grade_list[0]==120):  #check the conditions and appending the results to the main list        
            main_list.append(f"Progress - {grade_list[0]}, {grade_list[1]}, {grade_list[2]}")
            print("Progress")
            print("\n")
            Total_progress_count+=1
            
        elif(grade_list[0]==100 and (grade_list[1]==20 or grade_list[2]==20)):
            main_list.append(f"Progress (module trailer) - {grade_list[0]}, {grade_list[1]}, {grade_list[2]}")
            print("Progress (module trailer)")
            print("\n")
            Total_trailer_count+=1
            
        elif(grade_list[2]==100 or grade_list[2]==80 or grade_list[2]==120):
            main_list.append(f"Exclude - {grade_list[0]}, {grade_list[1]}, {grade_list[2]}")
            print("Exclude")
            print("\n")
            Total_exclude_count+=1
            
        else:
            main_list.append(f"module retriever - {grade_list[0]}, {grade_list[1]}, {grade_list[2]}")
            print("module retriever")
            print("\n")
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
        elif attempt=="q":#printing and writing each element in the main_list line by line
            now = datetime.datetime.now()
            filename = f"{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.txt"  #Creating each fike with the current year month day hour and minute
            with open(filename, "w") as file:#start the writing inside the file
                for j in main_list:
                    print(j)
                    file.write(f"{j}\n")
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
        aLine = Rectangle(Point(0, 250), Point(425, 250))
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
        outcome_message=Text(Point(163,295), f"{Total_progress_count+Total_trailer_count+Total_retriever_count+Total_exclude_count} outcomes in the total")

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

main()



    
    



    


