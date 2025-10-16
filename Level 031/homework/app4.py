'''4) დაწერე პროგრამა, რომელიც მომხმარებლისგან შეიტანს სტუდენტის მიღებულ ქულას (0-დან 100-მდე) და გამოიტანს 
შესაბამის ნიშანს დამოკიდებულს ქულაზე:
ქულა        ნიშანი
90 – 100      A
80 – 89       B
70 – 79       C
60 – 69       D
0 – 59        F'''

score = int(input("Enter your score :"))
if score >= 90 and score <= 100:
  print("A")
elif score >= 80 and score <= 89:
  print("B")
elif score >= 70 and score <= 79:
  print("C")
elif score >= 60 and score <= 69:
  print("D")
elif score >= 0 and score <= 59:
  print("F")