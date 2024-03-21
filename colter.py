def parse_input():
    lines = []
    while True:
        cur = input()
        if not cur:
            break
        lines.append(cur)
    input_data = lines
    first_row = list(map(int, input_data[0].split()))
    W, H, GN, SM, TL = first_row
    
    golden_points = set()
    silver_points = {}
    tile_id_to_cost = {}
    tile_id_to_remaining = {}
    
    current_line = 1
    
    # Parse Golden Points
    for _ in range(GN):
        gx, gy = map(int, input_data[current_line].split())
        golden_points.add((gx, gy))
        current_line += 1
    
    # Parse Silver Points
    for _ in range(SM):
        sx, sy, ss = map(int, input_data[current_line].split())
        silver_points[sx, sy] = ss
        current_line += 1
    
    # Parse Tiles
    for _ in range(TL):
        parts = input_data[current_line].split()
        tile_id = parts[0]
        tc, tn = map(int, parts[1:])
        tiles.append((tile_id, tc, tn))
        current_line += 1
    
    return {
        'grid_size': (W, H),
        'golden_points': golden_points,
        'silver_points': silver_points,
        'tiles': tiles,
    }

# Assuming the input is provided as described, call the function to parse it.
# parsed_data = parse_input()
# print(parsed_data)

