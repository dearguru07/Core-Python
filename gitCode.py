import pywhatkit
from random2 import *

number="+91 9346860132"
otp=randint(000000,999999)
z=str(otp)
msg="this is ur OPT"+z
hour=15
mints=11

pywhatkit.sendwhatmsg(number,z,msg,hour,mints)

# import pywhatkit
# from random2 import *

# phone_number='+918688174622'
# otp=randint(000000,999999)
# z=str(otp)
# msg='OTP is'+z +'pls dont share any one'
# hour=15
# mints=10
# pywhatkit.sendwhatmsg(phone_number,msg,hour,mints)
