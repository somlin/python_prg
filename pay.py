hours = input("Enter hours: ")
rate = input("Enter rate: ")



def get_pay(hours,rate):
    try:
        if int(hours)>40:
            pay = (40 * float(rate)) + (1.5 * float(rate) * (float(hours)-40))
            print (pay)
        else:
            pay = float(hours) * float(rate) 
            print (pay)
    except:
        print("Error,please a number")

get_pay(hours,rate)
