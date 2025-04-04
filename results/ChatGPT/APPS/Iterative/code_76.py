def can_construct_square(n, m, tiles):
    if m % 2 != 0:
        return "NO"
    
    # Check if any tile can form a square
    for tile_top, tile_bottom in tiles:
        if tile_top[1] == tile_bottom[0]:  # Check if top right == bottom left
            return "YES"
    
    return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        
        tiles = []
        for __ in range(n):
            tile_top = list(map(int, data[index].split()))
            index += 1
            tile_bottom = list(map(int, data[index].split()))
            index += 1
            tiles.append((tile_top, tile_bottom))
        
        result = can_construct_square(n, m, tiles)
        results.append(result)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()