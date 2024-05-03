def validate_instruction(instruction):
    # 
    # Validação de cada parte da instrução
    # 
    # Execução:
    # 1.1 - Alteração do tipo primitivo de algumas partes
    # 1.2 - Criação de um array para os desvios condicionais e incondicionais
    # 1.3 - Validação de cada parte da instrução
    # 
    # 2.1 - Adição das partes validadas na instrução
    # 2.2 - Retornado instrução modificada e validada
    # 

    label = int(instruction[0]) # 1.1
    operation = instruction[1].lower()
    register = instruction[2].upper()
    next_labels = [int(instruction[i]) for i in range(3, 5) if len(instruction) > i] # 1.1 / 1.2

    operation_options = ['add', 'sub', 'zero']
    register_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    # 1.3
    if operation not in operation_options:
        raise ValueError(f"Invalid operation: {operation}")
    if register not in register_options:
        raise ValueError(f"Invalid register: {register}")
    if next_labels == []:
        raise ValueError(f"This operation({operation}) must have a next label")
    if operation == "zero" and len(next_labels) <= 1:
        raise ValueError(f"This operation({operation}) must have 2 next labels")

    instruction = [label, operation, register, next_labels] # 2.1

    return instruction # 2.2

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

    print(instructions)

    for instruction in instructions:
        instruction = validate_instruction(instruction)
        print(instruction)

if __name__ == "__main__":
    main()