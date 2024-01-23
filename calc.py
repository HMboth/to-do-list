from tkinter import *
import math

#****************FUNCTIONS********************
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op
#******************FUNCTIONS********************
#******************VAR*********************************
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'
#******************VAR*********************************

root = Tk()
root.configure(bg="#293C4A", bd=10)
root.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(root, font=('Times', 15, 'bold'), textvariable=text_input,bd=5, insertwidth = 3, bg='gray', justify='right')
text_display.grid(columnspan=5, padx = 10, pady = 15)

button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('Times', 17, 'bold')}
button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('Times', 17, 'bold')}

#**************BUTTONS**********************************
btn_1 = Button(root, button_params_main, text='1',command=lambda:button_click('1'))
btn_1.grid(row=1, column=0, sticky="nsew")

btn_2 = Button(root, button_params_main, text='2',command=lambda:button_click('2'))
btn_2.grid(row=1, column=1, sticky="nsew")

btn_3 = Button(root, button_params_main, text='3',command=lambda:button_click('3'))
btn_3.grid(row=1, column=2, sticky="nsew")

DEL_btn = Button(root, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='DEL', command=button_delete, bg='#db701f')
DEL_btn.grid(row=1, column=3, sticky="nsew")

AC_btn = Button(root, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),text='AC', command=button_clear_all, bg='#db701f')
AC_btn.grid(row=1, column=4, sticky="nsew")

btn_4 = Button(root, button_params_main, text='4',command=lambda:button_click('4'))
btn_4.grid(row=2, column=0, sticky="nsew")

btn_5 = Button(root, button_params_main, text='5',command=lambda:button_click('5'))
btn_5.grid(row=2, column=1, sticky="nsew")

btn_6 = Button(root, button_params_main, text='6',command=lambda:button_click('6'))
btn_6.grid(row=2, column=2, sticky="nsew")

add_btn = Button(root, button_params_main, text='+',command=lambda:button_click('+'))
add_btn.grid(row=2, column=3, sticky="nsew")

sub_btn = Button(root, button_params_main, text='-',command=lambda:button_click('-'))
sub_btn.grid(row=2, column=4, sticky="nsew")

btn_7 = Button(root, button_params_main, text='7',command=lambda:button_click('7'))
btn_7.grid(row=3, column=0, sticky="nsew")

btn_8 = Button(root, button_params_main, text='8',command=lambda:button_click('8'))
btn_8.grid(row=3, column=1, sticky="nsew")

btn_9 = Button(root, button_params_main, text='9', command=lambda:button_click('9'))
btn_9.grid(row=3, column=2, sticky="nsew")

mul_btn = Button(root, button_params_main, text='*',command=lambda:button_click('*'))
mul_btn.grid(row=3, column=3, sticky="nsew")

div_btn = Button(root, button_params_main, text='/',command=lambda:button_click('/'))
div_btn.grid(row=3, column=4, sticky="nsew")

btn_0 = Button(root, button_params_main, text='0',command=lambda:button_click('0'))
btn_0.grid(row=4, column=0, sticky="nsew")

modulo_btn = Button(root, button_params, text='mod',command=lambda:button_click('%'))
modulo_btn.grid(row=4, column=1, sticky="nsew")

pi_btn = Button(root, button_params, text='π',command=lambda:button_click(str(math.pi)))
pi_btn.grid(row=4, column=2, sticky="nsew")

cos_btn = Button(root, button_params, text='cos',command=trig_cos)
cos_btn.grid(row=4, column=3, sticky="nsew")

sin_btn = Button(root, button_params, text='sin',command=trig_sin)
sin_btn.grid(row=4, column=4, sticky="nsew")

tan_btn = Button(root, button_params, text='tan',command=trig_tan)
tan_btn.grid(row=5, column=0, sticky="nsew")

cot_btn = Button(root, button_params, text='cot',command=trig_cot)
cot_btn.grid(row=5, column=1, sticky="nsew") 

signs_btn = Button(root, button_params, text='\u00B1',command=sign_change)
signs_btn.grid(row=5, column=2, sticky="nsew")

percentage_btn = Button(root, button_params, text='%',command=percent)
percentage_btn.grid(row=5, column=3, sticky="nsew")

ex_btn = Button(root, button_params, text='e^x',command=lambda:button_click('e('))
ex_btn.grid(row=5, column=4, sticky="nsew")

second_power_btn = Button(root, button_params, text='x\u00B2',command=lambda:button_click('**2'))
second_power_btn.grid(row=6, column=0, sticky="nsew")

third_power_btn = Button(root, button_params, text='x\u00B3',command=lambda:button_click('**3'))
third_power_btn.grid(row=6, column=1, sticky="nsew")

nth_power_btn = Button(root, button_params, text='x^n',command=lambda:button_click('**'))
nth_power_btn.grid(row=6, column=2, sticky="nsew")

square_root_btn = Button(root, button_params, text='\u00B2\u221A',command=square_root)
square_root_btn.grid(row=6, column=3, sticky="nsew")

nth_root_btn = Button(root, button_params, text='\u221A',command=lambda:button_click('**(1/'))
nth_root_btn.grid(row=6, column=4, sticky="nsew")

log_10_btn = Button(root, button_params, text='log\u2081\u2080', font=('sans-serif', 16, 'bold'),command=lambda:button_click('log('))
log_10_btn.grid(row=7, column=0, sticky="nsew")

log_btn = Button(root, button_params, text='ln',command=lambda:button_click('ln('))
log_btn.grid(row=7, column=1, sticky="nsew")

left_par_btn = Button(root, button_params, text='(',command=lambda:button_click('('))
left_par_btn.grid(row=7, column=2, sticky="nsew")

right_par_btn = Button(root, button_params, text=')',command=lambda:button_click(')'))
right_par_btn.grid(row=7, column=3, sticky="nsew")

equal_btn = Button(root, button_params_main, text='=',command=button_equal)
equal_btn.grid(row=7, column=4, sticky="nsew")
#**************BUTTONS**********************************

root.mainloop()