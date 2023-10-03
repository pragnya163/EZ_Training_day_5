'''sum=0
for i in range(1,10,1):
    for j in range(1,10,1):
        sum
print(sum)'''
def generate_magic_square():
    n = 3  # Size of the magic square (3x3)
    magic_square = [[0] * n for _ in range(n)]

    # Initialize the starting position for 1
    i, j = 0, n // 2

    # Fill in the magic square with numbers from 1 to n^2
    for num in range(1, n ** 2 + 1):
        magic_square[i][j] = num
        i -= 1
        j += 1

        # Wrap around if we go out of bounds
        if i < 0:
            i = n - 1
        if j == n:
            j = 0

        # Check if the next cell is already occupied
        if magic_square[i][j] != 0:
            i += 1
            j -= 2

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        for num in row:
            print(num, end='\t')
        print()

if __name__ == "__main__":
    magic_square = generate_magic_square()
    print("3x3 Magic Square:")
    print_magic_square(magic_square)

