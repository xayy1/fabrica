#Lista inicial
nomes = ["Joaquim","Maria","ana"]
print("Lista inicial:",nomes)
print("-"*30)

#Adicionando elementos
nomes.append("Carlos") #Adicional ao final 
print("Após append ", nomes)
print("-"*30)

nomes.insert(1,"Fernanda") #Insere "Fernanda" na posição 1
print("Após insert:", nomes)
print("-"*30)

#modificando elementos
nomes[2] = "Paulo" # Modifica o elementos do índice 2
print("Após modificação: ", nomes)
print("-"*30)

#Removendo elementos 
del nomes[3] # remove o elemento no índice 3 
print("Após del: ", nomes)
print("-"*30)

nomes.remove("paulo") # Remove a primeira ocorrêcia de "Paulo"
print("Após remove:", nomes)
print("-"*30)

removido = nomes.pop(2) #Remove e retorna o elemento o índice 2 
print(f"Após pop (removido '{removido}'):", nomes)
print("-"*30)

nomes.clear() # Esvazia a lista
print("Após clear:",nomes)
print("-"*30)
