"""
    This component handles user input event.
    It convert the events to the forms, which
    can be processed by model component.
    And instruct view component how model
    component react to these event.
"""


class Controller(object):

    def __init__(self):
        # register of other two modules
        self.model = None
        self.view = None
        # input widgets
        self.income = None
        self.rate = None
        # input entry current focused on
        # self.focus = income_entry|rate_entry
        self.focus = 'income'
        # define digit set
        self.digits = [0, 1, 2, 3, 4,
                       5, 6, 7, 8, 9]
        self.digits = list(map(str, self.digits))
        self.digits.append(".")

    def register_model(self, model):
        self.model = model

    def register_view(self, view):
        self.view = view

    def init_income(self, income_label):
        self.income = income_label
        # set initial income to empty string
        self.income['text'] = ""

    def init_rate(self, rate_label):
        self.rate = rate_label
        # set initial rate to empty string
        self.rate['text'] = ""

    """
        Update gross income.
    """
    def update_income(self, text):
        # try to set new income value
        res = self.model.set_income(text).split(':')
        # if set successfully, update income label
        if res[0] == "Success":
            self.income['text'] = text
        # display message
        self.view.display_msg(res[0], res[1])

    """
        Update pension rate.
    """
    def update_rate(self, text):
        # try to set new rate value
        res = self.model.set_rate(text).split(':')
        # if set successfully, update rate label
        if res[0] == "Success":
            self.rate['text'] = text
        # display message
        self.view.display_msg(res[0], res[1])

    """
        Button click event handler.
    """
    def on_button_click(self, text):
        # store previous value in case of new
        # input illegal
        if self.focus == 'income':
            old = self.income['text']
        else:
            old = self.rate['text']

        # get new value by button text
        if text == 'C':
            new = ""
        elif text == '<':
            new = old[:-1]
        else:
            new = old + text

        # try to update focused field
        if self.focus == 'income':
            self.update_income(new)
        else:
            self.update_rate(new)

    """
        Keyboard press event handler.
    """
    def on_key_press(self, event):
        char = event.char
        if char in self.digits:
            # digits can be processed as
            # in button click handler
            self.on_button_click(char)
        elif char == chr(8):
            # backSpace need to be
            # converted to '<' character
            self.on_button_click('<')
        elif char == 'y':
            # change mode to yearly
            self.model.set_mode('yearly')
            self.on_mode_switch()
        elif char == 'm':
            # change mode to monthly
            self.model.set_mode('monthly')
            self.on_mode_switch()

    def on_mode_switch(self):
        self.model.update()

    """
        On income and rate focus change.
    """
    def on_focus_switch(self, focus=None):
        # focus not specified, flip the focus
        if focus is None:
            if self.focus == 'income':
                focus = 'rate'
            else:
                focus = 'income'
        # set new focus
        self.focus = focus
        if focus == 'income':
            # change border to indicate focus
            self.income['relief'] = 'ridge'
            self.rate['relief'] = 'flat'
        elif focus == 'rate':
            # change border to indicate focus
            self.income['relief'] = 'flat'
            self.rate['relief'] = 'ridge'
