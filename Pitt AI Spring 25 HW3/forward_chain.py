from Propositional_KB_agent import *

def forwardchain(KB,theorem):
    newTheorem = True
    while newTheorem == True:
        if KB.is_in_FB(theorem):
            print("success")
            return True
        newTheorem = False
        for rule in KB.RB:
            if not KB.is_in_FB(rule.then_part):
                condition = True
                for requirement in rule.cond_part:
                    if not KB.is_in_FB(requirement): # if a parameter fails
                        condition = False
                if condition == True:
                    KB.add_fact(rule.then_part)
                    newTheorem = True
                    print_rule(rule)
                    print_fact(rule.then_part)
    print("false")
    return False

def print_rule(rule):
    print(rule.name)
    print('If:', rule.cond_part)
    print('Then:', rule.then_part)
    print(' ')

#prints fact base       
def print_fact(fact):
    print(fact)

# rules for the animal identification problem        
init_RB=[]
init_RB.append(Rule('R1',['has_hair'],'is_a_mammal'))
init_RB.append(Rule('R2',['gives_milk'],'is_a_mammal'))
init_RB.append(Rule('R3',['has_feathers'],'is_a_bird')) 
init_RB.append(Rule('R4',['flies','lays_eggs'],'is_a_bird')) 
init_RB.append(Rule('R5',['is_a_mammal','eats_meat'],'is_a_carnivore')) 
init_RB.append(Rule('R6',['is_a_mammal','has_pointed_teeth','has_claws','the_animals_eyes_point_forward'],'is_a_carnivore'))
init_RB.append(Rule('R7',['is_a_mammal','has_hoofs'],'is_an_ungulate'))
init_RB.append(Rule('R8',['is_a_mammal','chews_cud'],'is_an_ungulate'))
init_RB.append(Rule('R9',['is_a_mammal','chews_cud'],'is_even-toed'))
init_RB.append(Rule('R10',['is_a_carnivore','has_a_tawny_color','has_dark_spots'],'is_a_cheetah'))
init_RB.append(Rule('R11',['is_a_carnivore', 'has_a_tawny_color', 'has_black_stripes'],'is_a_tiger'))
init_RB.append(Rule('R12',['is_an_ungulate','has_long_legs','has_a_long_neck','has_a_tawny_color','has_dark_spots'],'is_a_giraffe'))
init_RB.append(Rule('R13',['is_an_ungulate', 'has_a_white_color','has_black_stripes'],'is_a_zebra'))
init_RB.append(Rule('R14',['is_a_bird','does_not_fly','has_long_legs','has_a_long_neck','is_black_and_white'],'is_an_ostrich'))
init_RB.append(Rule('R15',['is_a_bird','does_not_fly','swims','is_black_and_white'],'is_a_penguin'))
init_RB.append(Rule('R16',['is_a_bird','is_a_good_flyer'],'is_an_albatross'))

# facts/propositions known to be true for the animal we want to identify
init_FB=['gives_milk','chews_cud','has_long_legs','has_a_long_neck','has_a_tawny_color','has_dark_spots']

KBase=KB(init_RB,init_FB)

# here are theorems to prove
theorem1='is_a_giraffe'
theorem2='is_a_penguin'
theorem3='is_a_mammal'
theorem4='has_a_tawny_color'
theorem5='is_a_bird'

forwardchain(KBase, theorem2)