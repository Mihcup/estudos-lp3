#desconto aplicado 
# Compras entre 0,01 e 9,99 - 0% de desconto 
# Compras entre 10 e 99,99 - 5% de desconto 
# Compras entre 100 e 499,99 - 10% de desconto 
# Compras iguais ou superiores a 500 - 15% de desconto 

totalCompra = float(input('Qual foi o total da compra?'))

if(totalCompra>=0.01 and totalCompra<=9.99):
    print('Compra:',totalCompra, '\nValor do desconto: 0%')
elif(totalCompra>=10 and totalCompra<=99.99):
     totalCompra= totalCompra - (totalCompra*0.05)
     print('Compra:',totalCompra, '\nValor do desconto: 5%')
elif(totalCompra>=100 and totalCompra<=499.99):
     totalCompra= totalCompra - (totalCompra*0.10)
     print('Compra:',totalCompra, '\nValor do desconto: 10%')
else: 
     totalCompra= totalCompra - (totalCompra*0.15)
     print('Compra:',totalCompra, '\nValor do desconto: 15%')
