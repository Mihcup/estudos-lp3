from Pessoa import Pessoa
p = Pessoa('Millena','SP3089762', 17)

print(p.getNome())
print(p.getIdade())
print(p.getProntuario())

p2 = Pessoa('Lala','SP3089762', p.getIdade())
print(p2.getIdade())