#!/usr/bin/python
from __future__ import print_function
import random
import locale
import colorama
from colorama import Fore, Back, Style


# set locale and format for int

locale.setlocale(locale.LC_ALL, 'en_US')

# you need python version 2.7 (not 3) to run this program. 

	# # # V A L U E S  S T A R T S # # #

# input cost

paddys_cost = 1400 				# rs
urea_cost =	40 					# rs
DAP_cost =	20 					# rs
MOP_cost =	18 					# rs
compost_cost = 5 				# rs
greenf_cost = 4 				# rs
dryf_cost =	1.5 				# rs
cattlef_cost = 5 				# rs
mineral_cost = 20 				# rs
labour_cost= 120 				# rs

# credit cost

credit_cost = 0.04 				# %
MFI_cost = 0.24 				# %
informal_cost = 0.40		 	# %
risk_cost = 0.01				# %

# rate factors	

paddy_rate = 1400 				# rs
straw_rate = 1 					# rs
cowmilk_rate = 20 				# rs
goatmilk_rate = 10 				# rs
babygoat_rate = 2000 			# rs
compost_rate = 3 				# rs
employment_rate = 150 			# rs
SHGcontribution_rate = 25 		# rs

# asset valuation 1

land_value = 100000 			# rs per acre
cow_value =	40000 				# rs per cow
goat_value = 20000 				# rs per goat

# asset valuation 2
					
weeder_value = 1500 			# rs per unit
seeder_value = 6000 			# rs per unit
transplanter_value = 7500 		# rs per unit
harvester_value = 100000 		# rs per unit
irrigation_value = 5000 		# rs per unit
			
# infrastructure cost 		

storage_shed = 4000 			# rs per unit
livestock_shed = 4000 			# rs per unit
			
# seed requirement 		

SRIpaddy_min = 2 				# kg per acre
			
# fertilizer requirement	

urea_min = 8 					# kg per acre
DAP_min	= 35					# kg per acre
MOP_min	= 10					# kg per acre
compost_min	= 500				# kg per acre
			
# animal feed

greenf_min = 20 				# kg per cow
dryf_min = 2 					# kg per cow 
cattlef_min = 9 				# kg per cow
mineral_min = 0.15 				# kg per cow

# labour factors 

family_share =	0.6 			# share of the total labour need 

# labour 	

nurseryraising_md = 1 			# mandays per acre 
fieldprep_md = 6 				# mandays per acre 
transplanting_md = 8 			# mandays per acre 
weedhoe_md = 10 				# mandays per acre 
fertpest_md = 1 				# mandays per acre 
watermngmnt_md = 5 				# mandays per acre 
harvesting_md = 10 				# mandays per acre 
transportation_md = 5 			# mandays per acre 
threswinow_md = 12 				# mandays per acre 
storing_md = 2 					# mandays per acre 
marketing_md = 2 				# mandays per acre 
		
# yield 	

paddy_yield	= 10 				# quintals/acre
straw_yield = 2030 				# kg/acre
cowmilk_yield = 750 			# ltr/cow	
goatmilk_yield = 300 			# ltr/goat	
babygoat_births = 2 			# babies/goat
compost	= 100  					# kg/acre
employment_wage	= 50 			# hrs
SHGcontribution_yield = 40 		# hrs


	# # # P R O G R A M  S T A R T S # # #

# user is prompted to select starting assets 

print("\n")
land = input("How many acres of land : ")
irrigated = input("How many are irrigated : ")
paddy = input("How many are paddy : ")
cow = input("How many cows : ")
goat = input("How many goats : ")
initial_debt = input("How much is the intitial debt : ")

# set randomness factor for both players

turn_random = round(random.uniform(0.85, 1.15), 2)
family_share = family_share * turn_random
paddy_yield = paddy_yield * turn_random

# debt distribution calculation

credit_debt = initial_debt * 0.7
MFI_debt = initial_debt * 0.2
informal_debt = initial_debt * 0.1
total_debt = initial_debt

# interest cost calculation

turn_interest = (credit_debt * credit_cost) + (MFI_debt * MFI_cost) + (informal_cost * informal_debt)


# labor cost correction 

labour_demand = family_share * paddy * (fieldprep_md + nurseryraising_md + transplanting_md + weedhoe_md + fertpest_md + watermngmnt_md + harvesting_md + transportation_md + storing_md + marketing_md)

# paddy cumulative reduction

if paddy <= 1:
	paddy_reduction = 1
elif paddy == 2: 
	paddy_reduction = 0.85
elif paddy == 3:
	paddy_reduction = 0.73
elif paddy == 4:
	paddy_reduction = 0.63
elif paddy == 5:
	paddy_reduction = 0.55
elif paddy == 6:
	paddy_reduction = 0.49
else:
	paddy_reduction = 0.48


# paddy calculations

paddy_labour = (paddy * employment_rate * labour_demand) * paddy_reduction

paddy_nonlabour = paddy_reduction * paddy * (paddys_cost + urea_cost + DAP_cost + MOP_cost + compost_cost)
paddy_income = paddy * (paddy_rate * paddy_yield)
paddy_net = paddy_income - (paddy_labour + paddy_nonlabour)

# cow calculation

cow_nonlabour = cow * ((cattlef_min * cattlef_cost) + (dryf_min * dryf_cost) + (mineral_min * mineral_cost) + (greenf_min * greenf_cost) + livestock_shed)
cow_income = cow * (cowmilk_yield * cowmilk_rate)
cow_net = cow_income - cow_nonlabour

# goat calculation

goat_income = goat * (goatmilk_yield * goatmilk_rate) + (babygoat_births * babygoat_rate)
goat_net = goat_income

# suplementary income 

suplementary_income = (employment_rate * employment_wage) + (SHGcontribution_rate * SHGcontribution_yield)

# p&l

turn_assets = (land_value * land) + (cow_value * cow) + (goat_value * goat)

turn_costs0 = cow_nonlabour + paddy_nonlabour + paddy_labour + turn_interest
turn_inputs = cow_nonlabour + paddy_nonlabour
turn_labour = paddy_labour
turn_family = turn_labour * family_share
turn_hired = turn_labour - turn_family 
turn_risk = risk_cost * turn_costs0

turn_costs = turn_costs0 + turn_risk

turn_revenue = (goat_income + cow_income + paddy_income + suplementary_income)
turn_farm = paddy_income
turn_animal = goat_income + cow_income
turn_other = suplementary_income

turn_net = turn_revenue - turn_costs
turn_interestfree = turn_net + turn_interest

turn_investment = turn_hired + turn_risk + turn_labour + turn_inputs
turn_returnrate = turn_investment / turn_revenue * 100

# outputs 

colorama.init()

print("\n")
print(Fore.WHITE + Back.BLACK + "r u r a l  d e s i g n  l a b" + Style.RESET_ALL) 
print("\n")
print(Fore.WHITE + Back.BLACK + locale.format("%d", turn_assets, grouping=True), end='') 
print("\t A S S E T S"  + Style.RESET_ALL)
print(Fore.BLACK + locale.format("%d", land_value * land, grouping=True), end='')
print("\t > Land value")
print(Fore.BLACK + locale.format("%d", (cow_value * cow) + (goat_value * goat), grouping=True), end='')
print("\t > Animal value")
print("\n")
print(Fore.WHITE + Back.RED + locale.format("%d", turn_costs, grouping=True), end='')
print("\t C O S T S"  + Style.RESET_ALL)
print(Fore.RED + locale.format("%d", turn_inputs, grouping=True), end='')
print("\t > Inputs")
print(locale.format("%d", turn_labour, grouping=True), end='')
print("\t > Labour")
print(locale.format("%d", turn_family, grouping=True), end='')
print("\t  >> family share")
print(locale.format("%d", turn_labour - turn_family, grouping=True), end='')
print("\t  >> waged share")
print(locale.format("%d", turn_risk, grouping=True), end='')
print("\t > Risk")
print(locale.format("%d", turn_interest, grouping=True), end='')
print("\t > Interest"  + Style.RESET_ALL)

print("\n")
print(Fore.WHITE + Back.GREEN + locale.format("%d", turn_revenue, grouping=True), end='')
print("\t R E V E N U E"  + Style.RESET_ALL)
print(Fore.GREEN + locale.format("%d", turn_farm, grouping=True), end='')
print("\t > Farm based")
print(locale.format("%d", turn_animal, grouping=True), end='')
print("\t > Animal based")
print(locale.format("%d", turn_other, grouping=True), end='')
print("\t > Other")

print("\n")
print(Fore.WHITE + Back.BLACK + locale.format("%d", turn_net, grouping=True), end='')
print("\t N E T"  + Style.RESET_ALL)
print(Fore.BLACK + locale.format("%d", turn_interestfree, grouping=True), end='')
print("\t > Before interest payments")
print(locale.format("%d", turn_returnrate, grouping=True), end='')
print("\t > Return on capital invested (%)" + Style.RESET_ALL)
print("\n")
