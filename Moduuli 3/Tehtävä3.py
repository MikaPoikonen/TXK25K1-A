print("Oletko mies vai nainen?")
sukupuoli =  input("Anna sukupuolesi: ")
hemoglobiini = float(input("Anna hemoglobiinisi (g/l): "))
if "mies" in sukupuoli and 0<=hemoglobiini<133:(print("Hemoglobiinisi on alhainen"))
elif "mies" in sukupuoli and 134<=hemoglobiini<195:(print("Hemoglobiinisi on normaali"))
elif "mies" in sukupuoli and 196<=hemoglobiini<999:(print("Hemoglobiinisi on korkea"))
elif "nainen" in sukupuoli and 0<=hemoglobiini<116:(print("Hemoglobiinisi on alhainen"))
elif "nainen" in sukupuoli and 117<=hemoglobiini<175:(print("Hemoglobiinisi on normaali"))
elif "nainen" in sukupuoli and 176<=hemoglobiini<999:(print("Hemoglobiinisi on korkea"))