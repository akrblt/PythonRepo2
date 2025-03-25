from itertools import combinations, chain

def is_valid_sequence(seq):
    if len(seq) < 3:
        return False
    seq = sorted(seq)
    colors = [(c >> 4) & 0xF for c in seq]
    values = [c & 0xF for c in seq]
    return all(colors[0] == c for c in colors) and all(values[i] + 1 == values[i + 1] for i in range(len(values) - 1))

def is_valid_group(group):
    if len(group) < 3:
        return False
    colors = [(c >> 4) & 0xF for c in group]
    values = [c & 0xF for c in group]
    return len(set(values)) == 1 and len(set(colors)) == len(group)


def find_best(j1, game):
    best_j1, best_game = j1[:], game[:]
    min_hand_size = len(j1)
    
    def step1(temp_j1, temp_game):
        """Chercher dans la main si on peut former des séquences ou des groupes valides sans chevauchement"""
        new_combinations = []
        used_cards = set()
        
        for r in range(3, len(temp_j1) + 1):
            for combo in combinations(temp_j1, r):
                if set(combo).isdisjoint(used_cards) and (is_valid_sequence(combo) or is_valid_group(combo)):
                    new_combinations.append(list(combo))
                    used_cards.update(combo)
                    print("new_combinations", [[hex(card) for card in seq] for seq in new_combinations])



        
        for combo in new_combinations:
            for card in combo:
                if card in temp_j1:
                    temp_j1.remove(card)
            temp_game.append(combo)
        print("step1", temp_j1, temp_game)
    
    temp_j1 = j1[:]
    temp_game = [list(seq) for seq in game]
    
    step1(temp_j1, temp_game)
    #step2(temp_j1, temp_game)
    #step3(temp_j1, temp_game)
    #step4(temp_j1, temp_game)
    
    if len(temp_j1) < min_hand_size:
        best_j1, best_game = temp_j1, temp_game
        min_hand_size = len(temp_j1)
    
    return best_j1, best_game

# Exemple d'utilisation
j1 = [0x7, 0x9, 0xD, 0x1D, 0x21, 0x22, 0x27, 0x2B, 0x2C, 0x2D]
game = [
    [0x3, 0x4, 0x5, 0x6],
    [0x12, 0x13, 0x14],
    [0x1A, 0x1B, 0x1C],
    [0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A],
    [0x2A, 0x2B, 0x2C, 0x2D],
    [0x1, 0x11, 0x31],
    [0x2, 0x12, 0x22],
    [0x33, 0x34, 0x35]
]

print("ancienne main :",  [hex(card) for card in j1])
print("ancien plateau :", [[hex(card) for card in seq] for seq in game])
new_j1, new_game = find_best(j1, game)
print("Nouvelle main :", [hex(card) for card in new_j1])
print("Nouveau plateau :", [[hex(card) for card in seq] for seq in new_game])