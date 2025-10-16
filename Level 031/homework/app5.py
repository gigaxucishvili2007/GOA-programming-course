'''5) მომხმარებელს შემოატანინეთ ტემპერატურა ცელსიუსში.

თუ ტემპერატურა 0-ზე ნაკლებია დააბრუნეთ “Today is very cold! Wear warm clothes 💙”,

თუ 0–30 შორისაა → დაპრინტეთ “Today is a really nice weather 🥰”,

თუ 30-ზე მეტია → დაპრინტეთ “Today is very hot! Drink plenty of water 🔥”.'''

temperature = int(input("Enter the temperature in Celsius :"))
if temperature <= 0:
  print("Today is very cold! Wear warm clothes 💙")
elif temperature >= 0 and temperature <= 30:
  print("Today is a really nice weather 🥰")
elif temperature > 30:
  print("Today is very hot! Drink plenty of water 🔥")