print ("----------Program BMI----------")

Tinggi = float(input ("tinggi kamu berapa ? "))
Berat = float(input ("Berat kamu berapa ? "))

BMI = (Berat / Tinggi ** 2)

# Keterangan
# Di bawah 17,0 = Kurus, kekurangan berat badan berat
# 17,0 - 18,4 = Kurus, kekurangan berat badan ringan
# 18,5 – 25,0 = Normal
# 25,1 – 27,0 = Gemuk, kelebihan berat badan tingkat ringan
# Lebih dari 27 = Gemuk, kelebihan berat badan tingkat berat

print(BMI)

if BMI < 17:
  print("Kurus, kekurangan berat badan berat")
elif BMI < 18.5:
  print("Kurus, kekurangan berat badan ringan")
elif BMI < 25:
  print("Normal")
elif BMI < 27.1:
  print("Gemuk, kelebihan berat badan tingkat ringan")
else:
  print("Gemuk, kelebihan berat badan tingkat berat")
