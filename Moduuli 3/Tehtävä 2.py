print ("Anna hyttiluokka LUX,A,B tai C")
hytti = input (str ("hyttiluokka"))
if "LUX" in hytti: (print("LUX on parvekkeellinen hytti yläkannella."))
elif "A" in hytti: (print("A on ikkunallinen hytti autokannen yläpuolella."))
elif "B" in hytti: (print("B on ikkunaton hytti autokannen yläpuolella."))
elif "C" in hytti: (print("C on ikkunaton hytti autokannen alapuolella."))
else: (print("Virheellinen hyttiluokka."))

