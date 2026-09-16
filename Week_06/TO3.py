def gf2_solve(equations, n):
    matrix = [list(map(int, row)) for row in sorted(set(equations))
              if row != "0" * n]
    pivot = 0
    pivot_columns = []

    for col in range(n):
        selected = next(
            (r for r in range(pivot, len(matrix)) if matrix[r][col] == 1),
            None
        )

        if selected is None:
            continue
        matrix[pivot], matrix[selected] = matrix[selected], matrix[pivot]

        for r in range(len(matrix)):
            if r != pivot and matrix[r][col] == 1:
                matrix[r] = [a ^ b for a, b in zip(matrix[r], matrix[pivot])]

        pivot_columns.append(col)
        pivot += 1

    free = [c for c in range(n) if c not in pivot_columns]
    solution = [0] * n

    if not free:
        return "0" * n
    solution[free[0]] = 1

    for r in range(len(pivot_columns) - 1, -1, -1):
        col = pivot_columns[r]
        solution[col] = sum(
            matrix[r][c] * solution[c]
            for c in range(col + 1, n)
        ) % 2
    return "".join(map(str, solution))


equations = ["1100", "1010", "1000"]
recovered = gf2_solve(equations, 4)
print("Recovered secret:", recovered)