import Encoder

enc = Encoder.Encoder(17,18)
val = enc.read()
while(True):
    temp = enc.read()
    if(val != temp):
        val = temp
        print(val)