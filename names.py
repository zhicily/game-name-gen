import random
import string

def nameGen(numbers=False):
    prefixes = ['AL', 'AM', 'AN', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AZ', 'A_',
                'BE', 'BI', 'BL', 'BO', 'BR', 'BU', 'B_',
                'CH', 'CI', 'CL', 'CO', 'CR', 'CU', 'CY', 'C_',
                'DI', 'DE', 'DO', 'DR', 'DU', 'DY',
                'ES', 'ET', 'EV', 'EX', 'EY', 'EZ',
                'FI', 'FL', 'FO', 'FR', 'FU',
                'GE', 'GH', 'GI', 'GL', 'GO', 'GP', 'GR', 'GU',
                'HE', 'HI', 'HO', 'HU',
                'JE', 'JH', 'JI', 'JO', 'JU',
                'KE', 'KI', 'KL', 'KO', 'KR', 'KU', 'KY',
                'LE', 'LI', 'LL', 'LO', 'LU', 'LY', 'L_',
                'MA', 'ME', 'MI', 'MO', 'MR', 'MS', 'MU', 'MY',
                'NE', 'NI', 'NO', 'NU', 'NY',
                'PE', 'PI', 'PL', 'PO', 'PR', 'PT', 'PU', 'PY',
                'RE', 'RI', 'RO', 'RU', 'RY',
                'SC', 'SE', 'SH', 'SI', 'SK', 'SL', 'SM', 'SN', 'SO', 'SP', 'SQ', 'SS', 'ST', 'SU', 'SW', 'SY', 'S_',
                'TH', 'TI', 'TO', 'TR', 'TU', 'TW', 'TY', 'T_',
                'WO',
                '_L', '_M', '_P', '_R', '_S', '_T', '__']

    # 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    # 1
    consanants = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    # 2
    substr = ['th', 'ch', 'sh', 'pr', 'br', 'tr', 'fr', 'gr', 'kr', 'cr', 'gh', 'qu', 
            'st', 'sp', 'sn', 'sm', 'sk', 'sc', 'sl', 'pl', 'fl', 'gl', 'kl', 'cl', 
            'bl', 'wr', 'sw', 'tw', 'gh', 'ph']

    # 3
    suffixes = ['ay', 'ie']

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    length = random.randint(7, 10)
    num_letters = length

    has_num = random.randint(0, 1)

    if numbers == True and has_num == 1:
        num_letters = random.randint(4, length - 1)
    
    num_nums = length - num_letters

    name = prefixes[random.randint(0, len(prefixes) - 1)] + vowels[random.randint(0, len(vowels) - 1)]

    assert(len(name) == 3)

    new_substr = -1

    while len(name) < num_letters:
        if new_substr == 1 or new_substr == 2:
            curr_substr = 0
        elif num_letters - len(name) > 1:
            curr_substr = random.randint(0, 2)
        else:
            curr_substr = random.randint (0, 1)

        assert(curr_substr != 3)

        if num_letters - len(name) == 2:
            has_suffix = random.randint(0, 1)

            if has_suffix == 1:
                name = name + suffixes[random.randint(0, len(suffixes) - 1)]

        else:
            if curr_substr == 0:
                name = name + vowels[random.randint(0, len(vowels) - 1)]
                new_substr = 0
            elif curr_substr == 1:
                name = name + consanants[random.randint(0, len(consanants) - 1)]
                new_substr = 1
            elif curr_substr == 2: 
                name = name + substr[random.randint(0, len(substr) - 1)]
                new_substr = 2
        
    if num_nums > 1:
        underscore = random.randint(0, 1)

        if underscore == 1:
            name = name + '_'
    
    while len(name) < length:
        name = name + nums[random.randint(0, len(nums) - 1)]

    name = name.lower()
    name = string.capwords(name)

    return name