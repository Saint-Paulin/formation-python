#!/usr/bin/python3.6
var = "abc#a3#def#gh#e111#toto"
var2 = var.split("#")
results = []
#print(var2)
for mot in var2:
	if mot[-1] in "0123456789":
		results.append(mot)
var4 = ";".join(results)
print(var4)
