
import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="")
list_databases=[]
a=con.cursor()
a.execute("show databases")
for i in a:
        for j in i:
                list_databases.append(j)

if "reaction_tme" in list_databases:                    #creation of database
        a.execute("use reaction_tme")
        con.commit()
        a.close()
    
    
else:
        a.execute("create database reaction_tme")
        a.execute("use reaction_tme")
        a.execute("create table times(name varchar(30),r_time float(18.17),date datetime)")
        a.execute("create table leaderboard(name varchar(30),time float(18.17))")
        con.commit()
        a.close()
        


def reaction_test():
        import time
        import random
        global username
        name=input("enter name-").replace(" ","_")

        username=name.upper()
        print(username)
        for i in range (4):
                avg=0
                if i==0:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("""\t\t\t\t\thello!""")
                        time.sleep(2)
                        print("""\t\t\tWelcome to a very simple reaction test""")
                        time.sleep(3)
                        print("""\t\tPress ENTER when 5 stars appear on the screen in a random time""")
                        time.sleep(3)
                        print("""\tThe time between the appearance of the stars and your keystroke is recorded""")
                        time.sleep(3)
                        print("""\t\t\tThree such tests and the average is taken""")
                        time.sleep(3)
                        print("""\t\t\t\t\tAlL the best""")
                        time.sleep(3)
                        print("""\t\t\tpress enter when u want to begin countdown""")
                        abc=input("")
                        time.sleep(1)
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("""starting...""",end="\n\n")
                        time.sleep(0.5)
            
                else:
                        for j in range(5,-1,-1):
                                if j==5:
                                        print("Reaction test",i,"will start in",end=" ")
                                        time.sleep(1)
                                else:
                                        if j==0:
                                                print(j+1)
                                                print("-",end="")
                                                time.sleep(1)
                                                tme=0
                                                tme+=random.randrange(7)
                                                tme+=random.randrange(100)/100
                                                time.sleep(tme)
                                                x=time.time()
                                                print("*****",end=("-"))
                                                z=input("")
                                                y=time.time()
                                                tmp=y-x
                                                disq=0
                                                if tmp>10:
                                                        print("Time exceeded 10 seconds")
                                                        disq+=1
                                                        continue
                                                else:
                                                        avg+=tmp
                            
                                        else:
                                                print(j+1,end=" ")
                                                time.sleep(1)
        else:
                if disq==3:
                        time.sleep(1)
                        print("no time recorded")
                        r_time=0
                elif disq==2:
                        print("Your reaction time was-",avg)
                        r_time=avg
                elif disq==1:
                        print("Your reaction time was-",avg/2)
                        r_time=avg/2
                else:
                        time.sleep(1)
                        print("Your reaction time was-",avg/3)
                        r_time=avg/3
                print("")
                time.sleep(1)
                return r_time  



def table_check(name,table):
        a=con.cursor()
        a.execute("use reaction_tme")
        a.execute('select count(*) from {} where name="{}"'.format(table,name))
        for i in a:
                for j in i:
                        if j==0:
                                val="no"
                        else:
                                val="yes"
        a.close()
        return val






gg=1
import time
import random
while gg>0:
        print("select the option number according to your needs\n\t1 For registering reaction time\n\t2 leaderboard\n\t3 checking own times\n\t4 last 10 entries\n\t5 TEST STATISTICS \n\t6 TOP TEN in entries\n\t7 Check for data ON AN INDIVITUAL \n\t8 exit program ") 
        gg+=1
        print("")
        q=int(input("ENTER OPTION-"))
        if q==1:
                r_time=reaction_test()

                a=con.cursor()
                a.execute("use reaction_tme")
                a.execute('select r_time from times')                                                                             #times update
                ind_tme=0.00
                count1=0.00
                for i in a:
                        for j in i:
                                ind_tme+=j
                                count1+=1.00
                    
                avg_tme=0.00
                time.sleep(1)

                if count1==0:
                        print("first time recorded")
                elif avg_tme>=r_time:
                        avg_tme=ind_tme/count1
                        print("Your time was better than the world average by",r_time-avg_tme)
                        print("")
                else:
                        avg_tme=ind_tme/count1
                        print("Your time was worse than the world average by",avg_tme-r_time)
                        print("")
                time.sleep(1)
                 
            
                a.execute('insert into times values("{}",{},CURRENT_TIMESTAMP())'.format(username,r_time))
                con.commit()
                a.close()
                

                a=con.cursor()                                                                                                        #leaderboard update
                a.execute("use reaction_tme")
                a.execute('select time from leaderboard where name="{}"'.format(username))
                
                oldtime=-10.00
                for i in a:
                        for j in i:
                               oldtime=j


                if oldtime>0:
                        if oldtime<=r_time:
                                print("leaderboard not updated.")
                        elif r_time<oldtime:
                                a.execute('update leaderboard set time={} where name="{}"'.format(r_time,username))
                                print("Your time has improved by",1-(r_time-oldtime))
                                con.commit()
                else:
                        a.execute('insert into leaderboard values("{}",{})'.format(username,r_time))
                        con.commit()
                        print("leaderboard insertion complete")
                a.close()
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                
                
        elif q==2:
                print("\tL E A D E R B O A R D")
                print("\t---------------------")
                a=con.cursor()
                a.execute("use reaction_tme")
                a.execute("select * from leaderboard order by time")
                twocount=0
                for i in a:
                        twocount+=1
                        print(twocount,". NAME | ",i[0],"\nREACTION | ",i[1])
                        print("-----------------------------------------")
        
                                        
                                
                a.close()
                print("\n")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(2)

                
        elif q==3:
                wname=input("enter name").replace(" ","_")
                wwname=wname.upper()
                valcheck=table_check(wwname,"leaderboard")
                if valcheck=="yes":
                        a=con.cursor()
                        a.execute("use reaction_tme")
                        a.execute('select time from leaderboard where name="{}"'.format(wwname))
                        for i in a:
                                for j in i:
                                        print(j,"is your best time.")
                                        print("")
                                        
                        a.close()

                        a=con.cursor()
                        a.execute("use reaction_tme")
                        a.execute('select r_time,date from times where name="{}" order by date desc'.format(wwname))
                        twocount=0
                        for i in a:
                                twocount+=1
                                print(twocount,". REACTION TIME | ",i[0],"\nDATE & TIME | ",i[1])
                                print("-----------------------------------------")
                        
                        a.close()                 
                                
                else:
                        print("NAME NOT ON LEADERBOARD")
                print("\n")
                
                time.sleep(2)
                

                
        elif q==4:
                print("")
                print("SHOWING LAST TEN ENTRIES IN THE LOG")
                print("-----------------------------------------")
                count4=0
                a=con.cursor()
                a.execute("use reaction_tme")
                a.execute("select * from times order by date desc")
                for i in a:
                        count4+=1
                        if count4<=10:
                                print("\t",i[0],"-\n\t",i[1],"-",i[2])
                                print("-----------------------------------------")
                        
                print("\n")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                a.close()
                        
                                        


        elif q==5:
                print("")
                a=con.cursor()
                a.execute("use reaction_tme")
                a.execute('select r_time from times')                                                                             #times update
                ind_tme=0.00
                count1=0.00
                for i in a:
                        for j in i:
                                ind_tme+=j
                                count1+=1.00
                    
                avg_tme=0.00
                a.close()
                time.sleep(1)

                if count1==0:
                        print("No times added")
                else:
                        a=con.cursor()
                        a.execute("use reaction_tme")
                        a.execute("select count(*) from leaderboard")
                        for i in a:
                                for j in i:
                                        print(j,"people participated")
                        print("")
                        a.close()
                        print("No of TOTAL ENTRIES-",count1)
                        avg_tme=ind_tme/count1
                        print("")
                        a=con.cursor()
                        a.execute("use reaction_tme")
                        a.execute("select * from times order by r_time")
                        icount=0
                        for i in a:
                                icount+=1
                                for j in i:
                                        if icount==1:
                                                print("The best reaction time is",i[1],"achieved by",i[0])
                                                break
                                        if icount==count1:
                                                print("The best worst time is",i[1],"made by",i[0])
                                                break
                                                
                                        
                        a.close()
                        print("")
                        

                        print("THE WORLD AVERAGE REACTION TIME IS-",avg_tme)
                        print("")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(1.5)
                

                
        elif q==6:
                a=con.cursor()
                a.execute("use reaction_tme")
                print("")
                print("SHOWING TEN ENTRIES IN THE LOG")
                print("-----------------------------------------")
                count4=0
                a=con.cursor()
                a.execute("use reaction_tme")
                a.execute("select * from times order by r_time")
                for i in a:
                        count4+=1
                        if count4<=10:
                                print("\t",i[0],"-\n\t",i[1],"-",i[2])
                                print("-----------------------------------------")
                        
                print("\n")
                a.close()
                time.sleep(1)

                
        
                
        elif q==7:
                print("")
                print("USER DETAILS")
                print("-----------------------------------------")
                a=con.cursor()
                a.execute("use reaction_tme")
                qty=input("enter name").replace(" ","_")
                wwqty=qty.upper()
                check123=table_check(wwqty,"leaderboard")
                a.close()
                if check123=="no":
                        print("NO PERSON IN DATALOG")
                else:
                        a=con.cursor()
                        a.execute("use reaction_tme")
                        a.execute('select * from leaderboard')
                        wwcount=0
                        for i in a:
                                wwcount+=1
                                if i[0]==wwqty:
                                        print("BEST TIME-",i[1])
                                        print("")
                                        print(wwcount,"position in the world")
                                        print("")
                        a.close()

                        a=con.cursor()
                        count7=0
                        a.execute("use reaction_tme")
                        a.execute('select * from times where name="{}" order by r_time desc'.format(wwqty))
                        for i in a:
                                count7+=1
                                if count7==1:
                                        print("User's first entry on",i[2])
                                        print("")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(1)
                a.close()
                
        elif q==8:
                gg=-1
                print("Thanks for using this program!")
                time.sleep(1)
                print("HAVE A GOOD DAY MADAM/SIR!!!!")
                        
        


        else:
                print("______________________________")
                print("ENTER CORRECT OPTION PLEASE!!!")
                print("______________________________")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
                print("")
                time.sleep(1)

    






a.close()
con.close()


          
                    
                    
                
