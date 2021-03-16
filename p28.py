def p28(layer_count: int) -> int:
    # The first layer (n=0) is just the single number 1
    # Let C(n,m) = a corner of a layer, starting south east clockwise
    # e.g. C(1,1) = 3; C(1,2) = 5; C(1,3) = 7; C(1,4) = 9
    # It can be shown that C(n,m) = 2n(2(n-1)+m)+1
    # Let D(n) = sum of corners in layer
    #          = C(n,1) + C(n,2) + C(n,3) + C(n,4)
    #          = 2n(2n-1) + 1 + 2n(2n) + 1 + 2n(2n+1) + 1 + 2n(2n+2) + 1
    #          = 2n(2n-1 + 2n + 2n+1 + 2n+2) + 4
    #          = 2n(8n+2) + 4
    #          = 4n(4n+1) + 4
    #          = 16n^2 + 4n + 4
    #          = 4(4n^2 + n + 1)
    # e.g. D(1) = 24; D(2) = 76; D(3) = 160; D(4) = 276
    # Let S(n) = sum of layers (not counting n=0)
    #          = D(1) + D(2) + ... + D(n)
    # e.g. S(1) = 24; S(2) = 100; S(3) = 260; S(4) = 536
    # Assume S(n) is in the form: an^3 + bn^2 + cn + d
    # Solve system of linear equations:
    #   S(1) = a + b + c + d = 24
    #   S(2) = 8a + 4b + 2c + d = 100
    #   S(3) = 27a + 9b + 4c + d = 260
    #   S(4) = 64a + 16b + 4c + d = 536
    # Gives: a = 16/3; b = 10; c = 26/3; d = 0
    # So S(n) = (16/3)n^3 + 10n^2 + (26/3)n
    #         = (2n/3)(8n^2 + 15n + 13)
    # Then we need to +1 for that central single 1 (n=0 layer)

    if layer_count == 1: return 1
    n = layer_count - 1
    return 2*n * (8*n*n + 15*n + 13) // 3 + 1

if __name__ == '__main__':
    print(p28(1))
    print(p28(2))
    print(p28(3))
    print(p28(501))