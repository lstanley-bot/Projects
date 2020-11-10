from user import authentication
from transactions import journal
# from banking import reconciliation
# from banking.fvb.reconciliation import do_reconciliation as fvb
# from banking.ubsa.reconciliation import do_reconciliation as ubsa
# from banking.online.reconciliation import do_reconciliation as online
from banking import reconciliation
import sys


def print_words():
    '''
    finds the length of sys.argv; 
    if its more than 1 it prints the messages in a new line
    '''
    if len(sys.argv) > 1:
        print('\n'.join(sys.argv[1:]))


if __name__ == "__main__":
    print_words()
    authentication.authenticate_user()
    amount = 100
    journal.receive_income(amount)
    journal.pay_expense(amount)
    reconciliation.do_reconciliation()
    # fvb()
    # ubsa()
    # online()
