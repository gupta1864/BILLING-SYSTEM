from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import messagebox
import random,os,tempfile,smtplib 


#login function    
def Insert():
    user_id = entry_user_id.get()
    password = entry_password.get()
    if(user_id == "" or password == "" ):
        messagebox.showinfo("ALERT", "Please enter all fields")
    else:
        con= mysql.connector.connect(host="localhost",user="root",password="Abc@1234",database="billingsoftware")
        cursor = con.cursor()
        cursor.execute("insert into login values('" + user_id +"', '"+ password +"')")
        cursor.execute("commit")
        messagebox.showinfo("Status", "Successfully Inserted")
        con.close()
def login():
   user_id = entry_user_id.get()
   password = entry_password.get()
   try:
         conn = mysql.connector.connect(host="localhost",user="root",password="Abc@1234",database="billingsoftware")
         cursor = conn.cursor()
         # Execute query
         cursor.execute("SELECT * FROM login WHERE user_id=%s AND password=%s", (user_id, password))
         row = cursor.fetchone()
         if row:       
             root.destroy()
             open_root()
         else:
             messagebox.showerror("Login failed", "Invalid username or password So insert new username and password.")
         # Close cursor and connection
         cursor.close()
         conn.close()
 
   except mysql.connector.Error as err:
         messagebox.showerror("Error", "Error connecting to database: {}".format(err))
 #creating software window       
def open_root():
    if not os.path.exists('bills'):
     os.mkdir('bills')
     # Functionalty of Print Button 
    def print_bill():
      if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
      else:
       file=tempfile.mktemp('.txt')
       open(file,'w').write(textarea.get(1.0,END))
       os.startfile(file,'print')
    
   ##################################################
    def save_bill():
      
      result = messagebox.askyesno('Confirm','Do you want to save the bill' )
      if result:
         content = textarea.get("1.0", END)  # Retrieve content from the text area
         try:
            with open(f"bills/{phoneEntry.get()}.txt", "w") as file:
               file.write(content)
            messagebox.showinfo("Success", "Content saved successfully!")
         except Exception as e:
            messagebox.showerror("Error", f"Failed to save content: {str(e)}")
      
    billnumber=random.randint(500,1000)
    #########################################################
    def total():
        global soapprice,facecreameprice,facewashprince,hairsprayprice,hairgelprice,bodylotionprice
        global nailpaintprice,Moisturizerprice,totalcosmeticprice,cosmeticstax,handcreameprice
        soapprice=int(bathsoapEntry.get())*int(price_bath_soap.get())
        total_bath_soap.delete(0,END)
        total_bath_soap.insert(0,soapprice)

        facecreameprice=int(facecreamEntry.get())*int(price_face_cream.get())
        total_face_cream.delete(0,END)
        total_face_cream.insert(0,facecreameprice)
        facewashprince=int(faceWashEntry.get())*int(price_face_wash.get())
        total_face_wash.delete(0,END)
        total_face_wash.insert(0,facewashprince)
        hairsprayprice=int(hairSprayEntry.get())*int(price_hair_sparay.get())
        total_hair_spray.delete(0,END)
        total_hair_spray.insert(0,hairsprayprice)
        hairgelprice=int(hairGelEntry.get())*int(price_hair_gel.get())
        total_hair_gel.delete(0,END)
        total_hair_gel.insert(0,hairgelprice)
        bodylotionprice=int(BodyLotionEntry.get())*int(price_body_lotion.get())
        total_body_lotion.delete(0,END)
        total_body_lotion.insert(0,bodylotionprice)
        handcreameprice=int(HandCreamEntry.get())*int(price_hand_cream.get())
        total_hand_cream.delete(0,END)
        total_hand_cream.insert(0,handcreameprice)
        nailpaintprice=int(NailpaintEntry.get())*int(price_nail_paint.get())
        total_nail_paint.delete(0,END)
        total_nail_paint.insert(0,nailpaintprice)
        Moisturizerprice=int(MoisturizerEntry.get())*int(price_moisturizer.get())
        total_moisturizer.delete(0,END)
        total_moisturizer.insert(0,Moisturizerprice)

        totalcosmeticprice=soapprice+facecreameprice+facewashprince+hairsprayprice+hairgelprice+bodylotionprice+handcreameprice+nailpaintprice+Moisturizerprice
        cosmeticspriceEntry.delete(0,END)
        cosmeticspriceEntry.insert(0,totalcosmeticprice)
        cosmetics_tax_Entry.delete(0,END)
        cosmeticstax=int(totalcosmeticprice*0.12)
        cosmetics_tax_Entry.insert(0,cosmeticstax)
         ############
        global riceprice,Oilprice,Daalprice,Wheatprice,Sugarprice,Teaprice,TomatoSauce,Butterprice,Milkprice,totalgroceryprice,grocerytax
        riceprice=int(RiceEntry.get())*int(price_rice.get())
        total_rice.delete(0,END)
        total_rice.insert(0,riceprice)
        Oilprice=int(OilEntry.get())*int(price_oil.get())
        total_oil.delete(0,END)
        total_oil.insert(0,Oilprice)
        Daalprice=int(DaalEntry.get())*int(price_daal.get())
        total_daal.delete(0,END)
        total_daal.insert(0,Daalprice)
        Wheatprice=int(WheatEntry.get())*int(price_wheat.get())
        total_wheat.delete(0,END)
        total_wheat.insert(0,Wheatprice)
        Sugarprice=int(SugarEntry.get())*int(price_sugar.get())
        total_sugar.delete(0,END)
        total_sugar.insert(0,Sugarprice)
        Teaprice=int(TeaEntry.get())*int(price_tea.get())
        total_tea.delete(0,END)
        total_tea.insert(0,Teaprice)
        TomatoSauce=int(Tomato_Sauce_Entry.get())*int(price_tomato_sauce.get())
        total_tomato_sauce.delete(0,END)
        total_tomato_sauce.insert(0,TomatoSauce)
        Butterprice=int(Butter_Entry.get())*int(price_butter.get())
        total_butter.delete(0,END)
        total_butter.insert(0,Butterprice)
        Milkprice=int(Milk_Entry.get())*int(price_milk.get())
        total_milk.delete(0,END)
        total_milk.insert(0,Milkprice)

        #total of all grocery price 
        totalgroceryprice=riceprice+Oilprice+Daalprice+Wheatprice+Sugarprice+Teaprice+TomatoSauce+Butterprice+Milkprice
        GrocerypriceEntry.delete(0,END)
        GrocerypriceEntry.insert(0,totalgroceryprice)

        # calculation of Grocery tax block
        Grocery_tax_Entry.delete(0,END)
        grocerytax=int(totalgroceryprice*0.05)
        Grocery_tax_Entry.insert(0,grocerytax)
        #cold drink calacuation price
        global Cocacolaprice,Frootiprice, Dewprice,Spriteprice,PepsiPrice,Mazzaprice,Mountaindewprice,Appleprice,Limca,totalcoldprice,colddrinktax
        Cocacolaprice=int(Coca_colaEntry.get())*int(price_coca_cola.get())
        total_coca_cola.delete(0,END)
        total_coca_cola.insert(0,Cocacolaprice)
        Frootiprice=int(FrootiEntry.get())*int(price_frooti.get())
        total_frooti.delete(0,END)
        total_frooti.insert(0,Frootiprice)
        Dewprice=int(DewEntry.get())*int(price_dew.get())
        total_dew.delete(0,END)
        total_dew.insert(0,Dewprice)
        Spriteprice=int(SpriteEntry.get())*int(price_sprite.get())
        total_sprite.delete(0,END)
        total_sprite.insert(0,Spriteprice)
        PepsiPrice=int(PepsiEntry.get())*int(price_pepsi.get())
        total_pepsi.delete(0,END)
        total_pepsi.insert(0,PepsiPrice)
        Mazzaprice=int(MaazaEntry.get())*int(price_maazza.get())
        total_maaza.delete(0,END)
        total_maaza.insert(0,Mazzaprice)
        Mountaindewprice=int(Mountain_DewEntry.get())*int(price_mountain_dew.get())
        total_mountain_dew.delete(0,END)
        total_mountain_dew.insert(0,Mountaindewprice)
        Appleprice=int(Apple_fizz_Entry.get())*int(price_apple_fizz_label.get())
        total_apple_fizz.delete(0,END)
        total_apple_fizz.insert(0,Appleprice)
        Limca=int(Limca_Entry.get())*int(price_limca.get())
        total_limca.delete(0,END)
        total_limca.insert(0,Limca)

        totalcoldprice=Cocacolaprice+Frootiprice+Dewprice+Spriteprice+PepsiPrice+Mazzaprice+Mountaindewprice+Appleprice+Limca
        Cold_drink_priceEntry.delete(0,END)
        Cold_drink_priceEntry.insert(0,totalcoldprice)
    
        Cold_drink_TaxEntry.delete(0,END)
        colddrinktax=int(totalcoldprice*0.08)
        Cold_drink_TaxEntry.insert(0,colddrinktax)
        ###################################################################
    def bill_area():
        if nameEntry.get()=='' and phoneEntry.get()=='':
         messagebox.showerror('Error','Customer Detail Are Requird')
        elif cosmeticspriceEntry.get()==''and GrocerypriceEntry.get()=='' and Cold_drink_priceEntry.get()=='':
         messagebox.showerror('Error','No Product is selected')
        elif cosmeticspriceEntry.get()=='0'and GrocerypriceEntry.get()=='0' and Cold_drink_priceEntry.get()=='0':
         messagebox.showerror('Error','No Product is selected')
        else:
         textarea.insert(END,"\t\t**WELCOME CUSTOMER**\n")
         textarea.insert(END,f'\nBill Number:{billnumber}\n')
     #   textarea.delete(1.0,END)
         textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
         textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}\n')
         textarea.insert(END,'\n************************************************\n')
         textarea.insert(END,'Product\t\tPrice\tQuantity\tTotal')
         textarea.insert(END,'\n************************************************')

         if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t{price_bath_soap.get()}\t{bathsoapEntry.get()}\t{soapprice}')
         if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace cream\t\t{price_face_cream.get()}\t{facecreamEntry.get()}\t{facecreameprice}')
         if faceWashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t{price_face_wash.get()}\t{faceWashEntry.get()}\t{facewashprince}')
         if hairGelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t{price_hair_gel.get()}\t{hairGelEntry.get()}\t{hairgelprice}')
         if hairSprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t{price_hair_sparay.get()}\t{hairSprayEntry.get()}\t{hairsprayprice}')
         if  BodyLotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t{price_body_lotion.get()}\t{BodyLotionEntry.get()}\t{bodylotionprice}')
         if HandCreamEntry.get()!='0':
            textarea.insert(END,f'\nHand Cream\t\t{price_hand_cream.get()}\t{HandCreamEntry.get()}\t{handcreameprice}')
         if NailpaintEntry.get()!='0':
            textarea.insert(END,f'\nNail Paint\t\t{price_nail_paint.get()}\t{NailpaintEntry.get()}\t{nailpaintprice}')
         if MoisturizerEntry.get()!='0':
            textarea.insert(END,f'\nMoisturizer\t\t{price_moisturizer.get()}\t{MoisturizerEntry.get()}\t{Moisturizerprice}')

         if RiceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t{price_rice.get()}\t{RiceEntry.get()}\t{riceprice}')
         if OilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t{price_oil.get()}\t{OilEntry.get()}\t{Oilprice}')
         if DaalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t{price_daal.get()}\t{DaalEntry.get()}\t{Daalprice}')
         if WheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t{price_wheat.get()}\t{WheatEntry.get()}\t{Wheatprice}')
         if SugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t{price_sugar.get()}\t{SugarEntry.get()}\t{Sugarprice}')
         if TeaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t{price_tea.get()}\t{TeaEntry.get()}\t{Teaprice}')
         if Tomato_Sauce_Entry.get()!='0':
            textarea.insert(END,f'\nTomato Sauce\t\t{price_tomato_sauce.get()}\t{Tomato_Sauce_Entry.get()}\t{TomatoSauce}')
         if Butter_Entry.get()!='0':
            textarea.insert(END,f'\nButter\t\t{price_butter.get()}\t{Butter_Entry.get()}\t{Butterprice}')
         if Milk_Entry.get()!='0':
            textarea.insert(END,f'\nMilk\t\t{price_milk.get()}\t{Milk_Entry.get()}\t{Milkprice}')
      
         if Coca_colaEntry.get()!='0':
            textarea.insert(END,f'\nCoca cola\t\t{price_coca_cola.get()}\t{Coca_colaEntry.get()}\t{Cocacolaprice}')
         if FrootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t{price_frooti.get()}\t{FrootiEntry.get()}\t{Frootiprice}')  
         if DewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t{price_dew.get()}\t{DewEntry.get()}\t{Dewprice}')
         if SpriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{price_sprite.get()}\t{SpriteEntry.get()}\t{Spriteprice}')   
         if PepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t{price_pepsi.get()}\t{PepsiEntry.get()}\t{PepsiPrice}')       
         if MaazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t{price_maazza.get()}\t{MaazaEntry.get()}\t{Mazzaprice}')
         if Apple_fizz_Entry.get()!='0':
            textarea.insert(END,f'\nApple Fizz\t\t{price_apple_fizz_label.get()}\t{Apple_fizz_Entry.get()}\t{Appleprice}')
         if Limca_Entry.get()!='0':
            textarea.insert(END,f'\nLimca\t\t{price_limca.get()}\t{Limca_Entry.get()}\t{Limca}')
         if  Mountain_DewEntry.get()!='0':
            textarea.insert(END,f'\nMountain Dew\t\t{price_mountain_dew.get()}\t{Mountain_DewEntry.get()}\t{Mountaindewprice}')
         
         textarea.insert(END,'\n***********************************************')
         if cosmetics_tax_Entry.get()!='0' or '':
            textarea.insert(END,f'\n Cosmetic Tax\t\t\t Rs :{cosmetics_tax_Entry.get()}')
         if Grocery_tax_Entry.get()!='0' or '':
            textarea.insert(END,f'\n Grocery Tax\t\t\t Rs :{Grocery_tax_Entry.get()}')
         if Cold_drink_TaxEntry.get()!='0' or '':
            textarea.insert(END,f'\n Cold Drink Tax\t\t\t Rs :{Cold_drink_TaxEntry.get()}')
         total_bill = totalcosmeticprice+totalgroceryprice+totalcoldprice+grocerytax+cosmeticstax+colddrinktax
         textarea.insert(END,f'\n\nTotal Bill\t\t\t\t Rs :{total_bill}')

         textarea.insert(END,'\n***********************************************')
         



      ####################################################################################
    def search_bill():
     for i in  os.listdir('bills/'):
      if i.split('.')[0]==bill_no_Entry.get():
         f=open(f'bills/{i}','r')
         textarea.delete(1.0,END)
         for data in f:
            textarea.insert(END,data)
         f.close()   
         break

      else:
        messagebox.showinfo('Sucess','Valid Phone No')
    if not os.path.exists('bills'):
      os.mkdir('bills')    
########################################################################################################
    def send_email():
      def send_gmail():
         try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),PasswordEntry.get())
            message=messagebox.get(1.0,END)
               
            ob.sendmail(senderEntry.get(),recivierEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Sucess','Bill is sucessfully sent',parent=root1)
         except:
            messagebox.showerror('Error','Something went wrong,Please try again',parent=root1)   
      if textarea.get(1.0,END)=='\n':
         messagebox.showerror('Error','Bill is empty')
      else:
         root1=Tk()
         root1.title('Send Email')
         root1.config(bg='#8A360F')
         
         senderFrame=LabelFrame(root1,text='SENDER',font=('times new roman',25,'bold'))
         senderFrame.grid(row=0,column=0,pady=10,padx=10)
         
         gmailLabel=Label(senderFrame,text="Sender's Email",font=('times new roman',15,'bold'))
         gmailLabel.grid(row=0,column=0,padx=10,pady=10)
         
         senderEntry=Entry(senderFrame,font=('arial',15),bd=7,width=18,relief=RIDGE)
         senderEntry.grid(row=0,column=1,padx=10,pady=10)
         
         passwordLabel=Label(senderFrame,text="Password",font=('times new roman',15,'bold'))
         passwordLabel.grid(row=1,column=0,padx=10,pady=10)
         
         PasswordEntry=Entry(senderFrame,font=('arial',15),bd=7,width=18,relief=RIDGE,show='*')
         PasswordEntry.grid(row=1,column=1,padx=10,pady=10)
         
         recivierFrame=LabelFrame(root1,text='RECIPIENT',font=('times new roman',25,'bold'))
         recivierFrame.grid(row=1,column=0,padx=10,pady=10)

         recivierLabel=Label(recivierFrame,text='Email Address',font=('times new roman',15,'bold'))
         recivierLabel.grid(row=0,column=0,padx=10,pady=10)
         
         recivierEntry=Entry(recivierFrame,font=('arial',15),bd=7,width=18,relief=RIDGE)
         recivierEntry.grid(row=0,column=1,padx=10,pady=10)
         
         messaeELabel=Label(recivierFrame,text="Message",font=('times new roman',15,'bold'))
         messaeELabel.grid(row=1,column=0,padx=10,pady=10)

         messagebox=Text(recivierFrame,height=28,width=70)
         messagebox.grid(row=2,column=0,columnspan=2)
         messagebox.delete(1.0,END)
         messagebox.insert(END,textarea.get(1.0,END))

         sendButton=Button(root1,text='SEND',font=('times new roman',15,'bold'),command=send_gmail)
         sendButton.grid(row=2,column=0,pady=20)

    def clear():
      bathsoapEntry.delete(0,END)
      facecreamEntry.delete(0,END)
      faceWashEntry.delete(0,END)
      hairSprayEntry.delete(0,END)
      hairGelEntry.delete(0,END)
      BodyLotionEntry.delete(0,END)
      HandCreamEntry.delete(0,END)
      NailpaintEntry.delete(0,END)
      MoisturizerEntry.delete(0,END)

      RiceEntry.delete(0,END)
      OilEntry.delete(0,END)
      DaalEntry.delete(0,END)
      WheatEntry.delete(0,END)
      SugarEntry.delete(0,END)
      TeaEntry.delete(0,END)
      Tomato_Sauce_Entry.delete(0,END)
      Butter_Entry.delete(0,END)
      Milk_Entry.delete(0,END)

      Coca_colaEntry.delete(0,END)
      FrootiEntry.delete(0,END)
      DewEntry.delete(0,END)
      SpriteEntry.delete(0,END)
      PepsiEntry.delete(0,END)
      MaazaEntry.delete(0,END)
      Mountain_DewEntry.delete(0,END)
      Apple_fizz_Entry.delete(0,END)
      Limca_Entry.delete(0,END)

      bathsoapEntry.insert(0,0)
      facecreamEntry.insert(0,0)
      faceWashEntry.insert(0,0)
      hairSprayEntry.insert(0,0)
      hairGelEntry.insert(0,0)
      BodyLotionEntry.insert(0,0)
      HandCreamEntry.insert(0,0)
      NailpaintEntry.insert(0,0)
      MoisturizerEntry.insert(0,0)

      RiceEntry.insert(0,0)
      OilEntry.insert(0,0)
      DaalEntry.insert(0,0)
      WheatEntry.insert(0,0)
      SugarEntry.insert(0,0)
      TeaEntry.insert(0,0)
      Tomato_Sauce_Entry.insert(0,0)
      Butter_Entry.insert(0,0)
      Milk_Entry.insert(0,0)

      Coca_colaEntry.insert(0,0)
      FrootiEntry.insert(0,0)
      DewEntry.insert(0,0)
      SpriteEntry.insert(0,0)
      PepsiEntry.insert(0,0)
      MaazaEntry.insert(0,0)
      Mountain_DewEntry.insert(0,0)
      Apple_fizz_Entry.insert(0,0)
      Limca_Entry.insert(0,0)
      
      nameEntry.delete(0,END)
      phoneEntry.delete(0,END)
      
      cosmeticspriceEntry.delete(0,END)
      GrocerypriceEntry.delete(0,END)
      Cold_drink_priceEntry.delete(0,END)
      
      cosmetics_tax_Entry.delete(0,END)
      Grocery_tax_Entry.delete(0,END)
      Cold_drink_TaxEntry.delete(0,END)
      textarea.delete(1.0,END)

      total_bath_soap.delete(0,END)
      total_face_cream.delete(0,END)
      total_face_wash.delete(0,END)
      total_hair_gel.delete(0,END)
      total_hair_spray.delete(0,END)
      total_body_lotion.delete(0,END)
      total_hand_cream.delete(0,END)
      total_nail_paint.delete(0,END)
      total_moisturizer.delete(0,END)
      total_rice.delete(0,END)
      total_oil.delete(0,END)
      total_daal.delete(0,END)
      total_wheat.delete(0,END)
      total_sugar.delete(0,END)
      total_tea.delete(0,END)
      total_tomato_sauce.delete(0,END)
      total_butter.delete(0,END)
      total_milk.delete(0,END)
      total_coca_cola.delete(0,END)
      total_frooti.delete(0,END)
      total_dew.delete(0,END)
      total_sprite.delete(0,END)
      total_pepsi.delete(0,END)
      total_maaza.delete(0,END)
      total_mountain_dew.delete(0,END)
      total_apple_fizz.delete(0,END)
      total_limca.delete(0,END)


#######################################################################################################    
    root =Tk()
    global vars
# Title of the window 
    root.title("Retail Billing System Made by Abhishek Gupta")
    # Geomery means Size of window
    root.geometry("1920x1200")
    #given particular icon of our window tab
    root.iconbitmap('icon.ico')
    # Main Heading of the Window 
    headingLabel= Label(root,text ="Retail Billing System",font=('times new roman',25,'bold'),bg='#8A360F',fg='gold',bd=10,relief=GROOVE)
    headingLabel.pack(fill=X,pady=5)
    # Making first Label frame for customer detail
    customer_detail_frame=LabelFrame(root,text="Customer Details",font=('times new roman',12,'bold'),fg='gold',bd=8,relief=GROOVE,bg='#8A360F' )
    customer_detail_frame.pack(fill=X)
    # give label and Entry for phone number of customer in Customer detail frame 
    phoneLabel=Label(customer_detail_frame,text="Phone Number",font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    phoneLabel.grid(row=0,column=0,padx=20)
    phoneEntry=Entry(customer_detail_frame,font=('arial',12),bd=7,width=18)
    phoneEntry.grid(row=0,column=1,padx=8)
    vars= phoneEntry.get() 
    
     # give lable and Entry for Name of customer in Customer detail frame 
    nameLabel=Label(customer_detail_frame,text=" Customer Name",font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    nameLabel.grid(row=0,column=2,padx=20)
    nameEntry=Entry(customer_detail_frame,font=('arial',12),bd=7,width=18)
    nameEntry.grid(row=0,column=3,padx=8)
     # give lable and Entry for phone bill no of customer in Customer detail frame 
    bill_no_Label=Label(customer_detail_frame,text="Phone No",font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    bill_no_Label.grid(row=0,column=4,padx=20)
    bill_no_Entry=Entry(customer_detail_frame,font=('arial',12),bd=7,width=18)
    bill_no_Entry.grid(row=0,column=5,padx=8)
    # Search button for select previous Bill if bill no is given
    searchButton=Button(customer_detail_frame,text="SEARCH",font=('arial',12,'bold'),bd=7,width=10,
                        command=search_bill
                       )
    searchButton.grid(row=0,column=6,padx=20,pady=8)
    
    
    productFrame=Frame(root)
    productFrame.pack(pady=5)
    
    # frame for Cosmetics product
    cosmeticsFrame=LabelFrame(productFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='#8A360F')
    cosmeticsFrame.grid(row=0,column=0,padx=5)
    
    
    # showing heading of these
    productLabel= Label(cosmeticsFrame,text='Product',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    productLabel.grid(row=0,column=0,pady=6,padx=8)
    priceLabel= Label(cosmeticsFrame,text='Price',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    priceLabel.grid(row=0,column=1,pady=6,padx=8)
    quantityLabel= Label(cosmeticsFrame,text='Quantity',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    quantityLabel.grid(row=0,column=2,pady=6,padx=8)
    totalLabel= Label(cosmeticsFrame,text='Total',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    totalLabel.grid(row=0,column=3,pady=6,padx=8)
    # Label And Entry for bathsoap in cosmeticsFrame
    bathsoapLabel= Label(cosmeticsFrame,text='Bath Soap',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    bathsoapLabel.grid(row=1,column=0,pady=6,padx=8)
    price_bath_soap=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_bath_soap.grid(row=1,column=1,pady=6,padx=8)
    price_bath_soap.insert(0,10)
    bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    bathsoapEntry.grid(row=1,column=2,pady=6,padx=8)
    bathsoapEntry.insert(0,0)
    total_bath_soap=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_bath_soap.grid(row=1,column=3,pady=6,padx=8)
    # Label And Entry for tea in cosmeticsFrame
    
    facecreamLabel= Label(cosmeticsFrame,text='Face cream',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    facecreamLabel.grid(row=2,column=0,pady=6,padx=8)
    price_face_cream=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_face_cream.grid(row=2,column=1,pady=6,padx=8)
    price_face_cream.insert(0,40)
    facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    facecreamEntry.grid(row=2,column=2,pady=6,padx=8)
    facecreamEntry.insert(0,0)
    total_face_cream=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_face_cream.grid(row=2,column=3,pady=6,padx=8)
    
    # Label And Entry for faceWash in cosmeticsFrame
    faceWashLabel= Label(cosmeticsFrame,text='Face Wash',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    faceWashLabel.grid(row=3,column=0,pady=6,padx=8)
    price_face_wash=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_face_wash.grid(row=3,column=1,pady=6,padx=8)
    price_face_wash.insert(0,60)
    faceWashEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    faceWashEntry.grid(row=3,column=2,pady=6,padx=8)
    faceWashEntry.insert(0,0)
    total_face_wash=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_face_wash.grid(row=3,column=3,pady=6,padx=8)
    ## Label And Entry for Hai Sparay in cosmeticsFrame
    hairSprayLabel= Label(cosmeticsFrame,text='Hair Spray',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    hairSprayLabel.grid(row=4,column=0,pady=9,padx=10)
    price_hair_sparay=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_hair_sparay.grid(row=4,column=1,pady=6,padx=8)
    price_hair_sparay.insert(0,70)
    hairSprayEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    hairSprayEntry.grid(row=4,column=2,pady=6,padx=8)
    hairSprayEntry.insert(0,0)
    total_hair_spray=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_hair_spray.grid(row=4,column=3,pady=6,padx=8)
    # Label And Entry for Hai Gel in cosmeticsFrame
    hairGelLabel= Label(cosmeticsFrame,text='Hair Gel',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    hairGelLabel.grid(row=5,column=0,pady=6,padx=8)
    price_hair_gel=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_hair_gel.grid(row=5,column=1,pady=6,padx=8)
    price_hair_gel.insert(0,45)
    hairGelEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    hairGelEntry.grid(row=5,column=2,pady=6,padx=8)
    hairGelEntry.insert(0,0)
    total_hair_gel=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_hair_gel.grid(row=5,column=3,pady=6,padx=8)
    # Label And Entry for tea in cosmeticsFrame
    BodyLotionLabel= Label(cosmeticsFrame,text='Body Lotion',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    BodyLotionLabel.grid(row=6,column=0,pady=6,padx=8)
    price_body_lotion=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_body_lotion.grid(row=6,column=1,pady=6,padx=8)
    price_body_lotion.insert(0,90)
    BodyLotionEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    BodyLotionEntry.grid(row=6,column=2,pady=6,padx=8)
    BodyLotionEntry.insert(0,0)
    total_body_lotion=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_body_lotion.grid(row=6,column=3,pady=6,padx=8)
    # Label And Entry for Hand Cream in cosmeticsFrame
    HandCreamLabel= Label(cosmeticsFrame,text='Hand Cream',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    HandCreamLabel.grid(row=7,column=0,pady=6,padx=8)
    price_hand_cream=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_hand_cream.grid(row=7,column=1,pady=6,padx=8)
    price_hand_cream.insert(0,120)
    HandCreamEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    HandCreamEntry.grid(row=7,column=2,pady=6,padx=8)
    HandCreamEntry.insert(0,0)
    total_hand_cream=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_hand_cream.grid(row=7,column=3,pady=6,padx=8)
    # Label And Entry for Nail_paint in cosmeticsFrame
    NailpaintLabel= Label(cosmeticsFrame,text='Nail Paint',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    NailpaintLabel.grid(row=8,column=0,pady=6,padx=8)
    price_nail_paint=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_nail_paint.grid(row=8,column=1,pady=6,padx=8)
    price_nail_paint.insert(0,25)
    NailpaintEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    NailpaintEntry.grid(row=8,column=2,pady=6,padx=8)
    NailpaintEntry.insert(0,0)
    total_nail_paint=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_nail_paint.grid(row=8,column=3,pady=6,padx=8)
    # Label And Entry for Moisturizer in 
    MoisturizerLabel= Label(cosmeticsFrame,text='Moisturizer',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    MoisturizerLabel.grid(row=9,column=0,pady=6,padx=8)
    price_moisturizer=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_moisturizer.grid(row=9,column=1,pady=6,padx=8)
    price_moisturizer.insert(0,99)
    MoisturizerEntry=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    MoisturizerEntry.grid(row=9,column=2,pady=6,padx=8)
    MoisturizerEntry.insert(0,0)
    total_moisturizer=Entry(cosmeticsFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_moisturizer.grid(row=9,column=3,pady=6,padx=8)
    
    
    #Frame for Grocery Product
    GroceryFrame=LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='#8A360F')
    GroceryFrame.grid(row=0,column=1,padx=5)
    # Label And Entry for Rice in GroceryFrame
    productLabel= Label(GroceryFrame,text='Product',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    productLabel.grid(row=0,column=0,pady=6,padx=8)
    priceLabel= Label(GroceryFrame,text='Price',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    priceLabel.grid(row=0,column=1,pady=6,padx=8)
    quantityLabel= Label(GroceryFrame,text='Quantity',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    quantityLabel.grid(row=0,column=2,pady=6,padx=8)
    totalLabel= Label(GroceryFrame,text='Total',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    totalLabel.grid(row=0,column=3,pady=6,padx=8)
    
    RiceLabel= Label(GroceryFrame,text='Rice',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    RiceLabel.grid(row=1,column=0,pady=6,padx=8)
    price_rice=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_rice.grid(row=1,column=1,pady=6,padx=8)
    price_rice.insert(0,110)
    RiceEntry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    RiceEntry.grid(row=1,column=2,pady=6,padx=8)
    RiceEntry.insert(0,0)
    total_rice=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_rice.grid(row=1,column=3,pady=6,padx=8)
    #Label And Entry for Oil in GroceryFrame
    OilLabel= Label(GroceryFrame,text='Oil',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    OilLabel.grid(row=2,column=0,pady=6,padx=8)
    price_oil=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_oil.grid(row=2,column=1,pady=6,padx=8)
    price_oil.insert(0,140)
    OilEntry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    OilEntry.grid(row=2,column=2,pady=6,padx=8)
    OilEntry.insert(0,0)
    total_oil=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_oil.grid(row=2,column=3,pady=6,padx=8)
    #Label And Entry for Daal in GroceryFrame
    DaalLabel= Label(GroceryFrame,text='Daal',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    DaalLabel.grid(row=3,column=0,pady=6,padx=8)
    price_daal=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_daal.grid(row=3,column=1,pady=6,padx=8)
    price_daal.insert(0,130)
    DaalEntry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    DaalEntry.grid(row=3,column=2,pady=6,padx=8)
    DaalEntry.insert(0,0)
    total_daal=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_daal.grid(row=3,column=3,pady=6,padx=8)
    # Label And Entry for Wheat in GroceryFrame
    WheatLabel= Label(GroceryFrame,text='Wheat',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    WheatLabel.grid(row=4,column=0,pady=6,padx=8)
    price_wheat=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_wheat.grid(row=4,column=1,pady=6,padx=8)
    price_wheat.insert(0,32)
    WheatEntry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    WheatEntry.grid(row=4,column=2,pady=6,padx=8)
    WheatEntry.insert(0,0)
    total_wheat=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_wheat.grid(row=4,column=3,pady=6,padx=8)
    # Label And Entry for Sugar in GroceryFrame
    SugarLabel= Label(GroceryFrame,text='Sugar',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    SugarLabel.grid(row=5,column=0,pady=6,padx=8)
    price_sugar=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_sugar.grid(row=5,column=1,pady=6,padx=8)
    price_sugar.insert(0,42)
    SugarEntry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    SugarEntry.grid(row=5,column=2,pady=6,padx=8)
    SugarEntry.insert(0,0)
    total_sugar=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_sugar.grid(row=5,column=3,pady=6,padx=8)
    # Label And Entry for tea in GroceryFrame
    TeaLabel= Label(GroceryFrame,text='Tea',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    TeaLabel.grid(row=6,column=0,pady=6,padx=8)
    price_tea=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_tea.grid(row=6,column=1,pady=6,padx=8)
    price_tea.insert(0,65)
    TeaEntry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    TeaEntry.grid(row=6,column=2,pady=6,padx=8)
    TeaEntry.insert(0,0)
    total_tea=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_tea.grid(row=6,column=3,pady=6,padx=8)
    # Label And Entry for Tomato_Sauce in GroceryFrame
    Tomato_Sauce_Label= Label(GroceryFrame,text='Tomato Sauce',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Tomato_Sauce_Label.grid(row=7,column=0,pady=6,padx=8)
    price_tomato_sauce=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_tomato_sauce.grid(row=7,column=1,pady=6,padx=8)
    price_tomato_sauce.insert(0,101)
    Tomato_Sauce_Entry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Tomato_Sauce_Entry.grid(row=7,column=2,pady=6,padx=8)
    Tomato_Sauce_Entry.insert(0,0)
    total_tomato_sauce=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_tomato_sauce.grid(row=7,column=3,pady=6,padx=8)
    ## Label And Entry for Butter in GroceryFrame
    Butter_Label= Label(GroceryFrame,text='Butter',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Butter_Label.grid(row=8,column=0,pady=6,padx=8)
    price_butter=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_butter.grid(row=8,column=1,pady=6,padx=8)
    price_butter.insert(0,40)
    Butter_Entry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Butter_Entry.grid(row=8,column=2,pady=6,padx=8)
    Butter_Entry.insert(0,0)
    total_butter=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_butter.grid(row=8,column=3,pady=6,padx=8)
    # Label And Entry for Milk in GroceryFrame
    Milk_Label= Label(GroceryFrame,text='Milk',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Milk_Label.grid(row=9,column=0,pady=6,padx=8)
    price_milk=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_milk.grid(row=9,column=1,pady=6,padx=8)
    price_milk.insert(0,65)
    Milk_Entry=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Milk_Entry.grid(row=9,column=2,pady=6,padx=8)
    Milk_Entry.insert(0,0)
    total_milk=Entry(GroceryFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_milk.grid(row=9,column=3,pady=6,padx=8)
    
    
    #frame for Cold Drink Product
    ColdDrinkFrame=LabelFrame(productFrame,text='Cold Drink',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='#8A360F')
    ColdDrinkFrame.grid(row=0,column=3)
    productLabel= Label(ColdDrinkFrame,text='Product',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    productLabel.grid(row=0,column=0,pady=6,padx=8)
    priceLabel= Label(ColdDrinkFrame,text='Price',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    priceLabel.grid(row=0,column=1,pady=6,padx=8)
    quantityLabel= Label(ColdDrinkFrame,text='Quantity',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    quantityLabel.grid(row=0,column=2,pady=6,padx=8)
    totalLabel= Label(ColdDrinkFrame,text='Total',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    totalLabel.grid(row=0,column=3,pady=6,padx=8)
    # Label And Entry for Coca_cola in ColdDrinkFrame
    Coca_colaLabel= Label(ColdDrinkFrame,text='Coca cola',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Coca_colaLabel.grid(row=1,column=0,pady=6,padx=8)
    price_coca_cola=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_coca_cola.grid(row=1,column=1,pady=6,padx=8)
    price_coca_cola.insert(0,69)
    Coca_colaEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Coca_colaEntry.grid(row=1,column=2,pady=6,padx=8)
    Coca_colaEntry.insert(0,0)
    total_coca_cola=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_coca_cola.grid(row=1,column=3,pady=6,padx=8)
    ## Label And Entry for Frooti in ColdDrinkFrame
    FrootiLabel= Label(ColdDrinkFrame,text='Frooti',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    FrootiLabel.grid(row=2,column=0,pady=6,padx=8)
    price_frooti=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_frooti.grid(row=2,column=1,pady=6,padx=8)
    price_frooti.insert(0,65)
    FrootiEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    FrootiEntry.grid(row=2,column=2,pady=6,padx=8)
    FrootiEntry.insert(0,0)
    total_frooti=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_frooti.grid(row=2,column=3,pady=6,padx=8)
    # Label And Entry for Dew in ColdDrinkFrame
    DewLabel= Label(ColdDrinkFrame,text='Dew',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    DewLabel.grid(row=3,column=0,pady=6,padx=8)
    price_dew=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_dew.grid(row=3,column=1,pady=6,padx=8)
    price_dew.insert(0,55)
    DewEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    DewEntry.grid(row=3,column=2,pady=6,padx=8)
    DewEntry.insert(0,0)
    total_dew=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_dew.grid(row=3,column=3,pady=6,padx=8)
    ## Label And Entry for Sprite in ColdDrinkFrame
    SpriteLabel= Label(ColdDrinkFrame,text='Sprite',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    SpriteLabel.grid(row=4,column=0,pady=6,padx=8)
    price_sprite=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_sprite.grid(row=4,column=1,pady=6,padx=8)
    price_sprite.insert(0,65)
    SpriteEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    SpriteEntry.grid(row=4,column=2,pady=6,padx=8)
    SpriteEntry.insert(0,0)
    total_sprite=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_sprite.grid(row=4,column=3,pady=6,padx=8)
    # Label And Entry for Pepsi in ColdDrinkFrame
    PepsiLabel= Label(ColdDrinkFrame,text='Pepsi',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    PepsiLabel.grid(row=5,column=0,pady=6,padx=8)
    price_pepsi=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_pepsi.grid(row=5,column=1,pady=6,padx=8)
    price_pepsi.insert(0,35)
    PepsiEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    PepsiEntry.grid(row=5,column=2,pady=6,padx=8)
    PepsiEntry.insert(0,0)
    total_pepsi=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_pepsi.grid(row=5,column=3,pady=6,padx=8)
    # Label And Entry for Maaza in ColdDrinkFrame
    MaazaLabel= Label(ColdDrinkFrame,text='Maaza',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    MaazaLabel.grid(row=6,column=0,pady=6,padx=8)
    price_maazza=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_maazza.grid(row=6,column=1,pady=6,padx=8)
    price_maazza.insert(0,65)
    MaazaEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    MaazaEntry.grid(row=6,column=2,pady=6,padx=8)
    MaazaEntry.insert(0,0)
    total_maaza=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_maaza.grid(row=6,column=3,pady=6,padx=8)
    # Label And Entry for Mountain_Dew in ColdDrinkFrame
    Mountain_DewLabel= Label(ColdDrinkFrame,text='Mountain Dew',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Mountain_DewLabel.grid(row=7,column=0,pady=6,padx=8)
    price_mountain_dew=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_mountain_dew.grid(row=7,column=1,pady=6,padx=8)
    price_mountain_dew.insert(0,105)
    
    Mountain_DewEntry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Mountain_DewEntry.grid(row=7,column=2,pady=6,padx=8)
    Mountain_DewEntry.insert(0,0)
    total_mountain_dew=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_mountain_dew.grid(row=7,column=3,pady=6,padx=8)
    # Label And Entry for Apple_fizz in ColdDrinkFrame
    Apple_fizz_Label= Label(ColdDrinkFrame,text='Apple Fizz',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Apple_fizz_Label.grid(row=8,column=0,pady=6,padx=8)
    price_apple_fizz_label=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_apple_fizz_label.grid(row=8,column=1,pady=6,padx=8)
    price_apple_fizz_label.insert(0,125)
    Apple_fizz_Entry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Apple_fizz_Entry.grid(row=8,column=2,pady=6,padx=8)
    Apple_fizz_Entry.insert(0,0)
    total_apple_fizz=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_apple_fizz.grid(row=8,column=3,pady=6,padx=8)
    ## Label And Entry for Limca in ColdDrinkFrame
    Limca_Label= Label(ColdDrinkFrame,text='Limca',font=('time new roman',12,'bold'),bg='#8A360F',fg="white")
    Limca_Label.grid(row=9,column=0,pady=6,padx=8)
    price_limca=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    price_limca.grid(row=9,column=1,pady=6,padx=8)
    price_limca.insert(0,65)
    Limca_Entry=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    Limca_Entry.grid(row=9,column=2,pady=6,padx=8)
    Limca_Entry.insert(0,0)
    total_limca=Entry(ColdDrinkFrame,font=('times new roman',12,'bold'),width=5,bd=4)
    total_limca.grid(row=9,column=3,pady=6,padx=8)
    
    
    #In the Product frame for showing bill to create billframe .
    billframe=Frame(productFrame,bd=8,relief=GROOVE)
    billframe.grid(row=0,column=4,padx=10)
    #give the heading of the Frame to show that it is a bill represent block
    billareaLabel = Label(billframe,text='Bill Area',font=('times new roman',12,'bold'),bd=7,relief=GROOVE)
    billareaLabel.pack(fill=X)
    #create scroll bar to scroll it if bill is to long 
    scrollbar=Scrollbar(billframe,orient=VERTICAL)
    scrollbar.pack(side=RIGHT,fill=Y)
    # for showing the bill you create a textarea of size with 28X70
    textarea=Text(billframe,height=24,width=49,yscrollcommand=scrollbar.set)
    textarea.pack()
    scrollbar.config(command=textarea.yview)
    
    
    #in last to create billMenu frame for create price list
    billMenuframe=LabelFrame(root,text="Bill Menu",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='#8A360F')
    billMenuframe.pack(fill=X)
    #Label and Entry for the Cosmetics Price in Billframemenu
    cosmeticspriceLabel= Label(billMenuframe,text='Cosmetic Price',font=('time new roman',15,'bold'),bg='#8A360F',fg="white")
    cosmeticspriceLabel.grid(row=0,column=0,pady=9,padx=10)
    cosmeticspriceEntry=Entry(billMenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
    cosmeticspriceEntry.grid(row=0,column=1,pady=9,padx=10)
    #Label and Entry for the cosmetics_tax in Billframemenu
    cosmetics_tax_Label= Label(billMenuframe,text='Cosmetic Tax',font=('time new roman',15,'bold'),bg='#8A360F',fg="white")
    cosmetics_tax_Label.grid(row=0,column=2,pady=9,padx=10)
    cosmetics_tax_Entry=Entry(billMenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
    cosmetics_tax_Entry.grid(row=0,column=3,pady=9,padx=10)
    #Label and Entry for the Groceryprice in Billframemenu
    GrocerypriceLabel= Label(billMenuframe,text='Grocery Price',font=('time new roman',15,'bold'),bg='#8A360F',fg="white")
    GrocerypriceLabel.grid(row=1,column=0,pady=9,padx=10)
    GrocerypriceEntry=Entry(billMenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
    GrocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)
    #Label and Entry for the Grocery_tax in Billframemenu
    Grocery_tax_Label= Label(billMenuframe,text='Grocery Tax',font=('time new roman',15,'bold'),bg='#8A360F',fg="white")
    Grocery_tax_Label.grid(row=1,column=2,pady=9,padx=10)
    Grocery_tax_Entry=Entry(billMenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
    Grocery_tax_Entry.grid(row=1,column=3,pady=9,padx=10)
    #Label and Entry for the Cold_drink in Billframemenu
    Cold_drink_priceLabel= Label(billMenuframe,text='Cold Drink Price',font=('time new roman',15,'bold'),bg='#8A360F',fg="white")
    Cold_drink_priceLabel.grid(row=2,column=0,pady=9,padx=10)
    Cold_drink_priceEntry=Entry(billMenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
    Cold_drink_priceEntry.grid(row=2,column=1,pady=9,padx=10)
    #Label and Entry for the Cold_drink_Tax in Billframemenu
    Cold_drink_TaxLabel= Label(billMenuframe,text='Cold Drink Tax',font=('time new roman',15,'bold'),bg='#8A360F',fg="white")
    Cold_drink_TaxLabel.grid(row=2,column=2,pady=9,padx=10)
    Cold_drink_TaxEntry=Entry(billMenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
    Cold_drink_TaxEntry.grid(row=2,column=3,pady=9,padx=10)
    #Create buttonframe for the different button in billmenu frame
    buttonFrame=Frame(billMenuframe,bd=8,relief=GROOVE)
    buttonFrame.grid(row=0,column=4,rowspan=3,padx=60)
    #create total button for adding all price 
    total_Button=Button(buttonFrame,text="Total",font=('arial',16,'bold'),bg='#8A360F',fg="white",bd=5,width=8,pady=10,relief=GROOVE,command=total)
    total_Button.grid(row=0,column=0,pady=20,padx=10)
    #create bill button to show the bill
    Bill_Button=Button(buttonFrame,text="Bill",font=('arial',16,'bold'),bg='#8A360F',fg="white",bd=5,width=8,pady=10,relief=GROOVE,command=bill_area)
    Bill_Button.grid(row=0,column=1,pady=20,padx=10)
    #create email button to send the bill to customer email 
    Email_Button=Button(buttonFrame,text="Email",font=('arial',16,'bold'),bg='#8A360F',fg="white",bd=5,width=8,pady=10,relief=GROOVE,command=send_email)
    Email_Button.grid(row=0,column=2,pady=20,padx=10)
    #create print button to print the bill with the help of printer
    Print_Button=Button(buttonFrame,text="Print",font=('arial',16,'bold'),bg='#8A360F',fg="white",bd=5,width=8,pady=10,relief=GROOVE,command=print_bill)
    Print_Button.grid(row=0,column=3,pady=20,padx=10)
    #create clear button to clear to bill text area 
    Clear_Button=Button(buttonFrame,text="Clear",font=('arial',16,'bold'),bg='#8A360F',fg="white",bd=5,width=8,pady=10,relief=GROOVE,command=clear)
    Clear_Button.grid(row=0,column=5,pady=20,padx=10)
    Clear_Button=Button(buttonFrame,text="Save",font=('arial',16,'bold'),bg='#8A360F',fg="white",bd=5,width=8,pady=10,relief=GROOVE,command=save_bill)
    Clear_Button.grid(row=0,column=4,pady=20,padx=10)
    
    root.mainloop()  
#creating main window
root=Tk()
root.geometry('670x400')
background="floral white"
root.configure(bg=background)
root.resizable(False,False)

#adding title and icon
root.iconbitmap('icon.ico')
root.title('Login Software')
frame = Frame (root,width=300,height=200,bg="gainsboro",relief="solid")
frame.place(x=320,y=80)
#
photo=PhotoImage(file="logo.png")
l1=Label(image=photo)
frame = Frame (root,width=300,height=200,
               bg="gainsboro",relief="solid")
frame.place(x=320,y=80)
l1.place(x=45,y=70)
frame.pack_propagate(False)
##
entry_user_id=Entry(frame,font=('gothic',10,'bold'),bd=3,relief=GROOVE,width=25)
entry_user_id.place(x=40,y=40)
entry_id = Label(frame,text = "Id")
entry_id.place(x=1,y=40)

entry_password=Entry(frame,font=('gothic',10,'bold'),bd=3,relief=GROOVE,width=25)
entry_password.place(x=40,y=100)
entry_pass = Label(frame,text= "Pass")
entry_pass.place(x=1,y=100)
#login button
login_button=Button(frame,text="Login",command=login)
login_button.place(x=110,y=150)
SignUp_button=Button(frame,text="New User",command=Insert)
SignUp_button.place(x=160,y=150)

root.mainloop()
