# https://www.youtube.com/watch?v=C8eA83f9uaQ&t=142s

grid = [line.strip() for line in open(0)]

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@": continue

        at_count = 0

        # Check surrounding cells (3×3 area)        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        at_count += 1

        if at_count <= 4:
            total += 1
print(total)
