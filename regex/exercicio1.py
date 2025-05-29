# 1. Crie uma expressão regular para validar números de cartão de crédito

import re

def validar_cartao_credito(cartao):
    pattern = r'd{4}\d{}'