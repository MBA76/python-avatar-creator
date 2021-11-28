import pagan


img=pagan.pagan.Avatar
a=-1
while a<0:
    inpt = input("İsim Girin:")
    secim = input("Varyasyon(1-2-3-4-5):")

    if secim == "1":
        img = pagan.Avatar(inpt, pagan.SHA1)

        a = 1
    elif secim == "2":
        img = pagan.Avatar(inpt, pagan.SHA224)
        a = 2
    elif secim == "3":
        img = pagan.Avatar(inpt, pagan.SHA256)
        a = 3
    elif secim == "4":
        img = pagan.Avatar(inpt, pagan.SHA384)
        a = 4
    elif secim == "5":
        img = pagan.Avatar(inpt, pagan.SHA512)
        a = 5
    else:
        print("Hatali Tuslama yaptiniz.")
        a = -1

img.show()

outpath  = 'avatar/'
filename = inpt+ secim +".png"
img.save(outpath,filename)
print("end")