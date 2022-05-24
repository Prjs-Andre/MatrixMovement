valid_movement = ["C", "D", "B", "E", "CIMA", "DIREITA", "BAIXO", "ESQUERDA"]
position = "00"


def create_matrix(tam):
    matrix = []
    for row in range(tam):
        matrix.append([])
        for column in range(tam):
            matrix[-1].append(0)

    matrix[0][0] = 1
    return matrix


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])


def move_robot(matrix, movement, current_position):
    global position

    if not validate_movement(current_position, matrix, movement):
        print("Movimento Inválido")
    else:
        matrix[int(current_position[0])][int(current_position[1])] = 0
        new_position = change_robot(movement, current_position)
        matrix[int(new_position[0])][int(new_position[1])] = 1
        print_matrix(matrix)
        position = new_position


def validate_movement(current_position, matrix, movement):
    if current_position[0] == "0" and movement == "C" or movement == "CIMA":
        return False
    if current_position[0] == str(len(matrix) - 1) and movement == "B" or movement == "BAIXO":
        return False
    if current_position[1] == "0" and movement == "E" or movement == "ESQUERDA":
        return False
    if current_position[1] == str(len(matrix[int(current_position[0])]) - 1) and \
            movement == "D" or movement == "DIREITA":
        return False
    return True


def change_robot(movement, current_position):
    if movement == "C" or movement == "CIMA":
        current_position = str(int(current_position) - 10)
    if movement == "D" or movement == "DIREITA":
        current_position = str(int(current_position) + 1)
    if movement == "B" or movement == "BAIXO":
        current_position = str(int(current_position) + 10)
    if movement == "E" or movement == "ESQUERDA":
        current_position = str(int(current_position) - 1)
    if len(current_position) > 1:
        return current_position
    else:
        # Movimento Na Primeira Linha
        return "0" + current_position


size = int(input("Insira o número de linhas/colunas. (Será gerada uma matriz quadrada a partir desse valor)\n"))

while type(size) != int or size < 2:
    size = input("Insira um valor válido para o tamanho da matriz.\n")

field = create_matrix(size)
print_matrix(field)


while True:
    mov = input("Para onde o personagem deve se mover? Ex: cima, baixo, direita, esquerda\n").upper()
    while mov not in valid_movement:
        mov = input("Insira um movimento válido. Ex: cima, baixo, direita, esquerda\n").upper()
    move_robot(field, mov, position)
