from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

exemplo_cnpj = "00394460005887"
exemplo_cpf = "01234567890"
documento = CpfCnpj(exemplo_cnpj, "cnpj")
print(documento)