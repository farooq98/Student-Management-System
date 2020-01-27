from ast import literal_eval
#from IPython.display import clear_output
import datetime
while True:
    #clear_output()
    print("\t\tStudent Management System")
    now=datetime.datetime.now()
    print("1: Adminstartion\n2: Faculty\n3: Student Portal")
    select=input("Please Select Or Press x to exit: ")
    if select=="1":
        while True:
            #clear_output()
            print("\t\tAdministration")
            print("1: Student Registration\n2: Student Data\n3: Facilty Registration\n4: Faculty Data\n5: Courses")
            sel=input("Please Select or press y to go back: ")
            if sel=="1":
                while True:
                    #clear_output()
                    #data={}
                    readfile=open("student.txt","r")
                    data=readfile.read()
                    #print(type(data))
                    #print(data)
                    if data=="":
                        data={}
                    else:
                        data=literal_eval(data)
                    readfile.close()
                    #data=literal_eval(data)
                    #print(type(data))
                    #print(data)
                    #file.write(str(data))
                    #file.close()
                    print("\t\tStudent Registration")
                    Fn=input("First Name: ")
                    Ln=input("Last Name: ")
                    Ad=input("Address: ")
                    Ct=input("City: ")
                    Count=input("Country: ")
                    Dis=input("Discipline: ")
                    #Bat=input("Batch: ")
                    sem=int(input("Semester: "))
                    Hsc=int(input("HSC Marks: "))
                    Ssc=int(input("SSC Marks: "))
                    #sid=2
                    for i in data:
                        sid=i.split("-")
                    roll=now.strftime("%yB-"+str(int(sid[1])+1)+"-"+Dis)
                    #print(roll)
                    data.update({roll:{"fname":Fn,"lname":Ln,"address":Ad,"city":Ct,"country":Count,"discipline":Dis.upper(),"semester":sem,"HSC":Hsc,"SSC":Ssc}})
                    file=open("student.txt","w")
                    file.write(str(data))
                    file.close()
                    print("Registration Successful")
                    print("Your Roll Number is: "+roll)
                    studentpassdatafile=open("studentpass.txt","r")
                    studentpassdata=studentpassdatafile.read()
                    passwordstd="12345678"
                    if studentpassdata=="":
                        studentpassdata={}
                    else:
                        studentpassdata=literal_eval(studentpassdata)
                    studentpassdata.update({roll:passwordstd})
                    updatestudentpassdatafile=open("studentpass.txt","w")
                    updatestudentpassdatafile.write(str(studentpassdata))
                    updatestudentpassdatafile.close()
                    admin1=input("Press y to go back: ")
                    if admin1.lower()=="y":
                        break
            elif sel=="2":
                while True:
                    print("\t\tStudent Data")
                    studentroll=input("Roll Number: ")
                    stdfile=open("student.txt","r")
                    stddata=stdfile.read()
                    stddata=literal_eval(stddata)
                    tempstd=stddata[studentroll]
                    #print(tempstd)
                    for i,j in tempstd.items():
                        print(i.title()+": "+str(j))
                    stdfile.close()
                    admin2=input("Press y to go back: ")
                    if admin2.lower()=="y":
                        break
            elif sel=="3":
                while True:
                    #clear_output()
                    facfile=open("sfaculty.txt","r")
                    facdata=facfile.read()
                    if facdata=="":
                        facdata={}
                    else:
                        facdata=literal_eval(facdata)
                    #print(facdata)
                    print("\t\tFaculty Registration")
                    ffn=input("First Name: ")
                    fln=input("Last Name: ")
                    fadd=input("Address: ")
                    fct=input("City: ")
                    fc=input("Country: ")
                    fedu=input("Education: ")
                    fsale=input("Salary Package: ")
                    if facdata=={}:
                        num=1
                    for i in facdata:
                        num=i[-1]
                    fid=ffn[0].lower()+fln.lower()+str(int(num)+1)
                    facwrite=open("sfaculty.txt","w")
                    facdata.update({fid:{"fname":ffn,"lname":fln,"address":fadd,"city":fct,"country":fc,"education":fedu,"salary":fsale}})
                    facwrite.write(str(facdata))
                    print("Faculty ID: "+fid)
                    print("Registration Successful")
                    password="12345678"
                    facultypass=open("sfacultyuser.txt","r")
                    facultypassdata=facultypass.read()
                    if facultypassdata=="":
                        facultypassdata={}
                    else:
                        facultypassdata=literal_eval(facultypassdata)
                    facultypass.close()
                    facultypassdata.update({fid:password})
                    updatefacultypass=open("sfacultyuser.txt","w")
                    updatefacultypass.write(str(facultypassdata))
                    updatefacultypass.close()
                    facwrite.close()
                    admin3=input("Press Y to go back: ")
                    if admin3.lower()=="y":
                        break
            elif sel=="4":
                while True:
                    #clear_output()
                    print("\t\tFaculty Data")
                    facultyid=input("Faculty ID: ")
                    facultyfile=open("sfaculty.txt","r")
                    facultydata=facultyfile.read()
                    facultydata=literal_eval(facultydata)
                    tempfac=facultydata[facultyid]
                    #print(tempstd)
                    for i,j in tempfac.items():
                        print(i.title()+": "+str(j))
                    facultyfile.close()
                    admin4=input("Press y to go back: ")
                    if admin4.lower()=="y":
                        break
            elif sel=="5":
                while True:
                    #clear_output()
                    coursefile=open("course.txt","w")
                    courses={"se":{1:["Introduction to Information and Communication Technology (ICT)\t3+1","Programming Fundamentals\t3+1","Basic Electronics\t2+1","English Composition and Comprehension\t3+0","Islamic Studies/Ethics\t2+0","Calculus and Analytical Geometry\t3+0"],2:["Object Oriented Programming\t3+1","Discrete Structures\t3+0","Digital Logic Design\t3+1","Communication Skills\t3+0","Pakistan Studies\t2+0"],3:["Data Structures and Algorithms\t3+1","Technical and Business Writing\t3+0","Linear Algebra\t3+0","Probability and Statistics\t3+0","Supporting Elective-I\t3+0"],4:["Introduction to Software Engineering\t3+0","Data Communication and Computer Networks\t3+1","Supporting Elective-II\t3+0","Gen. Education/University Elective –II\t3+0","Gen. Education/University Elective -III\t3+0"],5:["Introduction to Database Systems\t3+1","Operating Systems\t3+1","Object Oriented Software Engineering\t3+1","SE Elective I\t3+0","Gen. Education/University Elective -IV\t3+0"],6:["Software Requirement Engineering\t3+0","Software Design and Architecture\t3+0","Software Verification and Validation\t3+0","SE Elective II\t2+1","SE Elective III\t3+0","Supporting Elective-III\t3+0"],7:["Human Computer Interaction\t2+1","Software Project Management\t3+0","Final Year Project\t0+3","SE Application Domain Elective- I\t3+0","SE Elective IV\t3+0"],8:["Professional Practices\t3+0","Final Year Project\t0+3","SE Application Domain Elective - II\t3+0","SE Elective V\t3+0"]},"cs":{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]},"ee":{1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}}
                    coursefile.write(str(courses))
                    coursefile.close()
                    del courses
                    readcoursefile=open("course.txt","r")
                    coursedata=readcoursefile.read()
                    coursedata=literal_eval(coursedata)
                    semester=int(input("Enter Semester: "))
                    discipline=input("Enter Discipline: ")
                    print("\t\tCourses")
                    tempcourse=coursedata[discipline.lower()][semester]
                    num=1
                    for i in tempcourse:
                        print(num,": "+i)
                        num+=1
                    admin5=input("Press y to go back: ")
                    if admin5.lower()=="y":
                        break
            else:
                print("Invalid Selection")
            #again2=input("Press Y to go back to the main menu: ")
            if sel=="y":
                break
    if select=="2":
        #clear_output()
        print("\t\tFaculty")
        facusername=input("Faculty ID: ")
        facpassword=input("Password: ")
        #clear_output()
        facultyuserpass=open("sfacultyuser.txt","r")
        facultyuserpassdata=facultyuserpass.read()
        facultyuserpassdata=literal_eval(facultyuserpassdata)
        if facusername in facultyuserpassdata:
            if facpassword==facultyuserpassdata[facusername]:
                while True:
                    #clear_output()
                    print("\t\tFaculty")
                    print("1: Batch and Sections\n2: Personal Information\n3: Change Password")
                    opt=input("Please Select or press y to go back: ")
                    #print("wah")
                    if opt=="1":
                        pass
                    elif opt=="2":
                        while True:
                            #clear_output()
                            print("\t\tPersonal Info")
                            #facultyid=input("Faculty ID: ")
                            facultyfile=open("sfaculty.txt","r")
                            facultydata=facultyfile.read()
                            facultydata=literal_eval(facultydata)
                            tempfac=facultydata[facusername]
                            #print(tempstd)
                            for i,j in tempfac.items():
                                print(i.title()+": "+str(j))
                            facultyfile.close()
                            again4=input("Press Y to go back: ")
                            if again4 == "y":
                                break
                    elif opt=="3":
                        while True:
                            #clear_output()
                            print("\t\tChange Password")
                            newpass=input("New Passwprd: ")
                            confirmnewpass=input("Confirm Password: ")
                            if newpass==confirmnewpass:
                                readchangepass=open("sfacultyuser.txt","r")
                                facultypassinfo=readchangepass.read()
                                readchangepass.close()
                                facultypassinfo=literal_eval(facultypassinfo)
                                facultypassinfo[facusername]=newpass
                                changepass=open("sfacultyuser.txt","w")
                                changepass.write(str(facultypassinfo))
                                changepass.close()
                                #clear_output()
                                print("Password Changed")
                                facsel=input("Press y to go back: ")
                                if facsel=="y":
                                    break
                            else:
                                print("New password and confirm password doesn't match")
                    else:
                        print("Invalid Selection")
                    #again3=input("Press Y to go back: ")
                    if opt == "y":
                        break
    if select=="3":
        #clear_output()
        print("\t\tStudent Portal")
        stdusername=input("Roll Number: ")
        stdpassword=input("Password: ")
        studentuserpass=open("studentpass.txt","r")
        studentuserpassdata=studentuserpass.read()
        studentuserpassdata=literal_eval(studentuserpassdata)
        if stdusername in studentuserpassdata:
            if stdpassword==studentuserpassdata[stdusername]:
                while True:
                    #clear_output()
                    print("\t\tStudent Portal")
                    print("1: Attendance Details\n2: Sessional Details\n3: Personal Information\n4: Change Password")
                    selopt=input("Please Select or press y to go back: ")
                    if selopt=="1":
                        pass
                    elif selopt=="2":
                        pass
                    elif selopt=="3":
                        while True:
                            #clear_output()
                            print("\t\tPersonal Info")
                            studentdatafile=open("student.txt","r")
                            studentdata=studentdatafile.read()
                            studentdata=literal_eval(studentdata)
                            tempstddata=studentdata[stdusername]
                            for i,j in tempstddata.items():
                                print(i.title()+": "+str(j))
                            studentdatafile.close()
                            selection=input("Press y to go back: ")
                            if selection=="y":
                                break
                    elif selopt=="4":
                        while True:
                            #clear_output()
                            print("\t\tChange Password")
                            stdnewpass=input("New Passwprd: ")
                            stdconfirmnewpass=input("Confirm Password: ")
                            if stdnewpass==stdconfirmnewpass:
                                readstudentchangepass=open("studentpass.txt","r")
                                studentpassinfo=readstudentchangepass.read()
                                readstudentchangepass.close()
                                studentpassinfo=literal_eval(studentpassinfo)
                                studentpassinfo[stdusername]=stdnewpass
                                stdchangepass=open("studentpass.txt","w")
                                stdchangepass.write(str(studentpassinfo))
                                stdchangepass.close()
                                #clear_output()
                                print("Password Changed")
                                stdselect=input("Press y to go back: ")
                                if stdselect=="y":
                                    break
                            else:
                                print("New password and confirm password doesn't match")
                    else:
                        print("Invalid Selection")
                    if selopt=="y":
                        break
    #again=input("Press Y to restart: ")
    if select == "x":
        #clear_output()
        print("Program Terminated")
        break
