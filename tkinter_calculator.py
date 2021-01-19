from tkinter import *

root = Tk()
root.title('Calculator - Ravi')
root.resizable(0, 0)


input_field = Entry(root, width = '50', borderwidth = 5)
input_field.grid(column = 0, row =0 ,columnspan = 5 , padx = 10 , pady = 10 , sticky=N+E+W+S)


def cal(number):
    current = input_field.get()
    input_field.delete(0,END)
    input_field.insert(0, current+number)


def opt(operation):
    global result_statement
    global current_num
    current_num = input_field.get()
    input_field.delete(0,END)
    result_statement = current_num + operation
    input_field.insert(0, result_statement)


def result():
    try:
        output = eval(input_field.get())
        input_field.delete(0,END)
        input_field.insert(0,output)

    except:
        g='Invalid input'
        input_field.delete(0, END)
        input_field.insert(0,g)


def del_last_num():
    initial_num = input_field.get()
    input_field.delete(len(initial_num)-1)

#creating button


button_1 = Button(root , text = '1',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('1'))
button_2 = Button(root , text = '2',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('2'))
button_3 = Button(root , text = '3',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('3'))
button_4 = Button(root , text = '4',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('4'))
button_5 = Button(root , text = '5',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('5'))
button_6 = Button(root , text = '6',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('6'))
button_7 = Button(root , text = '7',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('7'))
button_8 = Button(root , text = '8',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('8'))
button_9 = Button(root , text = '9',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('9'))
button_0 = Button(root , text = '0',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('0'))
button_dot = Button(root , text = '.',padx=33, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :cal('.'))

button_add = Button(root , text = '+',padx=30, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :opt('+'))
button_sub = Button(root , text = '-',padx=31, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :opt('-'))
button_mutli = Button(root , text = '* ',padx=29, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :opt('*'))
button_div = Button(root , text = ' /',padx=29, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :opt('/'))
button_equal = Button(root , text = '=',padx=29, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :result())
button_del = Button(root , text = 'DEL',padx=18, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :del_last_num())
button_clear = Button(root , text = 'CLEAR ALL',padx=77, pady=10,borderwidth = 5 ,font =15, fg ='white' ,bg ='black' , command = lambda :input_field.delete(0,END))

#position button on the screen

button_1.grid(row=4 ,column = 0,sticky=N+E+W+S)
button_2.grid(row=4 ,column = 1,sticky=N+E+W+S)
button_3.grid(row=4 ,column = 2,sticky=N+E+W+S)
button_0.grid(row=5 ,column = 0,sticky=N+E+W+S)
button_dot.grid(row=5 ,column = 1,sticky=N+E+W+S)

button_4.grid(row=3 ,column = 0,sticky=N+E+W+S)
button_5.grid(row=3 ,column = 1,sticky=N+E+W+S)
button_6.grid(row=3 ,column = 2,sticky=N+E+W+S)

button_7.grid(row=2 ,column = 0,sticky=N+E+W+S)
button_8.grid(row=2 ,column = 1,sticky=N+E+W+S)
button_9.grid(row=2 ,column = 2,sticky=N+E+W+S)

button_add.grid(row=2 ,column = 3,sticky=N+E+W+S)
button_sub.grid(row=2 ,column = 4,sticky=N+E+W+S)
button_mutli.grid(row=3 ,column = 3,sticky=N+E+W+S)
button_div.grid(row=3 ,column = 4,sticky=N+E+W+S)
button_equal.grid(row=4 ,column = 4,sticky=N+E+W+S)
button_del.grid(row=4 ,column = 3,sticky=N+E+W+S)
button_clear.grid(row=5 ,column = 2 , columnspan = 3,sticky=N+E+W+S)

root.mainloop()