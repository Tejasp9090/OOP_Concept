# Exception Handling

"""try:


    #print(10/0)
    print(10/u)

except Exception as msg:
    print('Error:',msg)
else:
    print('No Exception ...continue with ur process')

finally:
    print('Zukega Nahi sala')

------------------------------------------------
"""


"""balance = 5000
try:
    amount = float(input('Enter the amount to send:'))

    if amount > balance:
        raise ValueError('Insufficient Balance')
    
    # if above condition  is nt True then continue
    balance -= amount
    print('Payment Sucessfull')
    print('Remaining Balance:Rs.',balance)
    
except ValueError as msg:
    print('Payment Failed:',msg)
    -----------------------------------------
    
"""

"""
Assignment:
1. Login System- Wrong Password
2. Movie Ticket booking- Seat allocation
3. Online shopping- Product out of stock
4. Mobile Recharge- min Rs. 10
5. ATM - Daily withdrawal limit

"""

# Ecommerce/Food delivery
serviceable_pincodes = [411001,411002,411003]
try:
    pincode = int(input('Enter the Pincode:'))

    if pincode not in serviceable_pincodes:
        raise Exception('Delivery not available in your location')
    
    print('Delivery Available')

except ValueError:
    print('Pincode must be a number')

except Exception as msg:
    print(msg)
