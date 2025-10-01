from app.calculations import add ,subtract, multiply, divide, BankAccount, Insufficient
import pytest 


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8)
])
def test_add(num1, num2, expected):
    assert  add(num1,num2) == expected


def test_bank_set_initial_amount(zero_bank_acount):
    assert zero_bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account == 0 

def test_withdraw(zero_bank_account):
    assert zero_bank_account.withdraw(20)

def test_deposit():
    zero_bank_account.deposit(30)
    assert zero_bank_account.balance == 80

def test_bank_transaction(zero_bank_account):
    zero_bank_account.deposit(200)
    zero_bank_account.withdraw(100)
    assert zero_bank_account

@pytest.mark.parametrize("deposited, withdrew , expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
]) 
def test_bank_transaction(zero_bank_account):
    zero_bank_account.deposit(200)
    zero_bank_account.withdraw(100)
    assert zero_bank_account

def test_insufficient_funds(Zero_bank_account):
    with pytest.raises(Insufficient):
      zero_bank_account.withdraw(200)
