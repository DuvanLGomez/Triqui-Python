import random
from time import sleep

# Imprime por consola el tablero
def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
    print("-------------")

# Función que toma el movimiento del jugador X
def get_player_move(board):
    while True:
        move = input("Ingrese la fila y la columna (ejemplo 1,1): ")
        row, column = move.split(",")
        row = int(row) - 1
        column = int(column) - 1
        if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == "-":
            return row, column
        else:
            print("Movimiento inválido. Intente de nuevo.")

# Verifica si con el movimiento se ha ganado
def check_winner(board):
    # Validar líneas verticales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]
    # Validar líneas horizontales
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]
    # Validar líneas diagonales
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        return board[1][1]
    
    # Si no hay ganador
    return None

def main():
    print("Tres en línea")

    # Inicializamos el tablero
    board = [["-", "-", "-"] for _ in range(3)] 

    # Imprimir el tablero al inicio
    print_board(board)

    while True:
        # Obtener el movimiento del jugador
        row, column = get_player_move(board)
        board[row][column] = "X"
        print("Jugador X hizo su movimiento:")
        sleep(1.5)
        print_board(board)

        winner = check_winner(board)
        if winner is not None:
            break

        # Movimiento del computador 
        computer_row = random.randint(0, 2)
        computer_column = random.randint(0, 2)

        while board[computer_row][computer_column] != "-":
            computer_row = random.randint(0, 2)
            computer_column = random.randint(0, 2)
        
        # Pintar la jugada del computador
        board[computer_row][computer_column] = "O"
        print("Computadora O hizo su movimiento:")
        sleep(1.5)
        print_board(board)

        winner = check_winner(board)
        if winner is not None:
            break

    print(f"El jugador {winner} es el ganador!")

if __name__ == "__main__":
    main()