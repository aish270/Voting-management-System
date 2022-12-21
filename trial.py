import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',password='biot',database='voters')
cursor=mycon.cursor()
cursor.execute("use voters")




ans_='c'
while ans_=='c':
    cursor.execute("select voter_id from voter_info")
    

    v_id=cursor.fetchall()
    print(v_id)
    cursor.execute("select voterid from votes")
    voted=cursor.fetchall()
    
    
    print("                                 <WELCOME>         ")
    
    

    print("""                        1)VOTE


                        2)REGISTER

                        
                        3)VIEW VOTER INFORMATION

                        
                        4)CHANGE VOTERID

                        
                        5)VOTING RESULTS
                        
                        
                        6)DISTRIBUTION OF VOTES         """)

    

    choice=int(input("  Enter your choice here :  "))
    ans='y'
    if choice==1:
         while ans=='y':
        
            
            vid=int(input("voterid: "))
            vd=(vid,)
        
            if vd in v_id and vd not in voted:
                print("""                                  Vote for Leftfront :  enter left

                                   Vote for Westfront :  enter west
                                   
                                   Vote for Republic party:  enter republic            """)
                
                vt=input("""

                                   cast your vote (left/west/republic) : """)
                
                str2="insert into votes values({},'{}')".format(vid,vt)
                cursor.execute(str2)
                mycon.commit()
                
                
                
                
                
                v_id.remove(vd)
                ans=input("want to continue?(y/n)")
            else:
                print("invalid voterid")
                ans=input("want to continue?(y/n)")
         
         
         print("                                 SUCCESSFULLY VOTED:)    ")
         
         ans_=input("do you want to continue (c/n)")        
    elif choice==2:
         import random
         print("""
                              Register here !!!



                                                      """)
         name=input("    Enter your name  :  ")
         district=input("    Enter your district name :  ")
         age=int(input("    Enter your age :   "))
         vid=random.randint(20000,50000)
         str1="insert into voter_info values('{}','{}',{},{})".format(name,district,age,vid)
         cursor.execute(str1)
         mycon.commit()
         cursor.execute("select*from voter_info")
         v_data=cursor.fetchall()
         
         ans_=input("do you want to continue (c/n)")
    elif choice==3:
         cursor.execute("select*from voter_info")
         v_data=cursor.fetchall()
         count=cursor.rowcount
         print("""                      registered voters:-


                                                                           """)
         for i in v_data:
             print(i)
         print("                        Number of people registered:    ",count)
         ans_=input("do you want to continue (c/n)")
    elif choice==4:
         old_id=int(input("enter your old id"))
         new_id=int(input("enter your new id"))
         str2="UPDATE voter_info SET voter_id={} where voter_id={}".format(new_id,old_id)
         cursor.execute(str2)
         mycon.commit
         str3="select*from voter_info where voter_id={}".format(new_id)
         cursor.execute(str3)
         print("            modified voter_id")
         mv=cursor.fetchall()
         print(mv)
         ans_=input("do you want to continue (c/n)")              
    elif choice==5:
         
         print("""

                                 VOTING RESULTS      !!!

                                                                       """)
         cursor.execute("select vote,count(*) from votes GROUP BY vote")
                
         vts=cursor.fetchall()
         print(vts)
         a=vts[0]
         b=vts[1]
         c=vts[2]
         print(a[0],"scored",a[1],"votes")
         print(b[0],"scored",b[1],"votes")
         print(c[0],"scored",c[1],"votes")
         if a[1]==b[1]==c[1]:
             print("                     Its a tie!!! ")
         elif a[1]==b[1] and c[1]<a[1]:
             print ("                    Its a tie!!! ")
         elif b[1]==c[1] and a[1]<b[1]:
             print("Its a tie")
         elif c[1]==a[1] and b[1]<a[1]:
             print("Its a tie")
         
        
         elif max(a[1],b[1],c[1])==a[1]:
             
             print(                      a[0]," has won")
         elif max(a[1],b[1],c[1])==b[1]: 
             print(                      b[0]," has won")
         elif max(a[1],b[1],c[1])==c[1]: 
             print(                      c[0]," has won")
        
         ans_=input("do you want to continue  (c/n)")
        
    elif choice==6:
         cursor.execute("select vote,count(*) from votes GROUP BY vote")
                
         vts=cursor.fetchall()
        
         a=vts[0]
         b=vts[1]
         c=vts[2]
         import matplotlib.pyplot as mp
         parties=(a[0],b[0],c[0])
         print(parties)
         votes=(a[1],b[1],c[1])
         colors=['red','yellow','blue']
        
         explode=(0,0,0)
         
         mp.pie(votes,labels=parties, colors=colors, explode=explode, autopct='%1.0f%%')
         mp.title('distribution of votes')
         mp.show()
         ans_=input("do you want to continue and vote? (c/n)")
         
    
    

        
            
