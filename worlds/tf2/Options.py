from Options import Toggle, DefaultOnToggle, Choice, Range, DeathLink, PerGameCommonOptions, OptionGroup, OptionSet

class ShuffleMaps(Choice):
    """Shuffles maps to be played on.
    
    - **Stock Only:** Maps from Valve's original lineup.
    - **Community Only:** Maps only created by the TF2 Community are selected.
    - **Random Selected:** Maps from both Valve and the Community are selected, based on the provided selection.
    - **Completely Random:** Maps from both Valve and the Community are selected at random.
    - **All:** All the maps within the randomizer, including Valve and Community maps.
    """
    display_name = "Shuffle Maps"
    option_stock = 0
    option_comm = 1
    option_sel = 2
    option_ran = 3
    option_all = 4

class ShuffleMissions(Choice):
    """Shuffles the missions to be played on. 
    
    - **Stock Only:** Missions from Valve's original lineup.
    - **Community Only:** Missions from TF2 Community, mainly from Potato.tf or Moonlight.tf
    - **Random Selected:** Maps from both Valve and the Community, based on the provided selection.
    - **Completely Random:** Maps from both Valve and the Community that are selected from random.
    """
    display_name = "Shuffle Missions"
    option_stock = 0
    option_comm = 1
    option_sel = 2
    option_ran = 3

class RandomizeMissionCount(Range):
    """The number of missions required to be completed for the seed can be adjusted.
    """
    display_name = "Missions Required Count"
    range_start = 1
    range_end = 32
    default = 6
    
class ShuffleWaves(Choice):
    """Shuffles the waves for each mission into the item pool.
    
    - **Off:** The waves are not shuffled.
    - **On:** The waves are shuffled and a random wave can be received.
    - **Progression:** The waves are shuffled and each wave for a mission received progresses.
    """
    display_name = "Shuffle Waves"
    option_off = 0
    option_on = 1
    option_prog = 2

class LockClasses(Toggle):
    """When enabled, all but a select few classes will be available to each player.
    """
    display_name = "Lock Classes"

class LockClassesCounter(Range):
    """The number of classes locked. Lock Classes must be enabled.
    """
    display_name = "Number of Locked Classes"
    range_start = 1
    range_end = 8
    default = 3

class ShuffleUpgrades(Choice):
    """Shuffles the upgrades in the item pool.

    - **Off:** Upgrades are not shuffled.
    - **Shared:** Shared upgrades, such as reload speed and health on kill are shuffled.
    - **Class:** All the upgrades for a single class are shuffled as a single item.
    - **Weapon Slot:** All the upgrades for a weapon slot i.e. Primary are shuffled as a single item.
    - **Weapon:** All the upgrades for a single weapon are shuffled as a single item.
    - **All:** All the upgrades as a single item.
    - **Split:** All the upgrades and increments are shuffled in the item pool.
    - **Singular:** All the upgrades are shuffled in the item pool.
    """
    display_name = "Shuffle Upgrades"
    option_off = 0
    option_shared = 1
    option_class = 2
    option_weapon_slot = 3
    option_weapon = 4
    option_all = 5
    option_split = 6
    option_single = 7

class ShuffleRobots(Choice):
    """Shuffles the robot "souls" in the item pool. Waves and missions may not be completable until you obtain them.

    - **Off:** Souls are not shuffled.
    - **Class Based:** Souls based on classes are shuffled, 10 in total including the tank soul.
    - **Type:** Souls based on the same template are shuffled, i.e. Deflector Heavies (regular and giant) or Rapid Fire Demomen.
    - **Individual:** Souls based on a template are shuffled.
    - **Bosses and Tanks Only:** Only Boss and Tanks souls are shuffled.
    """
    display_name = "Shuffle Robot Souls"
    option_off = 0
    option_class = 1
    option_type = 2
    option_ind = 3
    option_bosstank = 4

class LockWeaponSlots(Choice):
    """Locks weapon slots, such as primary, secondary, etc., until the slot item is acquired.

    - **Off:** All weapon slots are accessible.
    - **Primary:** Start with only primary weapons. Inaccessible to Spy.
    - **Secondary:** Start with only secondary weapons.
    - **Melee:** Start with only melee weapons.
    - **PDA:** Starts with only PDAs. Only applicable to Engineer and Spy.
    - **Sapper:** Start with sapper only. Only applicable to Spy.
    """
    display_name = "Lock to Weapon Slot"
    option_off = 0
    option_prime = 1
    option_second = 2
    option_melee = 3
    option_pda = 4

class LockWeapons(Choice):
    """Locks weapons, both unlockables and/or stock weapons.

    - **Off:** All weapons are available.
    - **Stock Only:** All stock weapons are accessible.
    - **Unlockable Only:** All unlockable weapons are accessible.
    - **Random:** Available weapons are randomly accessible.
    """
    display_name = "Lock Weapons"
    option_off = 0
    option_stock = 1
    option_comm = 2
    option_rand = 3

class WeaponCount(Range):
    """The number of weapons that are obtained at the start of the seed.
    """
    display_name = "Starting Weapon Count"
    range_start = 1
    range_end = 32
    default = 9

class ShuffleCanteens(Toggle):
    """Shuffles the canteen slot and different canteens into the item pool.
    """
    display_name = "Shuffle Canteens"

class EnableBonuses(Toggle):
    """Enables the bonuses as 2 checks for each wave into the item pool.
    """
    display_name = "Enable End of Wave Bonuses"

class AddTraps(Toggle):
    """Adds Traps into the item pool. These are based on the Roll the Dice plugin and addcond command.
    """
    display_name = "Add Traps"

class AddTrapTypes(OptionSet):
    """Choose all the traps to be used.
    """
    display_name = "Trap Types"
    valid_keys = {
        "Blind Trap",
        "Bomb Trap",
        "Cursed Trap",
        "Death Trap",
        "Ice Trap",
        "Low Gravity Trap",
        "Low Health Trap",
        "Recall Trap",
        "Snail Trap",
        "Strong Gravity Trap",
        "Taunt Trap",
        "Vampire Trap",
    }

@dataclass
class TeamFortress2Options(PerGameCommonOptions):
    # Maps, Missions and Waves
    map_shuffle: ShuffleMaps
    mission_shuffle: ShuffleMissions
    mission_count: RandomizeMissionCount
    wave_shuffle: ShuffleWaves

    # Classes, Weapons, Upgrades and Canteens
    class_locker: LockClasses
    class_count: LockClassesCounter
    weapon_shuffle: LockWeapons
    weapon_slot_shuffle: LockWeaponSlots
    canteen_shuffle: ShuffleCanteens
    upgrades_shuffle: ShuffleUpgrades

    # Robots
    robot_shuffle: ShuffleRobots

    # Death Link and Traps
    death_link: DeathLink
    traps: AddTraps
    trap_types: AddTrapTypes

    option_groups = [
        OptionGroup("Map", [
            ShuffleMaps,
            ShuffleMissions,
            RandomizeMissionCount,
            ShuffleWaves
        ]),
        OptionGroup("Class", [
            LockClasses,
            LockClassesCounter,
            LockWeapons,
            LockWeaponSlots,
            ShuffleCanteens
        ])
    ]