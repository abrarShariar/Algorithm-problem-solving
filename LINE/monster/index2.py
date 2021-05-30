import sys

def main(argv):
    level_start = int(argv[0])
    level_end = int(argv[1])
    total_levels = (level_end - level_start) + 1
    spell_count = int(argv[2])

    spells = set()
    for i in range(1, spell_count + 1):
        spells.add(int(argv[2 + i]))
    
    all_spells = set()
    for spell in spells:
        if spell >= level_start and spell <= level_end:
            # generate all the multiples
            multiplier = 1
            running_spell = spell
            while running_spell <= level_end:
                all_spells.add(running_spell)
                running_spell = running_spell * multiplier
                multiplier += 1
    
    remaining_monsters = total_levels - len(all_spells)
    print(remaining_monsters)

if __name__ == '__main__':
    main(sys.argv[1:])
