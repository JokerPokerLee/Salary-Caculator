"""
    This component is responsible for build
    user interfaces and event reaction bindings.
"""


from tk_op import *


class View(object):

    def __init__(self):
        # register of other two modules
        self.controller = None
        self.model = None

        # main window size
        self.window_width = 280
        self.window_height = 320
        # mode select panel size
        self.select_width = 100
        self.select_height = 50

        # tk root object
        self.root = None
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
        self.income_label = None
        self.tax_label = None
        self.pension_label = None
        self.nic_label = None

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

    def build_ui(self):
        self.init_main_window()

        # build frame for displaying result
        self.result_frame = create_frame(self.root,
                                         self.window_width,
                                         self.window_height // 8 * 2,
                                         0, 0)
        self.build_result(self.result_frame)

        # build frame for displaying warning message and comments
        self.msg_frame = create_frame(self.root,
                                      self.window_width,
                                      self.window_height // 8 * 1,
                                      2, 0)
        self.build_msg(self.msg_frame)

        # build frame for input frame
        self.input_frame = create_frame(self.root,
                                        self.window_width,
                                        self.window_height // 8 * 1,
                                        4, 0)
        self.build_input(self.input_frame)

        # build frame for buttons
        self.button_frame = create_frame(self.root,
                                         self.window_width,
                                         self.window_height // 8 * 4,
                                         6, 0)
        self.build_button(self.button_frame)

    def build_result(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 3, 8], [5, 5, 5])
        col_conf(parent, [0, 2, 4], [4, 5, 4])

        # two labels each for income, tax, pension and nic
        create_label(parent, "Income($/y):", 1, 1)
        self.income_label = create_label(parent, "0.00",
                                         2, 1, sticky=tk.E)
        create_label(parent, "Tax($/y):", 1, 3)
        self.tax_label = create_label(parent, "0.00",
                                      2, 3, sticky=tk.E)
        create_label(parent, "Pension($/y):", 4, 1)
        self.pension_label = create_label(parent, "0.00",
                                          5, 1, sticky=tk.E)
        create_label(parent, "NICs($/y):", 4, 3)
        self.nic_label = create_label(parent, "0.00",
                                      5, 3, sticky=tk.E)

    def build_msg(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 2], [1, 1])
        col_conf(parent, [0, 2], [1, 1])
        self.msg_label = create_label(parent, "", 1, 2)

    def build_input(self, parent):
        # assign weight to rows and column
        row_conf(parent, [0, 2, 4], [1, 1, 1])
        col_conf(parent, [0, 2, 4], [4, 3, 4])

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
        col_conf(parent, [0, 6], [1, 1])

        # create buttons for digits
        digit_button = []
        for i in range(1, 10):
            digit_button.append(create_button(self.button_frame, str(i),
                                              self.controller.on_button_click,
                                              (i - 1) // 3 + 1,
                                              (i - 1) % 3 + 1))
        # disable tab to highlight buttons
        digit_button[1].bind("<FocusIn>", lambda e: self.root.focus_set())

        # create special button
        create_button(self.button_frame, '0',
                      self.controller.on_button_click, 4, 1)
        create_button(self.button_frame, '.',
                      self.controller.on_button_click, 4, 2)
        create_button(self.button_frame, '00',
                      self.controller.on_button_click, 4, 3)
        create_button(self.button_frame, '<',
                      self.controller.on_button_click,
                      3, 4, columnspan=1)
        create_button(self.button_frame, 'C',
                      self.controller.on_button_click,
                      4, 4, columnspan=1)

        # crate sub-frame to place radio buttons
        select_frame = create_frame(self.button_frame,
                                    self.select_width,
                                    self.select_height,
                                    1, 4, rowspan=2, columnspan=1)
        mode = tk.StringVar()
        self.model.init_mode(mode)
        create_radiobutton(select_frame, "yearly", mode,
                           self.controller.on_mode_switch,
                           'yearly', 0, 0)
        create_radiobutton(select_frame, "monthly", mode,
                           self.controller.on_mode_switch,
                           'monthly', 1, 0)

    def display_msg(self, sign, text):
        self.msg_label['text'] = text
        if sign == 'Success':
            self.msg_label['fg'] = 'black'
        else:
            self.msg_label['fg'] = 'red'

    def display_result(self, income, tax, pension, nic):
        self.income_label['text'] = "%.2f" % round(income, 2)
        self.tax_label['text'] = "%.2f" % round(tax, 2)
        self.pension_label['text'] = "%.2f" % round(pension, 2)
        self.nic_label['text'] = "%.2f" % round(nic, 2)

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
