def password_check(func):
    def verify_passwd(pin, *amt):
        if pin == 123:
            res = func(amt)
            print(res[0])
    return verify_passwd
        
@password_check
def depsite_money(amount):
    return amount

depsite_money(123, 500)
