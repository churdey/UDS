import csv

with open('forchris_python.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

i = 0
#for j in your_list[0]:
#	print str(i) + " " + j
#	i = i + 1

chkValsAll=[[231,"negative","positive","Col HX: If Culture"], \
            [232,"Unchecked","Checked","Col HY: E.Coli"], \
			[233,"Unchecked","Checked","Col HZ: Proteus"], \
			[234,"Unchecked","Checked","Col IA: Pseudomonas"], \
			[235,"Unchecked","Checked","Col IB: Enterococcus"],	\
			[236,"Unchecked","Checked","Col IC: Klebsiella"], \
			[237,"Unchecked","Checked","Col ID: Staphylococcus"], \
			[252,"Unchecked","Checked","Col IS: Ciprofloxacin"], \
			[340,"No","Yes","Col MC: Resistances"], \
			[341,"Unchecked","Checked","Col MD: Bactrim"], \
			[342,"Unchecked","Checked","Col ME: Amoxicillin"], \
			[343,"Unchecked","Checked","Col MF: Augmentin"], \
			[344,"Unchecked","Checked","Col MG: Nitrofurantoin"], \
			[345,"Unchecked","Checked","Col MH: Cephalexin"]
			]

for chkVals in chkValsAll:
	# Initialization of variables
	print "\n" + chkVals[3] + "\n"
	sum_yes=0
	sum_no=0
	sum_total=0
	sum_less_one=[0,0,0]
	sum_one_six=[0,0,0]
	sum_six_eleven=[0,0,0]
	sum_eleven_fifteen=[0,0,0]
	sum_fifteen_eighteen=[0,0,0]
	sum_greater_eighteen=[0,0,0]

	sex_f=[0,0,0]
	sex_m=[0,0,0]

	race_w=[0,0,0]
	race_b=[0,0,0]
	race_a=[0,0,0]
	race_o=[0,0,0]

	race_his=[0,0,0]
	race_nhis=[0,0,0]

	circumcised=[0,0,0]
	uncircumcised=[0,0,0]
	unknown_circ=[0,0,0]

	hydro_yes=[0,0,0]
	hydro_no=[0,0,0]
	hydro_unk=[0,0,0]

	hx_augmentation_y=[0,0,0]
	hx_augmentation_n=[0,0,0]

	hx_cath_y=[0,0,0]
	hx_cath_n=[0,0,0]

	recent_uti_y=[0,0,0]
	recent_uti_n=[0,0,0]
	recent_uti_unk=[0,0,0]

	VUR_1_2=[0,0,0]
	VUR_3_5=[0,0,0]
	VUR_unk=[0,0,0]
	VUR_y=[0,0,0]
	VUR_n=[0,0,0]

	etiology_myel=[0,0,0]
	etiology_fatt=[0,0,0]
	etiology_othe=[0,0,0]

	# Script Parsing
	for j in your_list[9:]:

	# Age counting section begin
		if float(j[4]) <= 1.0:  #Age function
			if j[chkVals[0]] == chkVals[1]:
				sum_less_one[1] = sum_less_one[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sum_less_one[0] = sum_less_one[0]+1
			sum_less_one[2] = sum_less_one[2]+1

		if (float(j[4]) > 1.0) and (float(j[4]) <= 6.0):  #Age function
			if j[chkVals[0]] == chkVals[1]:
				sum_one_six[1] = sum_one_six[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sum_one_six[0] = sum_one_six[0]+1
			sum_one_six[2] = sum_one_six[2]+1

		if (float(j[4]) > 6.0) and (float(j[4]) <= 11.0):  #Age function
			if j[chkVals[0]] == chkVals[1]:
				sum_six_eleven[1] = sum_six_eleven[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sum_six_eleven[0] = sum_six_eleven[0]+1
			sum_six_eleven[2] = sum_six_eleven[2]+1

		if (float(j[4]) > 11.0) and (float(j[4]) <= 15.0):  #Age function
			if j[chkVals[0]] == chkVals[1]:
				sum_eleven_fifteen[1] = sum_eleven_fifteen[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sum_eleven_fifteen[0] = sum_eleven_fifteen[0]+1
			sum_eleven_fifteen[2] = sum_eleven_fifteen[2]+1		

		if (float(j[4]) > 15.0) and (float(j[4]) <= 18.0):  #Age function
			if j[chkVals[0]] == chkVals[1]:
				sum_fifteen_eighteen[1] = sum_fifteen_eighteen[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sum_fifteen_eighteen[0] = sum_fifteen_eighteen[0]+1
			sum_fifteen_eighteen[2] = sum_fifteen_eighteen[2]+1

		if (float(j[4]) > 18.0):  #Age function
			if j[chkVals[0]] == chkVals[1]:
				sum_greater_eighteen[1] = sum_greater_eighteen[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sum_greater_eighteen[0] = sum_greater_eighteen[0]+1
			sum_greater_eighteen[2] = sum_greater_eighteen[2]+1
	# Age counting section end

	# Gender counting section begin
		if j[5] == "Female":
			if j[chkVals[0]] == chkVals[1]:
				sex_f[1] = sex_f[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sex_f[0] = sex_f[0]+1
			sex_f[2] = sex_f[2]+1
		
		if j[5] == "Male":
			if j[chkVals[0]] == chkVals[1]:
				sex_m[1] = sex_m[1]+1
			if j[chkVals[0]] == chkVals[2]:
				sex_m[0] = sex_m[0]+1
			sex_m[2] = sex_m[2]+1
	# Gender counting section end		


	# Ethnicity counting section begin
		if j[8] == "White":
			if j[chkVals[0]] == chkVals[1]:
				race_w[1] = race_w[1]+1
			if j[chkVals[0]] == chkVals[2]:
				race_w[0] = race_w[0]+1
			race_w[2] = race_w[2]+1
		
		if j[8] == "Black/African American":
			if j[chkVals[0]] == chkVals[1]:
				race_b[1] = race_b[1]+1
			if j[chkVals[0]] == chkVals[2]:
				race_b[0] = race_b[0]+1
			race_b[2] = race_b[2]+1

		if j[8] == "Asian":
			if j[chkVals[0]] == chkVals[1]:
				race_a[1] = race_a[1]+1
			if j[chkVals[0]] == chkVals[2]:
				race_a[0] = race_a[0]+1
			race_a[2] = race_a[2]+1
		
		if j[8] == "Other":
			if j[chkVals[0]] == chkVals[1]:
				race_o[1] = race_o[1]+1
			if j[chkVals[0]] == chkVals[2]:
				race_o[0] = race_o[0]+1
			race_o[2] = race_o[2]+1	
	# Ethnicity counting section end

	# Race counting section begin
		if j[7] == "Hispanic":
			if j[chkVals[0]] == chkVals[1]:
				race_his[1] = race_his[1]+1
			if j[chkVals[0]] == chkVals[2]:
				race_his[0] = race_his[0]+1
			race_his[2] = race_his[2]+1
		
		if j[7] == "Non-Hispanic":
			if j[chkVals[0]] == chkVals[1]:
				race_nhis[1] = race_nhis[1]+1
			if j[chkVals[0]] == chkVals[2]:
				race_nhis[0] = race_nhis[0]+1
			race_nhis[2] = race_nhis[2]+1
	# Race counting section end		

	# Cicumcision counting section begin
		if j[6] == "Circumcised":
			if j[chkVals[0]] == chkVals[1]:
				circumcised[1] = circumcised[1]+1
			if j[chkVals[0]] == chkVals[2]:
				circumcised[0] = circumcised[0]+1
			circumcised[2] = circumcised[2]+1
		
		if j[6] == "Uncircumcised":
			if j[chkVals[0]] == chkVals[1]:
				uncircumcised[1] = uncircumcised[1]+1
			if j[chkVals[0]] == chkVals[2]:
				uncircumcised[0] = uncircumcised[0]+1
			uncircumcised[2] = uncircumcised[2]+1
			
		if j[6] == "Unknown":
			if j[chkVals[0]] == chkVals[1]:
				unknown_circ[1] = unknown_circ[1]+1
			if j[chkVals[0]] == chkVals[2]:
				unknown_circ[0] = unknown_circ[0]+1
			unknown_circ[2] = unknown_circ[2]+1
	# Cicumcision counting section end	

	# Hydronephrosis counting section begin
		if j[137] == "Yes":
			if j[chkVals[0]] == chkVals[1]:
				hydro_yes[1] = hydro_yes[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_yes[0] = hydro_yes[0]+1
			hydro_yes[2] = hydro_yes[2]+1
		
		if j[137] == "No":
			if j[chkVals[0]] == chkVals[1]:
				hydro_no[1] = hydro_no[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_no[0] = hydro_no[0]+1
			hydro_no[2] = hydro_no[2]+1

		if (j[137] == "N/A") or (j[137] == "Unknown"):
			if j[chkVals[0]] == chkVals[1]:
				hydro_unk[1] = hydro_unk[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_unk[0] = hydro_unk[0]+1
			hydro_unk[2] = hydro_unk[2]+1
	# Hydronephrosis counting section end

	# HxAugmentation counting section begin
		if j[177] == "Checked": #This means yes
			if j[chkVals[0]] == chkVals[1]:
				hx_augmentation_y[1] = hx_augmentation_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hx_augmentation_y[0] = hx_augmentation_y[0]+1
			hx_augmentation_y[2] = hx_augmentation_y[2]+1
		
		if j[177] == "Unchecked": #This means no
			if j[chkVals[0]] == chkVals[1]:
				hx_augmentation_n[1] = hx_augmentation_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hx_augmentation_n[0] = hx_augmentation_n[0]+1
			hx_augmentation_n[2] = hx_augmentation_n[2]+1
	# HxAugmentation counting section end

	# HxCatheterizable Channel counting section begin
		if (j[175] == "Checked") or (j[176] == "Checked"): #This means yes
			if j[chkVals[0]] == chkVals[1]:
				hx_cath_y[1] = hx_cath_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hx_cath_y[0] = hx_cath_y[0]+1
			hx_cath_y[2] = hx_cath_y[2]+1
		
		if (j[175] == "Unchecked") and (j[176] == "Unchecked"): #This means no
			if j[chkVals[0]] == chkVals[1]:
				hx_cath_n[1] = hx_cath_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hx_cath_n[0] = hx_cath_n[0]+1
			hx_cath_n[2] = hx_cath_n[2]+1
	# HxCatheterizable Channel counting section end	

	# Recent UTI counting section begin
		if j[188] == "Yes":
			if j[chkVals[0]] == chkVals[1]:
				recent_uti_y[1] = recent_uti_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				recent_uti_y[0] = recent_uti_y[0]+1
			recent_uti_y[2] = recent_uti_y[2]+1
		
		if j[188] == "No":
			if j[chkVals[0]] == chkVals[1]:
				recent_uti_n[1] = recent_uti_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				recent_uti_n[0] = recent_uti_n[0]+1
			recent_uti_n[2] = recent_uti_n[2]+1

		if (j[188] == "N/A") or (j[188] == "Unknown"):
			if j[chkVals[0]] == chkVals[1]:
				recent_uti_unk[1] = recent_uti_unk[1]+1
			if j[chkVals[0]] == chkVals[2]:
				recent_uti_unk[0] = recent_uti_unk[0]+1
			recent_uti_unk[2] = recent_uti_unk[2]+1
	# Recent UTI Channel counting section end	

	# VUR counting section begin
		if (j[136] == "I") or (j[136] == "II"): 
			if j[chkVals[0]] == chkVals[1]:
				VUR_1_2[1] = VUR_1_2[1]+1
			if j[chkVals[0]] == chkVals[2]:
				VUR_1_2[0] = VUR_1_2[0]+1
			VUR_1_2[2] = VUR_1_2[2]+1
		
		if (j[136] == "III") or (j[136] == "IV") or (j[136] == "V"): #
			if j[chkVals[0]] == chkVals[1]:
				VUR_3_5[1] = VUR_3_5[1]+1
			if j[chkVals[0]] == chkVals[2]:
				VUR_3_5[0] = VUR_3_5[0]+1
			VUR_3_5[2] = VUR_3_5[2]+1
			
		if (j[136] == "Unknown"): #
			if j[chkVals[0]] == chkVals[1]:
				VUR_unk[1] = VUR_unk[1]+1
			if j[chkVals[0]] == chkVals[2]:
				VUR_unk[0] = VUR_unk[0]+1
			VUR_unk[2] = VUR_unk[2]+1

		if (j[135] == "Unilateral") or (j[135] == "Bilateral"): #
			if j[chkVals[0]] == chkVals[1]:
				VUR_y[1] = VUR_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				VUR_y[0] = VUR_y[0]+1
			VUR_y[2] = VUR_y[2]+1
		else:
			if j[chkVals[0]] == chkVals[1]:
				VUR_n[1] = VUR_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				VUR_n[0] = VUR_n[0]+1
			VUR_n[2] = VUR_n[2]+1
	# VUR Channel counting section end	

	# Etiology counting section begin
		if j[88] == "Yes":
			if j[chkVals[0]] == chkVals[1]:
				etiology_myel[1] = etiology_myel[1]+1
			if j[chkVals[0]] == chkVals[2]:
				etiology_myel[0] = etiology_myel[0]+1
			etiology_myel[2] = etiology_myel[2]+1
		
		if (j[89] == "Yes") or (j[90] == "Yes") or (j[91] == "Yes") or (j[92] == "Yes"):
			if j[chkVals[0]] == chkVals[1]:
				etiology_fatt[1] = etiology_fatt[1]+1
			if j[chkVals[0]] == chkVals[2]:
				etiology_fatt[0] = etiology_fatt[0]+1
			etiology_fatt[2] = etiology_fatt[2]+1

		if j[93] == "Yes":
			if j[chkVals[0]] == chkVals[1]:
				etiology_othe[1] = etiology_othe[1]+1
			if j[chkVals[0]] == chkVals[2]:
				etiology_othe[0] = etiology_othe[0]+1
			etiology_othe[2] = etiology_othe[2]+1
	# Etiology counting section end	


	# Total counting section begin	
		if j[chkVals[0]] == chkVals[1]:
			sum_no = sum_no+1
		if j[chkVals[0]] == chkVals[2]:
			sum_yes = sum_yes+1
		sum_total = sum_total+1
	# Total counting section end

	print "Description\t" + chkVals[2][:3] + "\t" + chkVals[1][:3] + "\tSum"
	print "<1:        \t" + str(sum_less_one[0]) + "\t" + str(sum_less_one[1]) + "\t" + str(sum_less_one[2])
		
	print "1 - <6     \t" + str(sum_one_six[0]) + "\t" + str(sum_one_six[1]) + "\t" + str(sum_one_six[2])

	print "6 - <11    \t"+ str(sum_six_eleven[0]) + "\t" + str(sum_six_eleven[1]) + "\t" + str(sum_six_eleven[2])

	print "11 - <15   \t" + str(sum_eleven_fifteen[0]) + "\t" + str(sum_eleven_fifteen[1]) + "\t" + str(sum_eleven_fifteen[2])

	print "15 - <18   \t" + str(sum_fifteen_eighteen[0]) + "\t" + str(sum_fifteen_eighteen[1]) + "\t" + str(sum_fifteen_eighteen[2])

	print ">18        \t" + str(sum_greater_eighteen[0]) + "\t" + str(sum_greater_eighteen[1]) + "\t" + str(sum_greater_eighteen[2])
	
	#----
	print "Female     \t" + str(sex_f[0]) + "\t" + str(sex_f[1]) + "\t" + str(sex_f[2])

	print "Male       \t" + str(sex_m[0]) + "\t" + str(sex_m[1]) + "\t" + str(sex_m[2])
	
	#----
	print "White      \t" + str(race_w[0]) + "\t" + str(race_w[1]) + "\t" + str(race_w[2])

	print "Black      \t" + str(race_b[0]) + "\t" + str(race_b[1]) + "\t" + str(race_b[2])

	print "Asian      \t" + str(race_a[0]) + "\t" + str(race_a[1]) + "\t" + str(race_a[2])

	print "Other      \t" + str(race_o[0]) + "\t" + str(race_o[1]) + "\t" + str(race_o[2])
	
	#----
	print "Hispanic   \t" + str(race_his[0]) + "\t" + str(race_his[1]) + "\t" + str(race_his[2])

	print "nonHispa   \t" + str(race_nhis[0]) + "\t" + str(race_nhis[1]) + "\t" + str(race_nhis[2])
	
	#----
	print "Circumci   \t" + str(circumcised[0]) + "\t" + str(circumcised[1]) + "\t" + str(circumcised[2])

	print "UnCircum   \t" + str(uncircumcised[0]) + "\t" + str(uncircumcised[1]) + "\t" + str(uncircumcised[2])

	print "Unknown    \t" + str(unknown_circ[0]) + "\t" + str(unknown_circ[1]) + "\t" + str(unknown_circ[2])
	
	#----
	print "Hydro No   \t" + str(hydro_no[0]) + "\t" + str(hydro_no[1]) + "\t" + str(hydro_no[2])

	print "HydroYes   \t" + str(hydro_yes[0]) + "\t" + str(hydro_yes[1]) + "\t" + str(hydro_yes[2])

	print "HydroUnk   \t" + str(hydro_unk[0]) + "\t" + str(hydro_unk[1]) + "\t" + str(hydro_unk[2])
	
	#----
	print "AugmentY   \t" + str(hx_augmentation_y[0]) + "\t" + str(hx_augmentation_y[1]) + "\t" + str(hx_augmentation_y[2])

	print "AugmentN   \t" + str(hx_augmentation_n[0]) + "\t" + str(hx_augmentation_n[1]) + "\t" + str(hx_augmentation_n[2])
	
	#----
	print "CathY      \t" + str(hx_cath_y[0]) + "\t" + str(hx_cath_y[1]) + "\t" + str(hx_cath_y[2])

	print "CathN      \t" + str(hx_cath_n[0]) + "\t" + str(hx_cath_n[1]) + "\t" + str(hx_cath_n[2])

	#----
	print "UTI No     \t" + str(recent_uti_n[0]) + "\t" + str(recent_uti_n[1]) + "\t" + str(recent_uti_n[2])

	print "UTI Yes    \t" + str(recent_uti_y[0]) + "\t" + str(recent_uti_y[1]) + "\t" + str(recent_uti_y[2])

	print "UTI Unk    \t" + str(recent_uti_unk[0]) + "\t" + str(recent_uti_unk[1]) + "\t" + str(recent_uti_unk[2])
	
	#----
	print "VUR1-2     \t" + str(VUR_1_2[0]) + "\t" + str(VUR_1_2[1]) + "\t" + str(VUR_1_2[2])

	print "VUR3-5     \t" + str(VUR_3_5[0]) + "\t" + str(VUR_3_5[1]) + "\t" + str(VUR_3_5[2])

	print "VURunk     \t" + str(VUR_unk[0]) + "\t" + str(VUR_unk[1]) + "\t" + str(VUR_unk[2])

	print "VUR Yes    \t" + str(VUR_y[0]) + "\t" + str(VUR_y[1]) + "\t" + str(VUR_y[2])

	print "VUR No     \t" + str(VUR_n[0]) + "\t" + str(VUR_n[1]) + "\t" + str(VUR_n[2])
	
	#----
	print "Eti-Myel   \t" + str(etiology_myel[0]) + "\t" + str(etiology_myel[1]) + "\t" + str(etiology_myel[2])

	print "Eti-Fatt   \t" + str(etiology_fatt[0]) + "\t" + str(etiology_fatt[1]) + "\t" + str(etiology_fatt[2])

	print "Eti-Othe   \t" + str(etiology_othe[0]) + "\t" + str(etiology_othe[1]) + "\t" + str(etiology_othe[2])
	
	#----
	print "Total      \t" + str(sum_yes) + "\t" + str(sum_no) + "\t" + str(sum_total)
	