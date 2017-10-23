import csv

def formattedOutput(fileName, data, headerFormatted):
	with open(fileName, 'wb') as fout:
		tempstring = ",,Overall,," +str(data[0])+"\n"
		tempstring = tempstring + ",,,,Yes,,No\n"
		tempstring = tempstring + ",,N,%,N,%,N,%\n"
		tempstring = tempstring + "Overall,," + str(data[-1][2]) + ",," + str(data[-1][0]) + ",," + str(data[-1][1]) + "\n"
		for results in data[2:]:
			# check for divide by 0 error?
			if data[-1][2] > 0:
				percent1 = str(round(100*float(results[2])/float(data[-1][2]),2)) + "%"
			else:
				percent1 = str(0)
			if results[2] > 0:
				percent2 = str(round(100*float(results[0])/float(results[2]),2)) + "%"
				percent3 = str(round(100*float(results[1])/float(results[2]),2)) + "%"
			else:
				percent2 = str(0)
				percent3 = str(0)
			tempstring = tempstring + results[3] + "," \
			+ results[4] + "," \
			+ str(results[2]) + "," \
			+ percent1 + "," \
			+ str(results[0]) + "," \
			+ percent2 + "," \
			+ str(results[1]) + "," \
			+ percent3 + "," \
			+ "\n"
		fout.write(tempstring)
		fout.close()
	

with open('forchris_python.csv', 'rb') as fin:
    reader = csv.reader(fin)
    your_list = list(reader)

MasterList=[]

HeaderPrint=["Description, <1_pos, <1_neg, 1-<6_pos, 1-<6_neg, 6-<11_pos, 6-<11_neg, 11-<15_pos, 11-<15_neg, 15-<18_pos, 15-<18_neg, >18_pos, >18_neg, sex_f_pos, sex_f_neg, sex_m_pos, sex_m_neg, race_white_pos, race_white_neg, race_black_pos, race_black_neg, race_asian_pos, race_asian_neg, race_other_pos, race_other_neg, race_hispanic_pos, race_hispanic_neg, race_non-hispanic_pos, race_non-hispanic_neg, circumcised_pos, circumcised_neg, uncircumcised_pos, uncircumcised_neg, unknown_circ_pos, unknown_circ_neg, hydro_yes_pos, hydro_yes_neg, hydro_no_pos, hydro_no_neg, hydro_unknown_pos, hydro_unknown_neg, hx_augment_yes_pos, hx_augment_yes_neg, hx_augment_no_pos, hx_augment_no_neg, hx_cath_yes_pos, hx_cath_yes_neg, hx_cath_no_pos, hx_cath_no_neg, recent_uti_yes_pos, recent_uti_yes_neg, recent_uti_no_pos, recent_uti_no_neg, recent_uti_unk_pos, recent_uti_unk_neg, VUR1-2_pos, VUR1-2_neg, VUR3-5_pos, VUR3-5_neg, VURunk_pos, VURunk_neg, VUR_yes_pos, VUR_yes_neg, VUR_no_pos, VUR_no_neg, Eti-Myel_pos, Eti-Myel_neg, Eti-Fatt_pos, Eti-Fatt_neg, Eti-Othe_pos, Eti-Othe_neg, Sum_yes, Sum_no, Sum_total"]

chkValsAll=[[231,"negative","positive","Col HX: If Culture","CulturePos.csv"], \
            [232,"Unchecked","Checked","Col HY: E.Coli","EColi.csv"], \
			[233,"Unchecked","Checked","Col HZ: Proteus","Proteus.csv"], \
			[234,"Unchecked","Checked","Col IA: Pseudomonas","Pseudomonas.csv"], \
			[235,"Unchecked","Checked","Col IB: Enterococcus","Enterococcus.csv"],	\
			[236,"Unchecked","Checked","Col IC: Klebsiella","Klebsiella.csv"], \
			[237,"Unchecked","Checked","Col ID: Staphylococcus","Staphy.csv"], \
			[252,"Unchecked","Checked","Col IS: Ciprofloxacin","Cipro.csv"], \
			[340,"No","Yes","Col MC: Resistances","Resistances.csv"], \
			[341,"Unchecked","Checked","Col MD: Bactrim","Bactrim.csv"], \
			[342,"Unchecked","Checked","Col ME: Amoxicillin","Amoxicillin.csv"], \
			[343,"Unchecked","Checked","Col MF: Augmentin","Augmentin.csv"], \
			[344,"Unchecked","Checked","Col MG: Nitrofurantoin","Nitrofurantoin.csv"], \
			[345,"Unchecked","Checked","Col MH: Cephalexin","Cephalexin.csv"]
			]

headerFormatted = ["<1yr, 1 to <6, 6 to <11, 11 to <15, 15 to <18, 18 and greater, Sex-Female, Sex-Male, Race-White, Race-Black, Race-Asian, Race-Other, Race-Hispanic, Race-nonHispanic, Circ-Circumcised, Circ-Uncircumcised, Circ-Unknown state, Hydronephrosis-Yes, Hydronephrosis-No, Hydronephrosis-Unknown, Hx Augment-Yes, Hx Augment-No, Hx Catheterizable Channel-Yes, Hx Catheterizable Channel-No, Recent UTI-Yes, Recent UTI-No, Recent UTI-Unknown, VUR grade I to II, VUR grade III to V, VUR grade unknown, Etiology Myelomeningocele, Etiology Fatt, Etiology Other, Sum "]			
			
for chkVals in chkValsAll:
	# Initialization of variables
	#print "\n" + chkVals[3] + "\n"
	sum_yes=0
	sum_no=0
	sum_total=0
	sum_less_one=[0,0,0,"Age","<1yr"]
	sum_one_six=[0,0,0,"Age","1 to <6"]
	sum_six_eleven=[0,0,0,"Age","6 to <11"]
	sum_eleven_fifteen=[0,0,0,"Age","11 to <15"]
	sum_fifteen_eighteen=[0,0,0,"Age","15 to <18"]
	sum_greater_eighteen=[0,0,0,"Age","18 and older"]

	sex_f=[0,0,0,"Sex","Female"]
	sex_m=[0,0,0,"Sex","Male"]

	race_w=[0,0,0,"Race","White"]
	race_b=[0,0,0,"Race","Black/African"]
	race_a=[0,0,0,"Race","Asian"]
	race_o=[0,0,0,"Race","Other"]

	race_his=[0,0,0,"Ethnicity/Race","Hispanic"]
	race_nhis=[0,0,0,"Ethnicity/Race","nonHispanic"]

	circumcised=[0,0,0,"Circumcision","Circumcised"]
	uncircumcised=[0,0,0,"Circumcision","Uncircumcised"]
	unknown_circ=[0,0,0,"Circumcision","Unknown"]

	hydro_yes=[0,0,0,"Hydronephrosis (Most Recent Test","Yes"]
	hydro_no=[0,0,0,"Hydronephrosis (Most Recent Test","No"]
	hydro_unk=[0,0,0,"Hydronephrosis (Most Recent Test","Unknown"]

	hx_augmentation_y=[0,0,0,"Hx Augmentation","Yes"]
	hx_augmentation_n=[0,0,0,"Hx Augmentation","No"]

	hx_cath_y=[0,0,0,"Hx Catheterizable Channel","Yes"]
	hx_cath_n=[0,0,0,"Hx Catheterizable Channel","No"]

	recent_uti_y=[0,0,0,"Recent UTI","Yes"]
	recent_uti_n=[0,0,0,"Recent UTI","No"]
	recent_uti_unk=[0,0,0,"Recent UTI","Unknown"]

	VUR_1_2=[0,0,0,"VUR (grade of those with VUR","VUR grade I to II"]
	VUR_3_5=[0,0,0,"VUR (grade of those with VUR","VUR grade III to V"]
	VUR_unk=[0,0,0,"VUR (grade of those with VUR","VUR grade unknown"]
	VUR_y=[0,0,0,"VUR (most recent test","Yes"]
	VUR_n=[0,0,0,"VUR (most recent test","No"]

	etiology_myel=[0,0,0,"Etiology","Myelomeningocele"]
	etiology_fatt=[0,0,0,"Etiology","Fatt"]
	etiology_othe=[0,0,0,"Etiology","Other"]

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
	sum_list=[]
	sum_list.append(sum_yes)
	sum_list.append(sum_no)
	sum_list.append(sum_total)
	sum_list.append("Sum")
	sum_list.append("Sum")
	MasterSubList = []
	MasterSubList.append(chkVals[3])
	MasterSubList.append(chkVals[4])
	MasterSubList.append(sum_less_one)
	MasterSubList.append(sum_one_six)
	MasterSubList.append(sum_six_eleven)
	MasterSubList.append(sum_eleven_fifteen)
	MasterSubList.append(sum_fifteen_eighteen)
	MasterSubList.append(sum_greater_eighteen)
	MasterSubList.append(sex_f)
	MasterSubList.append(sex_m)
	MasterSubList.append(race_w)
	MasterSubList.append(race_b)
	MasterSubList.append(race_a)
	MasterSubList.append(race_o)
	MasterSubList.append(race_his)
	MasterSubList.append(race_nhis)
	MasterSubList.append(circumcised)
	MasterSubList.append(uncircumcised)
	MasterSubList.append(unknown_circ)
	MasterSubList.append(hydro_yes)
	MasterSubList.append(hydro_no)
	MasterSubList.append(hydro_unk)
	MasterSubList.append(hx_augmentation_y)
	MasterSubList.append(hx_augmentation_n)
	MasterSubList.append(hx_cath_y)
	MasterSubList.append(hx_cath_n)
	MasterSubList.append(recent_uti_y)
	MasterSubList.append(recent_uti_n)
	MasterSubList.append(recent_uti_unk)
	MasterSubList.append(VUR_1_2)
	MasterSubList.append(VUR_3_5)
	MasterSubList.append(VUR_unk)
	MasterSubList.append(VUR_y)
	MasterSubList.append(VUR_n)
	MasterSubList.append(etiology_myel)
	MasterSubList.append(etiology_fatt)
	MasterSubList.append(etiology_othe)
	MasterSubList.append(sum_list)
	
	#print MasterSubList
	MasterList.append(MasterSubList)
	#print MasterList
	
	# print "Description\t" + chkVals[2][:3] + "\t" + chkVals[1][:3] + "\tSum"
	# print "<1:        \t" + str(sum_less_one[0]) + "\t" + str(sum_less_one[1]) + "\t" + str(sum_less_one[2])
		
	# print "1 - <6     \t" + str(sum_one_six[0]) + "\t" + str(sum_one_six[1]) + "\t" + str(sum_one_six[2])

	# print "6 - <11    \t"+ str(sum_six_eleven[0]) + "\t" + str(sum_six_eleven[1]) + "\t" + str(sum_six_eleven[2])

	# print "11 - <15   \t" + str(sum_eleven_fifteen[0]) + "\t" + str(sum_eleven_fifteen[1]) + "\t" + str(sum_eleven_fifteen[2])

	# print "15 - <18   \t" + str(sum_fifteen_eighteen[0]) + "\t" + str(sum_fifteen_eighteen[1]) + "\t" + str(sum_fifteen_eighteen[2])

	# print ">18        \t" + str(sum_greater_eighteen[0]) + "\t" + str(sum_greater_eighteen[1]) + "\t" + str(sum_greater_eighteen[2])
	
	# #----
	# print "Female     \t" + str(sex_f[0]) + "\t" + str(sex_f[1]) + "\t" + str(sex_f[2])

	# print "Male       \t" + str(sex_m[0]) + "\t" + str(sex_m[1]) + "\t" + str(sex_m[2])
	
	# #----
	# print "White      \t" + str(race_w[0]) + "\t" + str(race_w[1]) + "\t" + str(race_w[2])

	# print "Black      \t" + str(race_b[0]) + "\t" + str(race_b[1]) + "\t" + str(race_b[2])

	# print "Asian      \t" + str(race_a[0]) + "\t" + str(race_a[1]) + "\t" + str(race_a[2])

	# print "Other      \t" + str(race_o[0]) + "\t" + str(race_o[1]) + "\t" + str(race_o[2])
	
	# #----
	# print "Hispanic   \t" + str(race_his[0]) + "\t" + str(race_his[1]) + "\t" + str(race_his[2])

	# print "nonHispa   \t" + str(race_nhis[0]) + "\t" + str(race_nhis[1]) + "\t" + str(race_nhis[2])
	
	# #----
	# print "Circumci   \t" + str(circumcised[0]) + "\t" + str(circumcised[1]) + "\t" + str(circumcised[2])

	# print "UnCircum   \t" + str(uncircumcised[0]) + "\t" + str(uncircumcised[1]) + "\t" + str(uncircumcised[2])

	# print "Unknown    \t" + str(unknown_circ[0]) + "\t" + str(unknown_circ[1]) + "\t" + str(unknown_circ[2])
	
	# #----
	# print "HydroYes   \t" + str(hydro_yes[0]) + "\t" + str(hydro_yes[1]) + "\t" + str(hydro_yes[2])
	
	# print "Hydro No   \t" + str(hydro_no[0]) + "\t" + str(hydro_no[1]) + "\t" + str(hydro_no[2])

	# print "HydroUnk   \t" + str(hydro_unk[0]) + "\t" + str(hydro_unk[1]) + "\t" + str(hydro_unk[2])
	
	# #----
	# print "AugmentY   \t" + str(hx_augmentation_y[0]) + "\t" + str(hx_augmentation_y[1]) + "\t" + str(hx_augmentation_y[2])

	# print "AugmentN   \t" + str(hx_augmentation_n[0]) + "\t" + str(hx_augmentation_n[1]) + "\t" + str(hx_augmentation_n[2])
	
	# #----
	# print "CathY      \t" + str(hx_cath_y[0]) + "\t" + str(hx_cath_y[1]) + "\t" + str(hx_cath_y[2])

	# print "CathN      \t" + str(hx_cath_n[0]) + "\t" + str(hx_cath_n[1]) + "\t" + str(hx_cath_n[2])

	# #----
	# print "UTI Yes    \t" + str(recent_uti_y[0]) + "\t" + str(recent_uti_y[1]) + "\t" + str(recent_uti_y[2])
	
	# print "UTI No     \t" + str(recent_uti_n[0]) + "\t" + str(recent_uti_n[1]) + "\t" + str(recent_uti_n[2])

	# print "UTI Unk    \t" + str(recent_uti_unk[0]) + "\t" + str(recent_uti_unk[1]) + "\t" + str(recent_uti_unk[2])
	
	# #----
	# print "VUR1-2     \t" + str(VUR_1_2[0]) + "\t" + str(VUR_1_2[1]) + "\t" + str(VUR_1_2[2])

	# print "VUR3-5     \t" + str(VUR_3_5[0]) + "\t" + str(VUR_3_5[1]) + "\t" + str(VUR_3_5[2])

	# print "VURunk     \t" + str(VUR_unk[0]) + "\t" + str(VUR_unk[1]) + "\t" + str(VUR_unk[2])

	# print "VUR Yes    \t" + str(VUR_y[0]) + "\t" + str(VUR_y[1]) + "\t" + str(VUR_y[2])

	# print "VUR No     \t" + str(VUR_n[0]) + "\t" + str(VUR_n[1]) + "\t" + str(VUR_n[2])
	
	# #----
	# print "Eti-Myel   \t" + str(etiology_myel[0]) + "\t" + str(etiology_myel[1]) + "\t" + str(etiology_myel[2])

	# print "Eti-Fatt   \t" + str(etiology_fatt[0]) + "\t" + str(etiology_fatt[1]) + "\t" + str(etiology_fatt[2])

	# print "Eti-Othe   \t" + str(etiology_othe[0]) + "\t" + str(etiology_othe[1]) + "\t" + str(etiology_othe[2])
	
	# #----
	# print "Total      \t" + str(sum_yes) + "\t" + str(sum_no) + "\t" + str(sum_total)

intermediate_string = ""
for l in HeaderPrint:
	print l

for printList in MasterList:
	intermediate_string = intermediate_string + printList[0]
	for results in printList[2:]:
		#print results
		intermediate_string = intermediate_string + ", " + str(results[0]) + ", " + str(results[1])
	formattedOutput(printList[1],printList,headerFormatted)	
	intermediate_string = intermediate_string + "\n"
print intermediate_string
