"""
    This component provides simplified api of
    tk widget creator.
"""


import tkinter as tk


"""
    Set weight to rows so that the space between rows
    are proper set.
"""
def row_conf(parent, row, wei):
    for i in range(len(row)):
        parent.rowconfigure(row[i], weight=wei[i])


"""
    Set weight to columns so that the space between columns
    are proper set.
"""
def col_conf(parent, row, wei):
    for i in range(len(row)):
        parent.columnconfigure(row[i], weight=wei[i])


def create_frame(parent, width, height, row, column,
                 columnspan=1, rowspan=1):
    new_frame = tk.Frame(parent, width=width, height=height)
    new_frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
    # not scaling by the child widgets
    new_frame.grid_propagate(0)
    # set background to black
    new_frame['background'] = 'black'
    return new_frame


def create_button(parent, text, command, row, column,
                  rowspan=1, columnspan=1, sticky=tk.W + tk.E,
                  background='black', foreground='white'):
    new_button = tk.Button(parent, text=text, command=lambda : command(text))
    new_button.grid(row=row, column=column,
                    rowspan=rowspan, columnspan=columnspan,
                    sticky=sticky, padx=2, pady=2)
    new_button['background'] = background
    new_button['foreground'] = foreground
    new_button['activebackground'] = background
    new_button['activeforeground'] = foreground
    return new_button


def create_radiobutton(parent, text, vari, command, val, row, column,
                       background='black', foreground='black'):
    new_radiobutton = tk.Radiobutton(parent, text=text, value=val,
                                     variable=vari, command=command)
    new_radiobutton.grid(row=row, column=column, sticky=tk.W + tk.E,
                         padx=3)
    new_radiobutton['background'] = background
    new_radiobutton['foreground'] = foreground
    new_radiobutton['activebackground'] = background
    new_radiobutton['activeforeground'] = foreground
    new_radiobutton['highlightthickness'] = 0
    return new_radiobutton


def create_entry(parent, vari, row, column):
    new_entry = tk.Entry(parent, textvariable=vari, width=12, justify='right')
    new_entry.grid(row=row, column=column)
    return new_entry


def create_label(parent, text, row, column,
                 rowspan=1, columnspan=1, sticky=tk.W,
                 background='black', foreground='white'):
    new_label = tk.Label(parent, text=text, justify=tk.CENTER)
    new_label.grid(row=row, column=column,
                   rowspan=rowspan,
                   columnspan=columnspan,
                   sticky=sticky)
    new_label['background'] = background
    new_label['foreground'] = foreground
    return new_label
