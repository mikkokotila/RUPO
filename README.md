# RUPO
#### Simulator for evaluation of rural investment and development scenarios for small and micro size farmers. The underlying models and data are based on rural India.

At this stage, the code is left intentionally close to maximum verboseness. To run, the program needs to declare the following variables: 

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
