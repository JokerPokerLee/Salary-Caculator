"""
    This component is responsible for build
    user interfaces and event reaction bindings.
"""


from tk_op import *
from tkinter import font


class View(object):

    def __init__(self):
        # register of other two modules
        self.controller = None
        self.model = None

        # main window size
        self.window_width = 280
        self.window_height = 360
        # mode select panel size
        self.select_width = 100
        self.select_height = 65
        # height for delete and clear buttons
        self.del_height = 2
        self.clr_height = 2
        # frame heights
        self.tle_height = 30
        self.res_height = 150
        self.msg_height = 25
        self.inp_height = 50
        self.but_height = 160
        self.window_height = self.tle_height \
                             + self.res_height \
                             + self.msg_height \
                             + self.inp_height \
                             + self.but_height

        # tk root object
        self.root = None
        # top level frame
        self.root_frame = None
        # title display panel
        self. title_frame = None
        # result display panel
        self.result_frame = None
        # message display panel
        self.msg_frame = None
        self.msg_label = None
        # input display panel
        self.input_frame = None
        # button display panel
        self.button_frame = None

        # result labels
        self.total_label = None
        self.taxable_label = None
        self.tax_label = None
        self.pension_label = None
        self.nic_label = None
        self.net_label = None

    def register_model(self, model):
        self.model = model

    def register_controller(self, controller):
        self.controller = controller

    def init_main_window(self):
        self.root = tk.Tk()
        self.root.title("Net Salary Calc")
        # use fixed size window
        self.root.resizable(width=tk.FALSE,
                            height=tk.FALSE)
        self.root.geometry('{}x{}'.format(self.window_width,
                                          self.window_height))
        self.root_frame = create_frame(self.root,
                                       self.window_width,
                                       self.window_height,
                                       0, 0)

    def build_ui(self):
        self.init_main_window()

        row_conf(self.root_frame, [0, 6], [1, 1])
        col_conf(self.root_frame, [0, 2], [1, 1])

        # build frame for displaying title
        self.title_frame = create_frame(self.root_frame,
                                        self.window_width,
                                        self.tle_height,
                                        1, 1)
        self.build_title(self.title_frame)

        # build frame for displaying result
        self.result_frame = create_frame(self.root_frame,
                                         self.window_width,
                                         self.res_height,
                                         2, 1)
        self.build_result(self.result_frame)

        # build frame for displaying warning message and comments
        self.msg_frame = create_frame(self.root_frame,
                                      self.window_width,
                                      self.msg_height,
                                      3, 1)
        self.build_msg(self.msg_frame)

        # build frame for input frame
        self.input_frame = create_frame(self.root_frame,
                                        self.window_width,
                                        self.inp_height,
                                        4, 1)
        self.build_input(self.input_frame)

        # build frame for buttons
        self.button_frame = create_frame(self.root_frame,
                                         self.window_width,
                                         self.but_height,
                                         5, 1)
        self.build_button(self.button_frame)

    def build_title(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 2], [1, 10])
        col_conf(parent, [0, 2], [1, 1])

        # create title label
        title = create_label(parent,
                             "Salary Calculator",
                             1, 1, sticky="WE",
                             foreground='#ABB2B9')
        custom_font = font.Font(family="Helvetica", size=18)
        title['font'] = custom_font

    def build_result(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 2], [10, 1])
        col_conf(parent, [0, 2], [4, 4])

        self.res_panel= create_frame(parent,
                                     250,
                                     parent['height'] - 10,
                                     1, 1)
        row_conf(self.res_panel, [0, 3, 6, 9], [5, 5, 5, 5])
        col_conf(self.res_panel, [0, 2, 4], [4, 5, 4])
        self.res_panel['highlightbackground'] = '#ABB2B9'
        self.res_panel['highlightcolor'] = '#ABB2B9'
        self.res_panel['highlightthickness'] = 2
        self.res_panel['bd'] = 0
        background = '#273746'
        self.res_panel['background'] = background
        # two labels each for income, tax, pension and nic
        create_label(self.res_panel, "Total($/y):",
                     1, 1, background=background)
        self.total_label = create_label(self.res_panel, "0.00",
                                        2, 1, sticky=tk.E + tk.W,
                                        background=background)
        create_label(self.res_panel, "Pension($/y):",
                     1, 3, background=background)
        self.pension_label = create_label(self.res_panel, "0.00",
                                          2, 3, sticky=tk.E + tk.W,
                                          background=background)
        create_label(self.res_panel, "Taxable($/y):",
                     4, 1, background=background)
        self.taxable_label = create_label(self.res_panel, "0.00",
                                          5, 1, sticky=tk.E + tk.W,
                                          background=background)
        create_label(self.res_panel, "Tax($/y):",
                     4, 3, background=background)
        self.tax_label = create_label(self.res_panel, "0.00",
                                      5, 3, sticky=tk.E + tk.W,
                                      background=background)
        create_label(self.res_panel, "NICs($/y):",
                     7, 1, background=background)
        self.nic_label = create_label(self.res_panel, "0.00",
                                      8, 1, sticky=tk.E + tk.W,
                                      background=background)
        create_label(self.res_panel, "Net($/y):",
                     7, 3, background=background)
        self.net_label = create_label(self.res_panel, "0.00",
                                      8, 3, sticky=tk.E + tk.W,
                                      background=background)

    def build_msg(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 2], [5, 1])
        col_conf(parent, [0, 2], [1, 1])
        self.msg_label = create_label(parent, "", 1, 2)
        custom_font = font.Font(family="Helvetica", size=12)
        self.msg_label['font'] = custom_font

    def build_input(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 2, 4], [10, 1, 1])
        col_conf(parent, [0, 2, 4], [3, 7, 3])

        # name labels for user input label
        create_label(parent, "Gross income($):", 1, 1)
        create_label(parent, "Pension rate(%):", 1, 3)

        # create a label for displaying user input
        income_label = create_label(parent, "", 3, 1,
                                    sticky=tk.W + tk.E)
        rate_label = create_label(parent, "", 3, 3,
                                  sticky=tk.W + tk.E)

        # register and initiate input labels in controller
        self.controller.init_income(income_label)
        self.controller.init_rate(rate_label)

        # bind keyboard input event

        # bind mouse click event
        income_label.bind('<Button-1>',
                          lambda e: self.controller
                          .on_focus_switch('income'))
        rate_label.bind('<Button-1>',
                        lambda e: self.controller
                        .on_focus_switch('rate'))

        # bind key press event
        self.root.bind('<KeyPress>',
                       self.controller.on_key_press)
        self.root.bind('<BackSpace>',
                       self.controller.on_key_press)
        self.root.bind('<Tab>', lambda e: self.controller.
                       on_focus_switch())

        # focus is initially set to income label
        self.controller.on_focus_switch('income')

    def build_button(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 5], [1, 1])
        col_conf(parent,
                 [0, 1, 2, 3, 4, 5, 6],
                 [6, 5, 5, 5, 1, 1, 6])

        # create buttons for digits
        digit_button = []
        for i in range(1, 10):
            digit_button.append(create_button(self.button_frame, str(i),
                                              self.controller.on_button_click,
                                              (i - 1) // 3 + 1,
                                              (i - 1) % 3 + 1,
                                              background='#626568'))
        # disable tab to highlight buttons
        digit_button[1].bind("<FocusIn>", lambda e: self.root.focus())

        # create special button
        create_button(self.button_frame, '0',
                      self.controller.on_button_click, 4, 1,
                      background='#626568')
        create_button(self.button_frame, '.',
                      self.controller.on_button_click, 4, 2,
                      background='#626568')
        create_button(self.button_frame, '00',
                      self.controller.on_button_click, 4, 3,
                      background='#626568')

        create_button(self.button_frame, 'Delete',
                      self.controller.on_button_click,
                      1, 4, columnspan=2, sticky='WE',
                      background='#AF9D10')
        create_button(self.button_frame, 'Clear',
                      self.controller.on_button_click,
                      2, 4, columnspan=2, sticky='WE',
                      background='#C82106')

        # crate sub-frame to place radio buttons
        select_frame = create_frame(self.button_frame,
                                    self.select_width,
                                    self.select_height,
                                    3, 4, rowspan=2, columnspan=2)
        row_conf(select_frame, [0, 4], [2, 2])

        # create sub-frame for one addition row
        radio_frame = create_frame(select_frame,
                                   self.select_width,
                                   self.select_height,
                                   1, 1, rowspan=3)
        radio_frame['highlightbackground'] = 'white'
        radio_frame['highlightcolor'] = 'white'
        radio_frame['highlightthickness'] = 1
        radio_frame['bd'] = 0
        background = '#2E86C1'
        radio_frame['background'] = background
        mode = tk.StringVar()
        self.model.init_mode(mode)
        create_label(radio_frame, " Mode:", 0, 0,
                     background=background,
                     foreground='black')
        create_radiobutton(radio_frame, "Annual  ", mode,
                           self.controller.on_mode_switch,
                           'yearly', 1, 0, background=background)
        create_radiobutton(radio_frame, "Monthly", mode,
                           self.controller.on_mode_switch,
                           'monthly', 2, 0, background=background)

    def display_msg(self, sign, text):
        self.msg_label['text'] = text
        if sign == 'Success':
            self.msg_label['fg'] = '#01DF74'
        else:
            self.msg_label['fg'] = '#FF0080'

    def display_result(self, total, pension, income, tax, nic, net):
        self.total_label['text'] = "%.2f" % round(total, 2)
        self.taxable_label['text'] = "%.2f" % round(income, 2)
        self.tax_label['text'] = "%.2f" % round(tax, 2)
        self.pension_label['text'] = "%.2f" % round(pension, 2)
        self.nic_label['text'] = "%.2f" % round(nic, 2)
        self.net_label['text'] = "%.2f" % round(net, 2)

    def main_loop(self):
        tk.mainloop()


if __name__ == '__main__':

    view = View()

    import Model
    import Controller
    model = Model.Model()
    controller = Controller.Controller()

    controller.register_model(model)

    view.register_controller(controller)
    view.register_model(model)

    view.build_ui()
    view.main_loop()
