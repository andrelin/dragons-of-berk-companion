from util import parse_amount, get_timedelta


rarities = ['brute', 'champion', 'common' 'defender', 'exclusive', 'exiled', 'exotic',
            'premium', 'primal', 'rare', 'scarce', 'seedling', 'unique']


class DragonType(object):

    def __init__(self, name, breed, rarity, clz=None,
                 fish=None, fish_time=None,
                 wood=None, wood_time=None,
                 iron=None, iron_time=None,
                 iron_cost_fish=None, iron_cost_wood=None,
                 battle_type=None, battle_value=None,
                 battle_speciality=None):
        self.name = name
        self.breed = breed
        self.rarity = validate_rarity(rarity)
        self.clz = clz
        self.fish = parse_amount(fish) if fish else None
        self.fish_time = get_timedelta(fish_time) if fish_time else None
        self.wood = parse_amount(wood) if wood else None
        self.wood_time = get_timedelta(wood_time) if wood_time else None
        self.iron = parse_amount(iron) if iron else None
        self.iron_time = get_timedelta(iron_time) if iron_time else None
        self.iron_cost_fish = parse_amount(iron_cost_fish) if iron_cost_fish else None
        self.iron_cost_wood = parse_amount(iron_cost_wood) if iron_cost_wood else None

    def key(self):
        return ('{} {}'.format(self.name, self.breed)).replace(' ', '_')


class Dragon(DragonType):

    def __init__(self, lvl, **kwargs):
        super(self, kwargs)
        self.lvl = lvl


def validate_rarity(rarity):
    assert rarity.lower() in rarities
    return rarity
