import tkinter as tk
from tkinter import ttk


root = tk.Tk()
#ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
#ttk.Button(frame,text="Hail Hitler", padding=10, command=print("Hail Hitler!")).grid(column=0,row=1)


def calc_stress_from_force_over_area(F, A):
    if not isinstance(F, (int, float)):
        raise TypeError('Force has to be of type int or float')
    if not isinstance(A, (int, float)):
        raise TypeError('Area has to be of type int or float')
    return f'{F/A}MPa'

def calc_strain_from_delta_length_over_initial_length(delta_L, initial_L):
    if not isinstance(delta_L, (int, float)):
        raise TypeError('change in length has to be of type int or float')
    if not isinstance(initial_L, (int, float)):
        raise TypeError('initial length has to be of type int or float')
    return f'{delta_L/initial_L}'

def calc_elongation_from_strain(strain, initial_L):
    if not isinstance(strain, (int, float)):
        raise TypeError('strain has to be of type int or float')
    if not isinstance(initial_L, (int, float)):
        raise TypeError('initial length has to be of type int or float')
    return f'{strain*initial_L}mm'

def calc_stress_from_young_modulus_times_strain(young_modulus, strain):
    return f'{young_modulus * strain}N'

print(calc_elongation_from_strain(0.0005, 2000))
print(calc_strain_from_delta_length_over_initial_length(1, 2000))

rod = {'initial_length': 2000,
       'material': 'steel',
       }

material = tk.StringVar(value=rod['material'])
entry = ttk.Entry(root, textvariable=material)
entry.pack()
result_s = tk.StringVar(value='')
user_input_1 = tk.StringVar(root)
user_input_2 = tk.StringVar(root)
elongation_entry = ttk.Entry(root,
                             textvariable=user_input_1)
initial_length_entry = ttk.Entry(root,
                                 textvariable=user_input_2)

root.title('MDC - Material Deformation Calculator')
root.geometry('640x480')
root.minsize(320, 240)
ttk.Label(root, text='Calculate Material Deformation').pack(padx=20, pady=20)

def print_result():
    print(float(user_input_1.get()) / float(user_input_2.get()))
    result_s.set(str(float(user_input_1.get()) / float(user_input_2.get())))
def print_material(event):
    print('The current entry material is:', material.get())

entry.bind('<Return>', print_material)
def clear():
    material.set('')

elongation_entry.pack()
initial_length_entry.pack()
result = ttk.Entry(root,
                   textvariable=result_s)

ttk.Button(root, text='Clear', command=clear).pack()
ttk.Button(root, text='Calculate strain',
           command=print_result).pack()
result.pack()
#ttk.Button(root, text='Calculate strain',
#           command=calc_strain_from_delta_length_over_initial_length(
#               int(user_input_1), int(user_input_2)
#            )).pack()

root.mainloop()


