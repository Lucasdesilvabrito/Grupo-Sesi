def PiValue(x): #X =  A numero de termos, quanto mais tiver mais preciso o resultado é 
    soma = 0 #Valor de pi que vai ser acrescido depois 
    
    for i in range(x): #aqui ele soma ate o termo informado e acresce no soma 
        soma += ((-1)**i) / (2*i + 1)  #aqui acontece a inversao dos sinais e a a soma do numero impar escolhido no input dos termos

    return 4 * soma # Multiplica tudo por 4 igual na formula 


ntermos = int(input("Insira o numero de termos que vc deseja: ")) #usuario esoclher o tanto de termos

print(PiValue(ntermos)) #print valor de pi