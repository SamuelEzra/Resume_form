from tkinter import *
root = Tk()
root.geometry('500x300')

def getvals():
    print('Submitted')

Label(root, text = 'Resume', font = 'ar 15 bold').grid(row = 0, column = 3)

name = Label(root, text = 'Name')
age = Label(root, text = 'Age')
gender = Label(root, text = 'Name')
phone = Label(root, text = 'Phone Number')
email = Label(root, text = 'Email')
address = Label(root, text = 'Address')
work = Label(root, text = 'Work Experience')
education = Label(root, text = 'Institution Attended')
skills = Label(root, text = 'Skills')

name.grid(row = 1, column = 2)
age.grid(row = 2, column = 2)
gender.grid(row = 3, column = 2)
phone.grid(row = 4, column = 2)
email.grid(row = 5, column = 2)
address.grid(row = 6, column = 2)
work.grid(row = 7, column = 2)
education.grid(row = 8, column = 2)
skills.grid(row = 9, column = 2)

name_value = StringVar
age_value = IntVar
gender_value = StringVar
phone_value = IntVar
email_value = StringVar
address_value = StringVar
work_value = StringVar
education_value = StringVar
skills_value = StringVar

name_entry = Entry(root, textvariable = name_value)
age_entry = Entry(root, textvariable = age_value)
gender_entry = Entry(root, textvariable = gender_value)
phone_entry = Entry(root, textvariable = phone_value)
email_entry = Entry(root, textvariable = email_value)
address_entry = Entry(root, textvariable = address_value)
work_entry = Entry(root, textvariable = work_value)
education_entry = Entry(root, textvariable = education_value)
skills_entry = Entry(root, textvariable = skills_value)

name_entry.grid(row = 1, column = 3)
age_entry.grid(row = 2, column = 3)
gender_entry.grid(row = 3, column = 3)
phone_entry.grid(row = 4, column = 3)
email_entry.grid(row = 5, column = 3)
address_entry.grid(row = 6, column = 3)
work_entry.grid(row = 7, column = 3)
education_entry.grid(row = 8, column = 3)
skills_entry.grid(row = 9, column = 3)

Button(text = 'Submit', command = getvals).grid(row = 10, column = 3)

root.mainloop()