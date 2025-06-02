import re 

import re

class ValidarCPF:
    @staticmethod
    def validar_cpf(cpf):
        # Remove caracteres não numéricos
        cpf = re.sub(r'[^0-9]', '', cpf)
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        # Verifica se não são todos dígitos iguais
        if cpf == cpf[0] * 11:
            return False
        return True

class ValidarPlaca:
    @staticmethod
    def validar_placa(placa):
        # Placa antiga: ABC-1234
        padrao_antigo = r'^[A-Z]{3}-\d{4}$'
        # Placa Mercosul: ABC1D23
        padrao_mercosul = r'^[A-Z]{3}\d[A-Z]\d{2}$'
        if re.match(padrao_antigo, placa):
            return "Placa antiga válida"
        elif re.match(padrao_mercosul, placa):
            return "Placa Mercosul válida"
        else:
            return "Placa inválida"

# Testes (fora das classes)
if __name__ == "__main__":
    placas = []
    for placa in placas:
        print(f"{placa}: {ValidarPlaca.validar_placa(placa)}")
