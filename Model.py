"""
    This component implements most part of logic.
    It is responsible for tax and pension calculation.
    It also check the validity of input.
    And it dose not consider and interfaces with users.
"""


"""
    Convert string to float number.
    Only non-negative number allowed.
    Only two decimals are allowed.
"""
def s2f(s):
    if len(s) == 0:
        return 0.0
    f = None
    try:
        f = float(s)
    except Exception:
        pass
    if f is None:
        return "Not a number!"
    if f < 0:
        return "Negative number!"
    try:
        idx = s.index(".")
    except Exception as e:
        # no dot found
        idx = len(s)
    if len(s) - idx > 3:
        return "At most two decimals!"
    return f


"""
    Some comments on income.
"""
def judge_income(income, invs):
    if income > 1000000:
        return "Millionaire!!!"
    msg = [
        "Excellent!",
        "Well done!",
        "Keep going!",
        "Tax free!"
    ]
    for i in range(len(invs)):
        if income > invs[i][0]:
            return msg[i]
    return msg[-1]


class Model(object):

    def __init__(self):
        # register of other two modules
        self.view = None
        # tax rate as intervals
        self.tax_interval = [
            (150000.0, 0.45),
            (046350.0, 0.40),
            (011850.0, 0.20)
        ]
        # insurance rate as intervals
        self.insurance_interval = [
            (46350.0, 0.02),
            (08400.0, 0.12)
        ]
        # yearly or monthly
        self.mode = None
        # user input values
        self.gross = 0.0
        self.rate = 0.0
        # display values
        self.income = 0.0
        self.tax = 0.0
        self.pension = 0.0
        self.nic = 0.0

    def register_view(self, view):
        self.view = view

    def init_mode(self, mode):
        self.mode = mode
        mode.set('yearly')

    def set_mode(self, mode):
        self.mode.set(mode)

    def init_input(self):
        self.gross = 0.0
        return self.gross

    """
        Given a string of user input income.
        Check if the input is valid or not.
        If invalid, return error type.
        If valid, update model values
    """
    def set_income(self, s):
        res = s2f(s)
        if type(res) == str:
            return "Error:" + res
        if res > 1000000000:
            return "Error:" + "Too much to be real!"
        chk = self.update(gross=res)
        if chk != "Success":
            return "Error:" + chk
        msg = judge_income(self.income, self.tax_interval)
        return "Success:" + msg

    def init_rate(self):
        self.rate = 0.0
        return self.rate

    """
        Given a string of user input rate.
        Check if the input is valid or not.
        If invalid, return error type.
        If valid, update model values.
    """
    def set_rate(self, s):
        res = s2f(s)
        if type(res) == str:
            return "Error:" + res
        if res > 100:
            return "Error:" + "No more than 100!"
        chk = self.update(rate=res)
        if chk != "Success":
            return "Error:" + chk
        return "Success:"

    def get_tax(self, income):
        tax = 0.0
        for inv in self.tax_interval:
            if income > inv[0]:
                tax += (income - inv[0]) * inv[1]
                income = inv[0]
        return tax

    def get_nic(self, income):
        insurance = 0.0
        for inv in self.insurance_interval:
            if income > inv[0]:
                insurance += (income - inv[0]) * inv[1]
                income -= inv[0]
        return insurance

    """
        Update display values according to
        given income or rate
    """
    def update(self, gross=None, rate=None):
        if gross is None:
            gross = self.gross
        if rate is None:
            rate = self.rate
        income = gross
        if self.mode.get() == 'monthly':
            income *= 12
        tax = self.get_tax(income)
        pension = income * rate / 100.0
        nic = self.get_nic(income)

        # the sum of tax, pension and nic should
        # not exceed gross income
        if nic + pension + tax > income:
            return "Pension rate too high!"
        income -= tax + pension + nic

        # update result
        self.gross = gross
        self.rate = rate
        self.income = income
        self.tax = tax
        self.pension = pension
        self.nic = nic
        self.view.display_result(income, tax,
                                 pension, nic)
        return "Success"
