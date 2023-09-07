indeks = {   
    "Celsius   " : "c",
    "Fahrenheit" : "f", 
    "Kelvin    " : "k"
}
print("======Indeks Satuan Skala Suhu======")
for i in indeks:
    print("Satuan suhu :", i, "\t Indeks : ", indeks[i])

suhu = float(input("Masukkan suhu :' "))
satuan = input("Masukan indeks satuan skala suhu : ")

if (satuan == "c"):
    print (suhu, "derajat celsius : ")
    print ("Fahrenheit = ", (suhu*9/5)+32,"derajat")
elif (satuan == "f"):
    print (suhu, "derajat fahrenheit : ")
    print ("celsius = ", (5/9)+(suhu-32),"derajat")
elif (satuan == "k"):
    print (suhu, "derajat kelvin : ")
    print ("celsius = ", suhu-273,"derajat")