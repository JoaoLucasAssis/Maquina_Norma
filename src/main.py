# Instanciação dos registradores
A = B = C = D = E = F = G = H = 0

def add_one(register):
    globals()[register] += 1

def sub_one(register):
    globals()[register] -= 1

def is_zero(register):
    return globals()[register] == 0

def execute_instructions(instructions, next_instruction):
    while any(instruction[0] == next_instruction for instruction in instructions):
        for label, operation, register, next_labels in instructions:

            if label != next_instruction:
                break
            
            if operation == "add":
                add_one(register)
                next_instruction = next_labels[0]
            elif operation == "sub":
                sub_one(register)
                next_instruction = next_labels[0]
            elif operation == "zero":
                if is_zero(register):
                    next_instruction = next_labels[0]
                else:
                    next_instruction = next_labels[1]

            print(f"Operação {operation} no registrador {register}. Valor final: {globals()[register]}")
            print(f"Instrução atual: {label} | Próxima instrução: {next_instruction}")
            print("\n")

def initialize_registers():
    """
    Função para inicializar os registradores com valores determinados pelo usuário

    Execução:
    1.0 - Solicita ao usuário o número de registradores a serem inicializados.
    2.0 - Para cada registrador:
        2.1 - Solicita o nome do registrador e verifica se é válido.
        2.2 - Solicita o valor desejado para o registrador e verifica se é um número inteiro.
        2.3 - Atribui o valor à variável global correspondente ao registrador.
    3.0 - Retorna uma lista contendo os valores dos registradores e a instrução "M"
    """

    # 1.0
    num_registers = int(input("Quantos registradores você quer inicializar? "))
    while num_registers < 0:
        print("\x1b[2J\x1b[1;1H") # Faz a limpeza do terminal
        print("O número de registradores para inicializar não pode ser menor que zero.")
        num_registers = int(input("Quantos registradores você quer inicializar? "))
    
    register_values = []
    
    # 2.0
    for _ in range(num_registers):
        print("\x1b[2J\x1b[1;1H") # Faz a limpeza do terminal

        # 2.1
        register_name = input("Digite o nome do registrador (A, B, C, D, E, F, G, H): ").upper()
        while register_name not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            print("\x1b[2J\x1b[1;1H") # Faz a limpeza do terminal
            print("Nome de registrador inválido. Por favor, digite um dos registradores válidos.")
            register_name = input("Digite o nome do registrador (A, B, C, D, E, F, G, H): ").upper()
        
        # 2.2
        register_value = input(f"Digite o valor para o registrador {register_name}: ")
        while not register_value.isdigit():
            print("\x1b[2J\x1b[1;1H") # Faz a limpeza do terminal
            print("Valor inválido. Por favor, digite um número inteiro.")
            register_value = input(f"Digite o valor para o registrador {register_name}: ")
        register_value = int(register_value)
        register_values.append(register_value)

        globals()[register_name] = register_value # 2.3

    print("\x1b[2J\x1b[1;1H") # Faz a limpeza do terminal

    return [register_values, "M"] # 3.0

def validate_instruction(instruction):
    """
    Função para validar cada parte da instrução fornecida pelo usuário

    Execução:
    1.0 - Validação da estrutura da instrução:
        1.1 - Conversão do tipo primitivo de algumas partes da instrução
        1.2 - Criação de um array para os desvios condicionais e incondicionais
        1.3 - Validação de cada parte da instrução
    2.0 - Retorno da instrução modificada e validada
    """

    label = int(instruction[0])  # 1.1
    operation = instruction[1].lower()
    register = instruction[2].upper()
    next_labels = [int(instruction[i]) for i in range(3, 5) if len(instruction) > i]  # 1.1 / 1.2

    # 1.3
    operation_options = ['add', 'sub', 'zero']
    register_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    if operation not in operation_options:
        raise ValueError(f"Invalid operation: {operation}")
    if register not in register_options:
        raise ValueError(f"Invalid register: {register}")
    if next_labels == []:
        raise ValueError(f"This operation({operation}) must have a next label")
    if operation == "zero" and len(next_labels) <= 1:
        raise ValueError(f"This operation({operation}) must have 2 next labels")

    return [label, operation, register, next_labels] # 2.0

def read_instructions(input_file_name):
    try:
        with open(input_file_name, 'r') as file:
            instructions = [line.strip().split() for line in file.readlines()]

        if not instructions:
            print("\nError: File is empty.\n")
    except FileNotFoundError:
        raise FileNotFoundError("Error: File not found.")

    return instructions

def main():
    input_file_name = "input.txt"
    output_file_name = "output.txt"
    output = []

    instructions = read_instructions(input_file_name)

    for n, instruction in enumerate(instructions):
        instructions[n] = validate_instruction(instruction)

    output.append(initialize_registers())

    execute_instructions(instructions, instructions[0][0])

if __name__ == "__main__":
    main()