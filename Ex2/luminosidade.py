import re

with open("brilcalc.log", "r") as file:
    	luminosidade = file.read()
summary = luminosidade.split("#Summary:")[-1]
desnecessariamente_grande = r"\|\s*([\d\.]+)\s*\|\s*([\d\.]+)\s*\|\s*([\d\.]+)\s*\|\s*([\d\.]+)\s*\|\s*([\d\.]+)\s*\|\s*([\d\.]+)\s*\|"

achou = re.search(desnecessariamente_grande, summary)
	
if achou:	
	pb = float(achou.group(6))
	fb = pb/1000
	
	print(f"{fb:.1f} fb^-1")


    
