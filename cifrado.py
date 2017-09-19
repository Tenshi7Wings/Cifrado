from string import ascii_letters

abecedario = []
dvorak = ["p","y","f","g","c","r","l","a","o","e","u","i","d","h","t","n","s","q",
		"j","k","x","b","m","w","v","z","P", "Y", "F", "G", "C", "R", "L", "A", "O", 
		"E", "U", "I", "D", "H", "T", "N", "S", "Q", "J","K","X","B","M","W","V","Z"," "]

for letter in ascii_letters:
	abecedario.append(letter)
abecedario.append(" ")

print("Encriptar una contrasena")
pass_unencrypted = input("Introduce tu contrasena a encriptar: ")
pass_encrypted = ""
position = 0
for letter in pass_unencrypted:
	abc_letter = pass_unencrypted[position]
	#print("letra del abecedario detectada")
	#print(abc_letter)
	abc_index = abecedario.index(abc_letter)
	#print("posicion en el formato abecedario")
	#print(abc_index)
	pass_encrypted = pass_encrypted+dvorak[abc_index]
	position = position + 1
	
print("Contrasena encriptada: \n", pass_encrypted)

print("Decifrar una contrasena")
pass_encrypted = input("Introduce tu contrasena a desencriptar: ")
pass_unencrypted = ""
position = 0
for letter in pass_encrypted:
	dvorak_letter = pass_encrypted[position]
	dvorak_index = dvorak.index(dvorak_letter)
	pass_unencrypted = pass_unencrypted+abecedario[dvorak_index]
	position = position + 1
	
print("Contrasena decifrada: \n", pass_unencrypted)