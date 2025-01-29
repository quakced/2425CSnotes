def print_grid(rows,cols):
    for i in range(rows):
        for j in range(cols):
            print(f"{i * cols + j +1:2}", end=" ")
rows=10
cols=10
print_grid(rows,cols)