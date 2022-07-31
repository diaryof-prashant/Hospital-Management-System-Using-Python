import mysql.connector as sc
from datetime import date

con=sc.connect(host='localhost',user='root',passwd='12345',database='hospital')
if con.is_connected():
    print('Connection to Database Success')
else:
    print('Connection to Database Failed')
cur=con.cursor()


#-----------------------------------PATIENT-------------------------
def patient():
    print()
    print('This is Patient Management')
    b=input("""Enter you choice from the following options
                    1. Show all record
                    2. Show specific record
                    3. Add Record
                    4. Modify Record
                    5. Delete Record
                    6. Back to main menu
                    :""")
    if b.isnumeric()==True:
        choice1(b)
    else:
        print('Invalid input, Try again')
        patient()

def choice1(b):
    if b=='1':
        print('This is show all record section of Patient Management')
        print('Showing all records of patient table. . . . ')
        print('')
        cur.execute('select * from patient')
        data=cur.fetchall()
        print("(PID),(PNAME),(AGE),(GENDER),(ADDRESS),(TYPE)")
        for i in data:
            print(i)
        err=input('Do you want to go back?[y/n]')
        if err=='y':
            patient()
        else:
            exitt()

    elif b=='2':
        def shs():
            print('This is show specific record section of Patient Management')
            def id1():
                global ID
                ID=input('Enter Patient ID:')
                if ID.isnumeric()==True and len(ID)<5:
                    pass
                else:
                    print('Invalid Input')
                    id1()
            id1()
            def Name1():
                global Name
                Name=input('Enter Patient Name:')
                if Name.isalpha()==True and len(Name)<30:
                    pass
                else:
                    print('Invalid Input')
                    Name1()
            Name1()
            sql='select * from Patient where PID=%s or PName=%s'
            param=(int(ID),Name)
            cur.execute(sql,param)
            data=cur.fetchall()
            print("(PID),(PNAME),(AGE),(GENDER),(ADDRESS),(TYPE),(DATE OF ADMISSION)")
            print('')
            for i in data:
                print(i)
            innu=input('Do you want to try again?[y/n]:')
            if innu=='y':
                    shs()
            else:
                    patient()
            
        shs()

    elif b=='3':
        def addr():
            print('This is addition of record section of Patient Management')
            def pid2():
                global pid
                pid=input('Enter Patient ID:')
                if pid.isnumeric()==True and len(pid)<5:
                    pass
                else:
                    print('Invalid Input')
                    pid2()
            pid2()
            def pname2():
                global pname
                pname=input('Enter Patient Name:')
                if pname.isalpha()==True and len(pname)<30:
                    pass
                else:
                    print('Invalid Input')
                    pname2()
            pname2()
            def age2():
                global age
                age=input('enter patient age:')
                if age.isnumeric()==True and len(age)<3:
                    pass
                else:
                    print('Invalid Input')
                    age2()
            age2()
            def gender2():
                global gender
                gender=input("enter patient's gender(M/F):")
                if gender.isalpha()==True and len(gender)==1 and (gender=='M' or gender=='F'):
                    pass
                else:
                    print('Invalid Input')
                    gender2()
            gender2()
            def address2():
                global address
                address=input('enter patient address:')
                if address.isalpha()==True and len(address)<50:
                    pass
                else:
                    print('Invalid Input')
                    address2()
            address2()
            def Type2():
                global Type 
                Type=input('enter patient type[in]:')
                if Type.isalpha()==True and len(Type)<4 and (Type=='in' or Type=='out'):
                    pass
                else:
                    print('Invalid Input')
                    Type2()
            Type2()
#            if Type=='in':
#                def doa2():
#                    global doa
#                    doa=input('Enter Patient date of admission in format(yyyy-mm-dd):')
#                    if len(doa)==10:
#                        pass
            
#                    else:
#                        print('Invalid Input')
#                        doa2()
#                doa2()
#            else:
#                pass            
            sql='insert into patient(pid,pname,age,gender,address,Type) values(%s,%s,%s,%s,%s,%s)'
            recs=(int(pid),pname,int(age),gender,address,Type)
             
            try:
                cur.execute(sql,recs)
                con.commit()
                print('Inserted Successfully')
            except:
                con.rollback()
                print('Insertion Failed ')
            inu=input('Do you want to add more records?[y/n]:')
            if inu=='y':
                addr()
            else:
                patient()
            
        addr()

    elif b=='4':
        def mod1():
            print('This is modification of record section of Patient Management')
            rego=input("""Enter your choice from following options
                        1. Address Change
                        2. Go back to Patient Menu""")
            if rego.isnumeric()==True:
                if rego=='1':
                    def ad1():
                        print('You chose to change address')
                        def ID3():
                            global ID
                            ID=input("Enter Patient's ID:")
                            if ID.isnumeric()==True:
                                pass
                            else:
                                print('Invalid Input')
                                ID3()
                        ID3()
                        def Name3():
                            global Name 
                            Name=input('Enter Patient Name:')
                            if Name.isalpha()==True:
                                pass
                            else:
                                print('Invalid Input')
                                Name3()
                        Name3()
                        def Address3():
                            global Address
                            Address=input('Enter new address:')
                            if Address.isalpha()==True and len(Address)<50:
                                pass
                            else:
                                print('Invalid Input')
                                Address3()
                        Address3()
                        sql='Update Patient set Address=%s where PID=%s or PName=%s'
                        param=(Address,int(ID),Name)
                        try:
                            cur.execute(sql,param)
                            print('Updated Successfully')
                        except:
                            con.rollback()
                            print('Updation Failed')
                        inpu=input('Do you want to continue with address modification?[y/n] :')
                        if inpu=='y':
                            ad1()
                        else:
                            mod1()
                        

                    ad1()

                

                elif rego=='2':
                    print('You chose to go back to Patient menu')
                    print('Taking you back. . . .')
                    patient()

                else:
                    print('Invalid Input, try again')
                    mod1()
            else:
                print('Invalid input, Try again!')
                mod1()

        mod1()

    elif b=='5':
        def del1():
            print('This is deletion of record section')
            def ID4():
                global ID
                ID=input('Enter Patient ID:')
                if ID.isnumeric()==True and len(ID)<5:
                    pass
                else:
                    print('Invalid Input')
                    ID4()
            ID4()
            def Name4():
                global Name
                Name=input('Enter Patient Name:')
                if Name.isalpha()==True and len(Name)<30:
                    pass
                else:
                    print('Invalid Input')
                    Name4()
            Name4()
            sql='delete from Patient where PID=%s or PName=%s'
            recs=(int(ID),Name)
            try:
                cur.execute(sql,recs)
                con.commit()
                print('Deletion Success')
            except:
                con.rollback()
                print('Deletion Failed')
            inno=input('Do you want to continue with deletion of records?[y/n]:')
            if inno=='y':
                del1()
            else:
                patient()
            
        del1()

    elif b=='6':
        print('Taking you back to Main Menu. . . .')
        main()

    else:
        print('Invalid Input, Try again!')
        patient()




#-----------------------------------DOCTOR-----------------------------------
def doctor():
    print()
    print('This is Doctor Management')
    c=input("""Enter your choise from the following options
                1. Show all record
                2. Show specific record
                3. Add record
                4. Modify record
                5. Delete record
                6. Back to main menu
                :""")
    if c.isnumeric()==True:
        choice2(c)
    else:
        print('Invalid Input, Try again')
        doctor()

def choice2(c):
    if c=='1':
        print('This is show all record section of Patient Management')
        print('Showing all records of doctor table. . . . ')
        cur.execute('select * from doctor')
        data=cur.fetchall()
        print("(DID),(DNAME),(QUALIFICATION),(SPECIALIZATION),(DEPARTMENT),(EXPERIENCE),(CONTACT_INFO),(CHARGE)")
        print('')
        for i in data:
            print(i)
        err=input('Do you want to go back?[y/n]')
        if err=='y':
            doctor()
        else:
            exitt()
         
    elif c=='2':
        def shr():
            print('This is show specific record section of Doctor Management')
            def ID5():
                global ID
                ID=input('Enter Doctor ID:')
                if ID.isnumeric()==True and len(ID)<5:
                    pass
                else:
                    print('Invalid Input')
                    ID5()
            ID5()
            def Name5():
                global Name
                Name=input('Enterr Doctor Name:')
                if Name.isalpha()==True and len(Name)<30:
                    pass
                else:
                    print('Invalid Input')
                    Name5()
            Name5()
            sql='select * from Doctor where DID=%s or DName=%s'
            param=(int(ID),Name)
            cur.execute(sql,param)
            data=cur.fetchall()
            print("(DID),(DNAME),(QUALIFICATION),(SPECIALIZATION),(DEPARTMENT),(EXPERIENCE),(CONTACT_INFO),(CHARGE)")
            print('')
            for i in data:
                print(i)
            innu=input('Do you want to try again?[y/n]:')
            if innu=='y':
                    shr()
            else:
                    doctor()
            

        shr()

    elif c=='3':
        def addr1():
            print('This is addition of record section of Doctor Management')
            def did6(): 
                global did
                did=input('enter doctor id:')
                if did.isnumeric()==True and len(did)<5:
                    pass
                else:
                    print('Invalid Input')
                    did6()
            did6()
            def dname6():
                global dname
                dname=input('enter doctor name:')
                if dname.isalpha()==True and len(dname)<30:
                    pass
                else:
                    print('Invalid Input')
                    dname6()
            dname6()
            def qualification6():
                global qualification
                qualification=input('enter doctor qualification:')
                if qualification.isalpha()==True:
                    pass
                else:
                    print('Invalid Input')
                    qualification6()
            qualification6()
            def specialization6():
                global specialization
                specialization=input('enter doctor specialization:')
                if specialization.isalpha()==True:
                    pass
                else:
                    print('Invalid Input')
                    specialization6()
            specialization6()
            def department6():
                global department
                department=input('enter doctor department:')
                if department.isalpha()==True:
                    pass
                else:
                    print('Invalid Input')
                    department6()
            department6()
            def experience6():
                global experience
                experience=input('enter doctor experience(number of years):')
                if experience.isnumeric()==True and len(experience)<3 and int(experience)<70:
                    pass
                else:
                    print('Invalid Input')
                    experience6()
            experience6()
            def cinfo6():
                global cinfo
                cinfo=input('enter doctor contact information:')
                if cinfo.isnumeric()==True and len(cinfo)==10:
                    pass
                else:
                    print('Invalid Input')
                    cinfo6()
            cinfo6()
            def chargee6():
                global chargee
                chargee=input('Enter Fees of doctor:')
                if chargee.isnumeric()==True and len(chargee)<5:
                    pass
                else:
                    print('Invalid Input')
                    chargee6()
            chargee6()
            sql='insert into doctor(did,dname,qualification,specialization,department,experience,contact_info,charge) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            recs=(int(did),dname,qualification,specialization,department,int(experience),int(cinfo),int(chargee))
            try:
                cur.execute(sql,recs)
                con.commit()
                print('Inserted Successfully')
            except:
                con.rollback()
                print('Insertion Failed ')
            indo=input('Do you want to add more records?[y/n] :')
            if indo=='y':
                addr1()
            else:
                doctor()

        addr1()

    elif c=='4':
        def mod2():
            print('This is modification of record section of Doctor Management')
            rgo=input("""Enter your choice from the following options
                            1. Contact Info Change
                            2. Back to Doctor Menu
                            :""")
            if rgo.isnumeric()==True:
                if rgo=='1':
                    print('You chose to change contact info')
                    def DID7():
                        global DID
                        DID=input('Enter Doctor ID:')
                        if DID.isnumeric()==True and len(DID)<5:
                            pass
                        else:
                            print('Invalid Input')
                            DID7()
                    DID7()
                    def DName7():
                        global DName
                        DName=input('Enter Doctor name:')
                        if DName.isalpha()==True and len(DName)<30:
                            pass
                        else:
                            print('Invalid Input')
                            DName7()
                    DName7()
                    def CINFO7():
                        global CINFO
                        CINFO=input('Enter new Contact Info')
                        if CINFO.isnumeric()==True and len(cinfo)<11:
                            pass
                        else:
                            print('Invalid Input')
                            CINFO7()
                    CINFO7()
                    mysql='update Doctor set CONTACT_INFO=%s where DID=%s or DName=%s'
                    param=(int(CINFO),int(DID),DName)
                    try:
                        cur.execute(mysql,param)
                        con.commit()
                        print('Inserted successfully')
                    except:
                        con.rollback()
                        print('Insertion Failed')
                    indo=input('Do you want to continue with modification of Doctor records?[y/n] :')
                    if indo=='y':
                          mod2()
                    else:
                          doctor()
                elif rgo=='2':
                    print('You chose to go back to Doctor Menu')
                    print('Taking you back. . . .')
                    doctor()
                else:
                    print('Invalid input, Try again')
                    mod2()
            else:
                print('Invalid input, Try again')
                mod2()
        mod2()


    elif c=='5':
        def del2():
            print('This is deletion of record section')
            def ID8(): 
                global ID
                ID=input('Enter Doctor ID:')
                if ID.isnumeric()==True and len(ID)<5:
                    pass
                else:
                    print('Invalid Input')
                    ID8()
            ID8()
            def Name8():
                global Name
                Name=input('Enter Doctor Name:')
                if Name.isalpha()==True and len(Name)<30:
                    pass
                else:
                    print('Invalid Input')
                    Name8()
            Name8()
            sql="delete from doctor where DID=%s or DName=%s"
            param=(int(ID),Name)
            try:
                cur.execute(sql,param)
                con.commit()
                print('Deleted Successfully')
            except:
                con.rollback()
                print('Deletion Failed')
            indu=input('Do you want to continue with deletion of records?[y/n]:')
            if indu=='y':
                del2()
            else:
                doctor()
            
        del2()

    elif c=='6':
        print('Taking you back to Main Menu. . . ')
        main()

    else:
        print('Invalid Input, Try again')
        doctor()



#--------------------------------Employees-----------------------------------
def employee():
    print()
    print('This is Employee Management')
    d=input("""Enter you choice from the following options
                1. Show all record
                2. Show specific record
                3. Add Record
                4. Modify Record
                5. Delete Record
                6. Back to main menu
                :""")
    if d.isnumeric()==True:
        choice3(d)
    else:
        print('Invalid Input, Try again')
        employee()

def choice3(d):
    if d=='1':
        print('This is show all record section of Employee Management')
        print('Showing all records of Employee table. . . .')
        cur.execute('Select * from Employee')
        data=cur.fetchall()
        print("(EID),(ENAME),(FIELD),(CONTACT_INFO)")
        print('')
        for i in data:
            print(i)
        elo=input('Do you want to go back?[y/n]:')
        if elo=='y':
            employee()
        else:
            exitt()

    elif d=='2':
        def shl():
            print('This is show specific record section of Employee Management')
            def ID9():
                global ID
                ID=input('Enter Employee ID:')
                if ID.isnumeric()==True and len(ID)<5:
                    pass
                else:
                    print('Invalid Input')
                    ID9()
            ID9()
            def Name9(): 
                global Name
                Name=input('Enter Employee NAme:')
                if Name.isalpha()==True and len(Name)<30:
                    pass
                else:
                    print('Invalid Input')
                    Name9()
            Name9()                                                         
            sql='Select * from Employee where EID=%s or Ename=%s'
            param=(int(ID), Name)
            cur.execute(sql,param)
            data=cur.fetchall()
            print("(EID),(ENAME),(FIELD),(CONTACT_INFO)")
            print('')
            for i in data:
                print(i)
            do=input('Do you want to try again?[y/n] :')
            if do=='y':
                shl()
            else:
                employee()
            
        shl()

    elif d=='3':
        def ear():
            print('This is a record insertion section of Employee Management')
            def EID10():
                global EID 
                EID=input('Enter Employee ID:')
                if EID.isnumeric()==True and len(EID)<5:
                    pass
                else:
                    print('Invalid Input')
                    EID10()
            EID10()
            def Ename10():
                global Ename
                Ename=input('Enter Employee Name:')
                if Ename.isalpha()==True and len(Ename)<30:
                    pass
                else:
                    print('Invalid Input')
                    Ename10()
            Ename10()
            def Field10():
                global Field
                Field=input('Enter Field Name:')
                if Field.isalpha()==True:
                    pass
                else:
                    print('Invalid Input')
                    Field10()
            Field10()
            def CINFO10():
                global CINFO
                CINFO=input('Enter contact information:')
                if CINFO.isnumeric()==True and len(CINFO)<11:
                    pass
                else:
                    print('Invalid Input')
                    CINFO10()
            CINFO10()
            sql='insert into employee(EID,EName,Field,contact_info) values(%s,%s,%s,%s)'
            recs=(int(EID),Ename,Field,int(CINFO))
            try:
                cur.execute(sql,recs)
                con.commit()
                print('Inserted Successfully')
            except:
                con.rollback()
                print('Insertion Failed')
            eno=input('Do you want to insert more records?[y/n] :')
            if eno=='y':
                ear()
            else:
                employee()
        ear()

    elif d=='4':
        def mod3():
            print('This is modification of record section of Employee Management')
            rello=input("""Enter your choice from the following options
                            1. Contact Info
                            2. Go back to Employee Menu
                            : """)
            if rello.isnumeric()==True:
                if rello=='1':
                    def cicc():
                        print("You chose to change Contact Info")
                        def EID11():
                            global EID
                            EID=input('Enter Employee ID: ')
                            if EID.isnumeric()==True and len(EID)<5:
                                pass
                            else:
                                print('Invalid Input')
                                EID11()
                        EID11()
                        def EName11():
                            global EName                          
                            EName=input('Enter Employee Name: ')
                            if EName.isalpha()==True and len(EName)<30:
                                pass
                            else:
                                print('Invalid Input')
                                EName11()
                        EName11()
                        def CINFO11():
                            global CINFO10
                            CINFO=input('Enter new contact info :')
                            if CINFO.isnumeric()==True and len(CINFO)==10:
                                pass
                            else:
                                print('Invalid Input')
                                CINFO11()
                        CINFO11()
                        sql='update employee set CONTACT_INFO=%s where EID=%S or EName=%s'
                        param=(int(CINFO),int(EID),EName)
                        try:
                            cur.execute(sql,param)
                            con.commit()
                            print('Updated Successfully')
                        except:
                            con.rollback()
                            print('Updation Failed')
                        leo=input('Do you want to continue modifying record?[y/n] :')
                        if leo=='y':
                            cicc()

                        else:
                            mod3()
                    cicc()

                            
                        
                elif rello=='2':
                    print('Taking you back to Employee Menu')
                    employee()
                else:
                    print('Invalid input')
                    mod3()
            else:
                print('Invalid input')
                mod3()
        mod3()


    elif d=='5':
        def del3():
            print('This is deletion of record section of Employee Management')
            def EID12(): 
                global EID
                EID=input('Enter Employee ID:')
                if EID.isnumeric()==True and len(EID)<5:
                    pass
                else:
                    print('Invalid Input')
                    EID12()
            EID12()
            def Name12():
                global Name
                Name=input("Enter Employee Name:")
                if Name.isalpha()==True and len(Name)<30:
                    pass
                else:
                    print('Invalid Input')
                    Name12()
            Name12()
            sql='delete from employee where EID=%s or EName=%s'
            recs=(int(EID),Name)
            try:
                cur.execute(sql,recs)
                con.commit()
                print('Deletion Success')
            except:
                con.rollback()
                print('Deletion failed')
            indu=input('Do you want to continue with deletion of records?[y/n] :')
            if indu=='y':
                del3()
            else:
                employee()

        del3()

    elif d=='6':
        print('Taking you back to Main Menu. . . . .')
        main()

    else:
        print('Invalid input, try again')
        employee()


#-------------------------------Room----------------------------------------
def room():
    print()
    print('This is Room Management')
    e=input("""Enter your choice from following options
                1. Show all records
                2. Show specific record
                3. Add Record
                4. Modify Record
                5. Delete Record
                6. Back to Main Menu
                :""")
    if e.isnumeric()==True:
        choice4(e)
    else:
        print('Invalid input, Try again')
        room()

def choice4(e):
    if e=='1':
        print('This is show all record section of Room Management')
        print('Showing all records of Room table. . . .')
        cur.execute('select * from room')
        data=cur.fetchall()
        print("(RID),(BEDS),(AVAILIBILITY),(CHARGE),(TYPE)")
        print('')
        for i in data:
            print(i)
        elo=input('Do you want to go back?[y/n] :')
        if elo=='y':
            room()
        else:
            exitt()
    elif e=='2':
        def roog():
            print('This is show specific record section of Room Management')
            def RID13():
                global RID
                RID=input('Enter Room ID:')
                if RID.isnumeric()==True and len(RID)<5:
                    pass
                else:
                    print('Invalid Input')
                    RID13()
            RID13()
            sql='select *from room where RID=%s'%(int(RID),)
            cur.execute(sql)
            data=cur.fetchall()
            print("(RID),(BEDS),(AVAILIBILITY),(CHARGE),(TYPE)")
            print('')
            for i in data:
                print(i)
            ro=input('Do you want to try again?[y/n] :')
            if ro=='y':
                roog()
            else:
                room()
        roog()

    elif e=='3':
        def addd():
            print('This is addition of record  section of Room Management')
            def rid14():
                global rid
                rid=input('Enter room ID:')
                if rid.isnumeric()==True and len(rid)<5:
                    pass
                else:
                    print('Invalid Input')
                    rid14()
            rid14()
            def beds14():
                global beds
                beds=input('Enter number of beds:')
                if beds.isnumeric()==True and len(beds)<11:
                    pass
                else:
                    print('Invalid Input')
                    beds14()
            beds14()
            def availability14(): 
                global availability
                availability=input('Enter availability status[yes/no] :')
                if availability.isalpha()==True and len(availability)<4 and (availability=='yes' or availability=='no'):
                    pass
                else:
                    print('Invalid Input')
                    availability14()
            availability14()
            def charge14(): 
                global charge
                charge=input('Enter Room charges:')
                if charge.isnumeric()==True and len(charge)<5 and int(charge)<5000:
                    pass
                else:
                    print('Invalid Input')
                    charge14()
            charge14()
            def Type14():
                global Type
                Type=input('Enter room type[AC/Non-AC]:')
                if Type.isalpha()==True and (Type=='AC' or Type=='Non-AC'):
                    pass
                else:
                    print('Invalid Input')
                    Type14()
            Type14()
            sql='insert into room(rid,beds,availability,charge,Type) values(%s,%s,%s,%s,%s)'
            recs=(int(rid),int(beds),availability,int(charge),Type)
            
            try:
                cur.execute(sql,recs)
                con.commit()
                print('Insertion Successful')
            except:
                con.rollback()
                print('Insertion Failed')
            weu=input('Do you want to try again?[y/n] :')
            if weu=='y':
                addd()
            else:
                print('Taking you back to Room menu')
                room()
            
        addd()

    elif e=='4':
        def mod4():
            print('This is modification section of Room Management')
            reel=input("""Enter your choice from following options
                            1. Availibility
                            2. No. of beds
                            3. Go back to Room Menu
                            : """)
            if reel.isnumeric()==True:
                if reel=='1':
                    def avm():
                        print('You chose to change availibility status')
                        def RID15():
                            global RID
                            RID=input('Enter Room ID:')
                            if RID.isnumeric()==True and len(RID)<5:
                                pass
                            else:
                                print('Invalid Input')
                                RID15()
                        RID15()
                        def AVAIL15(): 
                            global AVAIL
                            AVAIL=input('Enter availability status [yes/no]:')
                            if AVAIL.isalpha()==True and (AVAIL=='yes' or AVAIL=='no'):
                                pass
                            else:
                                print('Invalid Input')
                                AVAIL15()
                        AVAIL15()
                        mysqll='update ROOM set Availability=%s where RID=%s'
                        param=(AVAIL,int(RID))
                        try:
                            cur.execute(mysqll,param)
                            con.commit()
                            print('Updated Successfully')
                        except:
                            con.rollback()
                            print('Updation Failed')
                        ro=input('Enter do you want to continue with availibility status modification?[y/n] :')
                        if ro=='y':
                            avm()
                        else:
                            mod4()
                        
                    avm()

                elif reel=='2':
                    def nbm():
                        print('You chose to change No. of beds')
                        def RID16():
                            global RID
                            RID=input('Enter Room ID:')
                            if RID.isnumeric()==True and len(RID)<5:
                                pass
                            else:
                                print('Invalid Input')
                                RID16()
                        RID16()
                        def NBED16():
                            global NBED
                            NBED=input('Enter no. of beds:')
                            if NBED.isnumeric()==True and len(NBED)<11:
                                pass
                            else:
                                print('Invalid Input')
                                NBED16()
                        NBED16()
                        mysqll='update ROOM set BEDS=%s where RID=%s'
                        param=(int(NBED),int(RID))
                        try:
                            cur.execute(mysqll,param)
                            con.commit()
                            print('Updated Successfully')
                        except:
                            con.rollback()
                            print('Updation Failed')
                        rebo=input('Do you want to continue with  No. of beds modification?[y/n] :')
                        if rebo=='y':
                            nbm()
                        else:
                            mod4()
                        
                    nbm()
        mod4()

    elif e=='5':
        def del4():
            print('This is delete record section of Room Management')
            def rid17(): 
                global rid
                rid=input('Enter Room ID:')
                if rid.isnumeric()==True and len(rid)<5:
                    pass
                else:
                    print('Invalid Input')
                    rid17()
            rid17()
            sql='delete from room where rid=%s'%(int(rid),)
            try:
                cur.execute(sql)
                con.commit()
                print('Deletion Success')
            except:
                con.rollback()
                print('Deletion Failed')
            reo=input('Do you want to continue with deletion of records?[y/n] :')
            if reo=='y':
                del4()
            else:
                room()
            
        del4()

    elif e=='6':
        print('Taking you back to Main Menu. . . . ')
        main()
    else:
        print('Invalid input, Try again')
        room()


#--------------------------Services-----------------------
def services():
    print()
    print('This is Services Management')
    f=input("""Enter your choice from the following options
                1. Show all record
                2. Show specific record
                3. Add record
                4. Modify Record
                5. Delete Record
                6. Back to main menu
                : """)
    if f.isnumeric()==True:
        choice5(f)
    else:
        print('Invalid input, Try again')
        services()

def choice5(f):
    if f=='1':
        print('This is show all record section of Services Management')
        print('Showing all records of room table. . . .')
        cur.execute('select * from service')
        data=cur.fetchall()
        print("(SID),(SNAME),(CHARGE)")
        print('')
        for i in data:
            print(i)
        eq=input('Do you want to go back?[y/n] :')
        if eq=='y':
            services()
        else:
            exitt()
    elif f=='2':
        def sss():
            print('This is show specific record section of Services Management')
            def sid18(): 
                global sid
                sid=input('Enter Service ID:')
                if sid.isnumeric()==True and len(sid)<5:
                    pass
                else:
                    print('Invalid Input')
                    sid18()
            sid18()
            def sname18():
                global sname
                sname=input('Enter Service Name:')
                if sname.isalpha()==True and len(sname)<15:
                    pass
                else:
                    print('Invalid Input')
                    sname18()
            sname18()
            sql='select * from service where sid=%s or sname=%s'
            param=(int(sid),sname)
            cur.execute(sql,param)
            data=cur.fetchall()
            print("(SID),(SNAME),(CHARGE)")
            print('')
            for i in data:
                print(i)
            op=input('Do you want to try again?[y/n] :')
            if op=='y':
                sss()
            else:
                services()
        sss()

    elif f=='3':
        def ador():
            print('This is addition of record section of Services Management')
            def sid19(): 
                global sid
                sid=input('enter the service id:')
                if sid.isnumeric()==True and len(sid)<5:
                    pass
                else:
                    print('Invalid Input')
                    sid19()
            sid19()
            def sname19():
                global sname
                sname=input('enter the service name:')
                if sname.isalpha()==True and len(sname)<30:
                    pass
                else:
                    print('Invalid Input')
                    sname19()
            sname19()
            def charge19():
                global charge
                charge=input('enter the charge:')
                if charge.isnumeric()==True and len(charge)<5 and int(charge)<7000:
                    pass
                else:
                    print('Invalid Input')
                    charge19()
            charge19()
            sql='insert into service(sid,s_name,charge) values(%s,%s,%s)'
            recs=(int(sid),sname,int(charge))
            try:
                cur.execute(sql,recs)
                con.commit()
                print('inserted successfully')
            except:
                con.rollback()
                print('insertion failed')
            rog=input('Do you want to add more records?[y/n]:')
            if rog=='y':
                ador()
            else:
                services()
        ador()

    elif f=='4':
        def mod5():
            print('This is modification section of Services Management')
            relo=input("""Enter your choice from following options
                            1. Charge
                            2. Go back to Service Menu
                            :""")
            if relo.isnumeric()==True:
                if relo=='1':
                    def cc():
                        print('You chose to change charge for a specific service')
                        def SID20():
                            global SID
                            SID=input('Enter Service ID:')
                            if SID.isnumeric()==True and len(SID)<5:
                                pass
                            else:
                                print('Invalid Input')
                                SID20()
                        SID20()
                        def S_name20():
                            global S_name
                            S_name=input('Enter Service Name:')
                            if S_name.isalpha()==True and len(S_name)<30:
                                pass
                            else:
                                print('Invalid Input')
                                S_name20()
                        S_name20()
                        def Charge20():
                            global Charge
                            Charge=input('Enter new charges:')
                            if Charge.isnumeric()==True and len(Charge)<5 and int(Charge)<7000:
                                pass
                            else:
                                print('Invalid Input')
                                Charge20()
                        Charge20()
                        sql='update Service set Charge=%s where SID=%s or s_name=%s'
                        param=(int(Charge),int(SID),S_name)
                        try:
                            cur.execute(sql,param)
                            con.commit()
                            print('Updation Success')
                        except:
                            con.rollback()
                            print('updation failed')
                        ew=input("Do you want to continue with charge modification?[y/n] :")
                        if ew=='y':
                                cc()
                        else:
                                mod5()
                    cc()
                elif relo=='2':
                    print('Taking back to Service Menu')
                    services()
                    
                else:
                    print('Invalid input, Try again')
                    mod5()

            else:
                print('Invalid Input, Try again')
                mod5()
        mod5()

    elif f=='5':
        def del5():
            print('This is delete record section of Services management')
            def sid21(): 
                global sid
                sid=input('Enter Service ID:')
                if sid.isnumeric()==True and len(sid)<5:
                    pass
                else:
                    print('Invalid Input')
                    sid21()
            sid21()
            def s_name21():
                global s_name
                s_name=input('Enter Service Name:')
                if s_name.isalpha()==True and len(s_name)<30:
                    pass
                else:
                    print('Invalid Input')
                    s_name21()
            s_name21()
            sql='delete from service where sid=%s or sname=%s'
            param=(int(sid),s_name)
            try:
                cur.execute(sql,param)
                con.commit()
                print('Deletion Success')
            except:
                con.rollback()
                print('Deletion Failed')
            qnoy=input("Do you want to continue with deletion of records?[y/n] :")
            if qnoy=='y':
                del5()
            else:
                services()            
        del5()

    elif f=='6':
        print('Taking you back to Main Menu. . . ')
        main()
    else:
        print('Invalid input, Try again')
        services()


#----------------------------------Pharmacy-----------------------------
def pharmacy():
    print()
    print('This is Pharmacy management')
    g=input("""Enter you choice from the following options
                1. Show all record
                2. Show specific record
                3. Add record
                4. Modify record
                5. Delete record
                6. Back to Main Menu
                :""")
    if g.isnumeric()==True:
        choice6(g)
    else:
        print('Invalid input, Try again')
        pharmacy()

def choice6(g):
    if g=='1':
        print('This is show all record section of Pharmacy management')
        print('Showing all records of Pharmacy table. . . ')
        print('(MED_ID),(MED_NAME),(QUANTITY),(RATE)')
        cur.execute("Select * from pharmacy")
        data=cur.fetchall()
        for i in data:
            print(i)
        elo=input('Do you want to travel back?[y/n]:')
        if elo=='y':
            pharmacy()
        else:
            exitt()
    elif g=='2':
          def shs1():
              print('This is show specific record section of Pharmacy Management')
              def med_id22(): 
                  global med_id
                  med_id=input('Enter the medicine id:')
                  if med_id.isnumeric()==True and len(med_id)<5:
                      pass
                  else:
                      print('Invalid Input')
                      med_id22()
              med_id22()
              def med_name22():
                  global med_name
                  med_name=input('Enter Medicine Name:')
                  if med_name.isalpha()==True and len(med_name)<30:
                      pass
                  else:
                      print('Invalid Input')
                      med_name22()
              med_name22()
              print('(MED_ID),(MED_NAME),(QUANTITY),(RATE)')
              sql='select * from pharmacy where med_id=%s or med_name=%s'
              param=(int(med_id), med_name)
              cur.execute(sql,param)
              data=cur.fetchall()
              for i in data:
                  print(i)
              op=input('Do you want to try again?[y/n] :')
              if op=='y':
                    shs1()
              else:
                    
                    pharmacy()
             
          shs1()

    elif g=='3':
        def adorr():
            print('This is addition of record section of Pharmacy Management')
            def med_id23():
                global med_id
                med_id=input('enter the medicine id:')
                if med_id.isnumeric()==True and len(med_id)<5:
                    pass
                else:
                    print('Invalid Input')
                    med_id23()
            med_id23()
            def med_name23():
                global med_name
                med_name=input('enter the medicine name:')
                if med_name.isalpha()==True and len(med_name)<30:
                    pass
                else:
                    print('Invalid Input')
                    med_name23()
            med_name23()
            def quantity23(): 
                global quantity
                quantity=input('enter the quantity of medicine:')
                if quantity.isnumeric()==True and int(quantity)<500:
                    pass
                else:
                    print('Invalid Input')
                    quantity23()
            quantity23()
            def rate23():
                global rate
                rate=input('enter the rate of medicine:')
                if rate.isnumeric()==True and len(rate)<5 and int(rate)<2000:
                    pass
                else:
                    print('Invalid Input')
                    rate23()
            rate23()
            sql='insert into pharmacy(med_id,med_name,quantity,rate) values(%s,%s,%s,%s)'
            recs=(int(med_id),med_name,int(quantity),int(rate))
            try:
                cur.execute(sql,recs)
                con.commit()
                print('inserted successfully')
            except:
                con.rollback()
                print('insertion failed')
            dep=input('Do you want to add more records?[y/n]:')
            if dep=='y':
                adorr()
            else:
                pharmacy()
        adorr()

    elif g=='4':
        def mod6():
            print('This is modification sectior of Pharmacy Management')
            rt=input("""Enter your choice from following options
                        1. Quantity of medicine
                        2. Back to Pharmacy Menu
                        :""")
            if rt.isnumeric()==True:
                if rt=='1':
                    def qm():
                        print('You chose to change Medicine Quantity')
                        def med_id24(): 
                            global med_id
                            med_id=input('Enter med ID:')
                            if med_id.isnumeric()==True and len(med_id)<5:
                                pass
                            else:
                                print('Invalid Input')
                                med_id24()
                        med_id()
                        def med_name24():
                            global med_name
                            med_name= input('Enter med Name:')
                            if med_name.isalpha()==True and len(med_name)<30:
                                pass
                            else:
                                print('Invalid Input')
                                med_name24()
                        med_name24()
                        def Qty24():
                            global Qty
                            Qty=input('Enter quantity')
                            if Qty.isnumeric()==True and len(Qty)<5 and int(Qty)<500:
                                pass
                            else:
                                print('Invalid Input')
                                Qty24()
                        Qty24()
                        sql='update Pharmacy set QUANTITY=%s where med_id=%s or med_name=%s'
                        param=(int(Qty),int(med_id),med_name)
                        try:
                            cur.execute(sql,param)
                            con.commit()
                            print('Updation Success')
                        except:
                            con.rollback()
                            print('Updation Failed')
                        ann=input('Do you want to continue with quantity updation?[y/n] :')
                        if ann=='y':
                            qm()
                        else:
                            mod6()
                    qm()

                elif rt=='2':
                    print('Taking you back to Pharmacy Menu. . . ')
                    pharmacy()

                else:
                    print('Invalid input, Re-try')
                    mod6()
            else:
                print('Invalid input, Re-try')
                mod6()
        mod6()

    elif g=='5':
        def del6():
            print('This is delete record section of Pharmacy management')
            def med_id25(): 
                global med_id
                med_id=input('Enter med ID:')
                if med_id.isnumeric==True and len(med_id)<5:
                    pass
                else:
                    print('Invalid Input')
                    med_id25()
            med_id25()
            def med_name25(): 
                global med_name
                med_name=input('Enter med Name:')
                if med_name.isalpha()==True and len(med_name)<30:
                    pass
                else:
                    print('Invalid Input')
                    med_name25()
            med_name25()
            sql='delete from Pharmacy where med_id=%s or med_name=%s'
            param=(int(med_id),med_name)
            try:
                cur.execute(sql,param)
                con.commit()
                print('Deletion Success')
            except:
                con.rollback()
                print('Deletion Failed')
            roy=input('Do you want to continue with deletion of records?[y/n] :')
            if roy=='y':
                del6()
            else:
                pharmacy()
            
        del6()


    elif g=='6':
        print('Taking you back to Main menu. . .')
        main()

    else:
        print('Invalid input, Try again')
        pharmacy()

#-----------------------------Billing----------------------------------
def billing():
    global roomcharge
    global doccharge
    global patientname
    global servicecharge
    print('This is billing section of Hospital Management System')
    def pidd():
        global ID
        ID=input('Enter Patient ID:')
        if ID.isnumeric()==True and len(ID)<5:
            pass
        else:
            pidd()
    pidd()
    
    
    def didd():
        global DID
        DID=input('Enter Doctor ID:')
        if DID.isnumeric()==True and len(DID)<5:
            pass
        else:
            didd()
    didd()
    sql2='select charge from doctor where DID=%s'
    paramm=(int(DID),)
    cur.execute(sql2,paramm)
    data=cur.fetchall()
    for i in data:
        doccharge=i
    
    def ridd():
        global RID
        RID=input('Enter Room ID:')
        if RID.isnumeric()==True and len(RID)<5:
            pass
        else:
            ridd()
    ridd()
    sql3='select charge from room where rid=%s'
    parammm=(int(RID),)
    cur.execute(sql3,parammm)
    data=cur.fetchall()
    for i in data:
        roomcharge=i
    
    def sidd():
        global SID
        SID=input('Enter Service ID:')
        if SID.isnumeric()==True and len(SID)<5:
            pass
        else:
            sidd()
    sidd()
    sql3='select charge from service where sid=%s'
    parammm=(int(SID),)
    cur.execute(sql3,parammm)
    data=cur.fetchall()
    for i in data:
        servicecharge=i
        
    
    sqll='select pname from patient where pid=%s'
    param=(int(ID),)
    cur.execute(sqll,param)
    data=cur.fetchall()
    for i in data:
        patientname=i
    
    
    s="select doa from patient where pid=%s"
    param=(int(ID),)
    cur.execute(s,param)
    data=cur.fetchall()
    t=str(date.today()).split('-')
    t=date(int(t[0]),int(t[1]),int(t[2]))
    for row in data:
        doa=row[0]
        doa=str(doa)
        doa=(doa.split('-'))
        doa=date(int(doa[0]),int(doa[1]),int(doa[2]))
        dd=(t-doa).days

    print('')
    billing=doccharge[0]+dd*roomcharge[0]+servicecharge[0]
    print('Overall bill for',patientname,'is',billing,'Rupees')
    
    bill=input('Enter do you want to continue with Billing?[yes/no] :')
    if bill=='yes':
        billing()
    else:
        print('Taking you back to main menu')
        print('')
        main()
    
    

def exitt():
    print("""Thank you for using our HOSPITAL MANAGEMENT PROGRAM.
Group memebers:- Prashant, Lakshay, Aditya""")                   
  

def main():
    print('_________________________________________________________')
    print()
    print(           'WELCOME TO HOSPITAL MANAGEMENT SYSTEM'         )
    print('_________________________________________________________')
    print()

    print("""Select from the following options
            1. To manage Patients
            2. To manage Doctors
            3. To manage Employees
            4. To manage Rooms
            5. To manage Services
            6. To manage Pharmacy
            7. Billing
            8. Exit """)
    global a
    a=input('Enter you choice:')
    if a.isnumeric()==True:
        choices(a)
    else:
        print('Invalid Input, Try again')
        main()

def choices(a):
    if a=='1':
        patient()
    elif a=='2':
        doctor()
    elif a=='3':
        employee()
    elif a=='4':
        room()
    elif a=='5':
        services()
    elif a=='6':
        pharmacy()
    elif a=='7':
        billing()
    elif a=='8':
        exitt()
    else:
        print('Enter valid input')
        main()


#---------------MENU---------------
main()


        
        

        
