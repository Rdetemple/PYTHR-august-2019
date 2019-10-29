defense = True
offense = True
rule_changes = True

def set_offense():
    offense = True
    print('offense is', offense)


def set_defense():
    defense = True
    print('defence is', defense)

def set_rule_changes():
    rule_changes = True

set_offense()
set_defense()



if offense and defense:

    set_rule_changes()


print('How are the Jags doing?', rule_changes)
print('We have offense:', offense)
print('We have defense:', defense)
print('We have some rule changes:', rule_changes)

if offense and defense and rule_changes:
    print("We're going to the Super Bowl!")
else:
    print("I can't predict the future, but no, the Jaguars will never win the Super Bowl.")
