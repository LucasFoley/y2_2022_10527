from basic_unit import *

wizard = Wizard()
healer = Shaman()
warrior = Warrior()

minion = EnemyMinion()
minion2 = EnemyMinion()
brute = EnemyBrute()

# test basic combat and hp
while wizard.is_alive() and minion.is_alive():
    wizard.combat(minion)
    if minion.hp > 0:
        print("enemy hp:", minion.hp)
        minion.combat(wizard)
        print("wizard hp:", wizard.hp)
print("enemy is dead")

# test apply stun status
while minion.check_status() is None:
    wizard.special_ability(minion)
    print(minion.check_status())

# test healer
wizard.hp -= 100
while wizard.hp < 150:
    print("Wizard HP:", wizard.hp)
    healer.special_ability(wizard)
    if wizard.hp > 150:
        wizard.hp = 150

# test positions and combat


