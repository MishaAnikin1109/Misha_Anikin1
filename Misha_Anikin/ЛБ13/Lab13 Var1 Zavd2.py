from telephone import Telephone

phone = Telephone("123-456-7890", "Poco X3 PRO")

phone.call("Іван", "098-111-2222")
phone.call("Марія", "099-333-4444")

phone.show_info()

phone.delete_call()

phone.show_info()