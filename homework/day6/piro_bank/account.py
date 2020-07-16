import random

def set_random_account_num():
    random_num = list(str(random.randrange(10000000000, 100000000000)))
    random_num.insert(3, '-')
    random_num.insert(6, '-')
    random_account_num = ""
    for _ in random_num:
        random_account_num = random_account_num + _
    return random_account_num


class Account:
    account_count = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.bank_name = "SC 은행"
        self.account_num = set_random_account_num()
        self.deposit_count = 0
        Account.account_count += 1
        self.deposit_list = []
        self.withdraw_list = []

    @classmethod
    def get_account_num(cls):
        print("총 계좌 개수는 {}개 입니다.".format(cls.account_count))

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        if self.deposit_amount >= 1:
            self.deposit_list.append(self.deposit_amount)
            self.balance = self.balance + self.deposit_amount
            print("정상 입금 되었습니다.")
            self.deposit_count += 1
            self.balance = self.interest()
            return(self.balance)
        else:
            return print("최소 입금 금액은 1원 입니다.")
        
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount <= self.balance:
            self.withdraw_list.append(self.withdraw_amount)
            self.balance = self.balance - self.withdraw_amount
            print("정상 출금 되었습니다.")
            return(self.balance)
        else:
            return print("잔액이 부족합니다")

    def display_info(self):
        print("은행이름: {}".format(self.bank_name))
        print("예금주: {}".format(self.account_holder))
        print("계좌번호: {}".format(self.account_num))
        print("잔고: {0:,.2f}원".format(self.balance))

    def interest(self):
        if self.deposit_count % 5 == 0:
            self.balance = self.balance * 1.01
            return self.balance
        else:
            return self.balance

    def deposit_history(self):
        for d in self.deposit_list:
            print("{}원 입금".format(d))

    def withdraw_history(self):
        for w in self.withdraw_list:
            print("{}원 입금".format(w))
