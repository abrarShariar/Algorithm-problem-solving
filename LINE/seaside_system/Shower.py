class Shower:
    def __init__(self, user_age = 0, fee = 0):
        self.user_age = int(user_age)
        self.fee = fee
    
    def set_user_fee(self, fee):
        self.fee = fee

    def get_shower_fee(self):
        if self.user_age < 12:
            return 700
        elif self.user_age >= 12 and self.user_age < 15:
            return 1000
        elif self.user_age >= 15 and self.user_age < 18:
            return 1200
        elif self.user_age > 18:
            return 1500
