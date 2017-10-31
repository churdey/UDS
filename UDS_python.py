import csv

def formattedOutput(fileName, data):
	with open(fileName, 'wb') as fout:
		tempstring = ",,Overall,," +str(data[0])+"\n"
		tempstring = tempstring + ",,,,Yes,,No\n"
		tempstring = tempstring + ",,N,% of Total,N,% of cohort,N,% of cohort\n"
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
	

with open('uds_latest.csv', 'rb') as fin:
    reader = csv.reader(fin)
    your_list = list(reader)

MasterList=[]

HeaderPrint=["Description, <1_pos, <1_neg, 1-<6_pos, 1-<6_neg, 6-<11_pos, 6-<11_neg, 11-<15_pos, 11-<15_neg, 15-<18_pos, 15-<18_neg, >18_pos, >18_neg, sex_f_pos, sex_f_neg, sex_m_pos, sex_m_neg, race_white_pos, race_white_neg, race_black_pos, race_black_neg, race_asian_pos, race_asian_neg, race_other_pos, race_other_neg, race_hispanic_pos, race_hispanic_neg, race_non-hispanic_pos, race_non-hispanic_neg, circumcised_pos, circumcised_neg, uncircumcised_pos, uncircumcised_neg, unknown_circ_pos, unknown_circ_neg, hydro_yes_pos, hydro_yes_neg, hydro_no_pos, hydro_no_neg,  hx_augment_yes_pos, hx_augment_yes_neg, hx_augment_no_pos, hx_augment_no_neg, hx_cath_yes_pos, hx_cath_yes_neg, hx_cath_no_pos, hx_cath_no_neg, recent_uti_yes_pos, recent_uti_yes_neg, recent_uti_no_pos, recent_uti_no_neg, recent_uti_unk_pos, recent_uti_unk_neg, VUR1-2_pos, VUR1-2_neg, VUR3-5_pos, VUR3-5_neg, VURunk_pos, VURunk_neg, VUR_yes_pos, VUR_yes_neg, VUR_no_pos, VUR_no_neg, Eti-Myel_pos, Eti-Myel_neg, Eti-Fatt_pos, Eti-Fatt_neg, Eti-Othe_pos, Eti-Othe_neg, Sum_yes, Sum_no, Sum_total"]

chkValsAll=[[231,"negative","positive","Col HX: If Culture","01_culture_posvsneg.csv"], \
            [232,"Unchecked","Checked","Col HY: E.Coli","EColi.csv"], \
			[233,"Unchecked","Checked","Col HZ: Proteus","Proteus.csv"], \
			[234,"Unchecked","Checked","Col IA: Pseudomonas","Pseudomonas.csv"], \
			[235,"Unchecked","Checked","Col IB: Enterococcus","Enterococcus.csv"],	\
			[236,"Unchecked","Checked","Col IC: Klebsiella","Klebsiella.csv"], \
			[237,"Unchecked","Checked","Col ID: Staphylococcus","Staph.csv"], \
			[238,"Unchecked","Checked","Col IE: Other Organism","OtherOrganism.csv"], \
			[239,"Unchecked","Checked","Col IF: Unknown Organism","UnknownOrganism.csv"], \
			[240,"Unchecked","Checked","Col IG: Multiple Organism","MultipleOrganism.csv"], \
			[372,"Unchecked","Checked","Col NI: Organism Not E.Coli","OrganismNotEColi.csv"], \
			[243,"Unchecked","Checked","Col IJ: Resistance Ampicillin","ResAmpicillin.csv"], \
			[244,"Unchecked","Checked","Col IK: Resistance Nitrofurantoin","ResNitrofurantoin.csv"], \
			[245,"Unchecked","Checked","Col IL: Resistance Tetracycline","ResTetracycline.csv"], \
			[246,"Unchecked","Checked","Col IM: Resistance Bactrim","ResBactrim.csv"], \
			[247,"Unchecked","Checked","Col IN: Resistance Gentamycin","ResGentamycin.csv"], \
			[248,"Unchecked","Checked","Col IO: Resistance Tobramycin","ResTobramycin.csv"], \
			[249,"Unchecked","Checked","Col IP: Resistance Amikacin","ResAmikacin.csv"], \
			[250,"Unchecked","Checked","Col IQ: Resistance Cefotaxime","ResCefotaxime.csv"], \
			[251,"Unchecked","Checked","Col IR: Resistance Ceftazidime","ResCeftazidime.csv"], \
			[252,"Unchecked","Checked","Col IS: Resistance Ciprofloxacin","ResCiprofloxacin.csv"], \
			[253,"Unchecked","Checked","Col IT: Resistance Aztreonam","ResAztreonam.csv"], \
			[254,"Unchecked","Checked","Col IU: Resistance Imipenem","ResImipenem.csv"], \
			[255,"Unchecked","Checked","Col IV: Resistance Zosyn","ResZosyn.csv"], \
			[256,"Unchecked","Checked","Col IX: Resistance Other","ResOther.csv"], \
			[373,"Unchecked","Checked","Col NJ: All EColi","AllEColi.csv"], \
			[374,"Unchecked","Checked","Col NK: All Proteus","AllProteus.csv"], \
			[375,"Unchecked","Checked","Col NL: All Pseudomonas","AllPseudomonas.csv"], \
			[376,"Unchecked","Checked","Col NM: All Enterococcus","AllEnterococcus.csv"], \
			[377,"Unchecked","Checked","Col NN: All Klebsiella","AllKlebsiella.csv"], \
			[378,"Unchecked","Checked","Col NO: All Staphylococcus","AllStaphylococcus.csv"], \
			[379,"Unchecked","Checked","Col NP: All Multiple-Other Organism","AllMultipleOther.csv"], \
			[380,"Unchecked","Checked","Col NQ: All Not EColi","AllNotEColi.csv"], \
			[382,"Unchecked","Checked","Col NS: All Resistances Ampicillin","AllResAmpicillin.csv"], \
			[383,"Unchecked","Checked","Col NT: All Resistances Nitrofurantoin","AllResNitrofurantoin.csv"], \
			[384,"Unchecked","Checked","Col NU: All Resistances Tetracycline","AllResTetracycline.csv"], \
			[385,"Unchecked","Checked","Col NV: All Resistances Bactrim","AllResBactrim.csv"], \
			[386,"Unchecked","Checked","Col NW: All Resistances Gentamycin","AllResGentamycin.csv"], \
			[387,"Unchecked","Checked","Col NX: All Resistances Tobramycin","AllResTobramycin.csv"], \
			[388,"Unchecked","Checked","Col NY: All Resistances Amikacin","AllResAmikacin.csv"], \
			[389,"Unchecked","Checked","Col NZ: All Resistances Cefotaxime","AllResCefotaxime.csv"], \
			[390,"Unchecked","Checked","Col OA: All Resistances Ceftazidime","AllResCeftazidime.csv"], \
			[391,"Unchecked","Checked","Col OB: All Resistances Ciprofloxacin","AllResCiprofloxacin.csv"], \
			[392,"Unchecked","Checked","Col OC: All Resistances Aztreonam","AllResAztreonam.csv"], \
			[393,"Unchecked","Checked","Col OD: All Resistances Imipenem","AllResImipenem.csv"], \
			[394,"Unchecked","Checked","Col OE: All Resistances Zosyn","AllResZosyn.csv"], \
			[395,"Unchecked","Checked","Col OF: All Resistances Other","AllResOther.csv"] \
			]
			#[252,"Unchecked","Checked","Col IS: Ciprofloxacin","Cipro.csv"], \
			#[340,"No","Yes","Col MC: Resistances","Resistances.csv"], \
			#[341,"Unchecked","Checked","Col MD: Bactrim","Bactrim.csv"], \
			#[342,"Unchecked","Checked","Col ME: Amoxicillin","Amoxicillin.csv"], \
			#[343,"Unchecked","Checked","Col MF: Augmentin","Augmentin.csv"], \
			#[344,"Unchecked","Checked","Col MG: Nitrofurantoin","Nitrofurantoin.csv"], \
			#[345,"Unchecked","Checked","Col MH: Cephalexin","Cephalexin.csv"]
			#]		
			
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

	hydro_yes=[0,0,0,"Hydronephrosis (Most Recent Test)","Yes"]
	hydro_no=[0,0,0,"Hydronephrosis (Most Recent Test)","No"]

	hx_augmentation_y=[0,0,0,"Hx Augmentation","Yes"]
	hx_augmentation_n=[0,0,0,"Hx Augmentation","No"]

	hx_cath_y=[0,0,0,"Hx Catheterizable Channel","Yes"]
	hx_cath_n=[0,0,0,"Hx Catheterizable Channel","No"]
	
	hx_bowel_surg_y=[0,0,0,"Hx Surgery with bowel in urinary tract","Yes"]
	hx_bowel_surg_n=[0,0,0,"Hx Surgery with bowel in urinary tract","No"]
	
	immunosuppression_y=[0,0,0,"Immunosuppression","Yes"]
	immunosuppression_n=[0,0,0,"Immunosuppression","No"]

	overnight_foley_y=[0,0,0,"Overnight Foley","Yes"]
	overnight_foley_n=[0,0,0,"Overnight Foley","No"]
	
	recent_uti_y=[0,0,0,"Recent UTI","Yes"]
	recent_uti_n=[0,0,0,"Recent UTI","No"]
	recent_uti_unk=[0,0,0,"Recent UTI","Unknown"]
	
	antibiotic_prophylaxis_y=[0,0,0,"Antibiotic Prophylaxis","Yes"]
	antibiotic_prophylaxis_n=[0,0,0,"Antibiotic Prophylaxis","No"]

	VUR_1_2=[0,0,0,"VUR (grade of those with VUR)","VUR grade I to II"]
	VUR_3_5=[0,0,0,"VUR (grade of those with VUR)","VUR grade III to V"]
	VUR_unk=[0,0,0,"VUR (grade of those with VUR)","VUR grade unknown"]
	VUR_y=[0,0,0,"VUR (most recent test)","Yes"]
	VUR_n=[0,0,0,"VUR (most recent test)","No"]

	etiology_myel=[0,0,0,"Etiology","Myelomeningocele"]
	etiology_fatt=[0,0,0,"Etiology","Fatt"]
	etiology_othe=[0,0,0,"Etiology","Other"]
	
	hydro_grade0=[0,0,0,"Hydronephrosis (grade)", "mild"]
	hydro_grade1=[0,0,0,"Hydronephrosis (grade)", "mild-moderate to moderate"]
	hydro_grade2=[0,0,0,"Hydronephrosis (grade)", "moderate-severe to severe"]

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
		if (j[138] == "unilateral") or \
		   (j[138] == "unilateral (solitary kidney)") or \
		   (j[138] == "bilateral"):
			if j[chkVals[0]] == chkVals[1]:
				hydro_yes[1] = hydro_yes[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_yes[0] = hydro_yes[0]+1
			hydro_yes[2] = hydro_yes[2]+1
		
		if (j[138] == "No Hydronephrosis on most recent test") or \
		   (j[138] == ""):
			if j[chkVals[0]] == chkVals[1]:
				hydro_no[1] = hydro_no[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_no[0] = hydro_no[0]+1
			hydro_no[2] = hydro_no[2]+1
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

	# HxBowel used in urinary tract surgery counting section begin
		if (j[178] == "Checked"): #This means yes
			if j[chkVals[0]] == chkVals[1]:
				hx_bowel_surg_y[1] = hx_bowel_surg_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hx_bowel_surg_y[0] = hx_bowel_surg_y[0]+1
			hx_bowel_surg_y[2] = hx_bowel_surg_y[2]+1
		
		if (j[178] == "Unchecked"): #This means no
			if j[chkVals[0]] == chkVals[1]:
				hx_bowel_surg_n[1] = hx_bowel_surg_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hx_bowel_surg_n[0] = hx_bowel_surg_n[0]+1
			hx_bowel_surg_n[2] = hx_bowel_surg_n[2]+1
	# HxBowel used in urinary tract surgery counting section end		
	
	# Immunosuppression counting section begin
		if j[85] == "Yes":
			if j[chkVals[0]] == chkVals[1]:
				immunosuppression_y[1] = immunosuppression_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				immunosuppression_y[0] = immunosuppression_y[0]+1
			immunosuppression_y[2] = immunosuppression_y[2]+1
		
		if (j[85] == "No") or (j[85] == ""):
			if j[chkVals[0]] == chkVals[1]:
				immunosuppression_n[1] = immunosuppression_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				immunosuppression_n[0] = immunosuppression_n[0]+1
			immunosuppression_n[2] = immunosuppression_n[2]+1
	# Immunosuppression counting section end
	
	# Overnight foley counting section begin
		if j[108] == "Yes":
			if j[chkVals[0]] == chkVals[1]:
				overnight_foley_y[1] = overnight_foley_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				overnight_foley_y[0] = overnight_foley_y[0]+1
			overnight_foley_y[2] = overnight_foley_y[2]+1
		
		if j[108] == "No":
			if j[chkVals[0]] == chkVals[1]:
				overnight_foley_n[1] = overnight_foley_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				overnight_foley_n[0] = overnight_foley_n[0]+1
			overnight_foley_n[2] = overnight_foley_n[2]+1
	# Overnight foley counting section end
	
	
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

	# Antibiotic Prophylaxis counting section begin
		if j[351] == "Checked":
			if j[chkVals[0]] == chkVals[1]:
				antibiotic_prophylaxis_y[1] = antibiotic_prophylaxis_y[1]+1
			if j[chkVals[0]] == chkVals[2]:
				antibiotic_prophylaxis_y[0] = antibiotic_prophylaxis_y[0]+1
			antibiotic_prophylaxis_y[2] = antibiotic_prophylaxis_y[2]+1
		
		if j[351] == "Unchecked":
			if j[chkVals[0]] == chkVals[1]:
				antibiotic_prophylaxis_n[1] = antibiotic_prophylaxis_n[1]+1
			if j[chkVals[0]] == chkVals[2]:
				antibiotic_prophylaxis_n[0] = antibiotic_prophylaxis_n[0]+1
			antibiotic_prophylaxis_n[2] = antibiotic_prophylaxis_n[2]+1
	# Antibiotic Prophylaxis counting section begin	
	
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

	# Hydronephrosis grading Section begin
		if (j[139] == "Mild"):
			if j[chkVals[0]] == chkVals[1]:
				hydro_grade0[1] = hydro_grade0[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_grade0[0] = hydro_grade0[0]+1
			hydro_grade0[2] = hydro_grade0[2]+1
		
		if (j[139] == "Mild-moderate") or \
		   (j[139] == "Moderate"):
			if j[chkVals[0]] == chkVals[1]:
				hydro_grade1[1] = hydro_grade1[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_grade1[0] = hydro_grade1[0]+1
			hydro_grade1[2] = hydro_grade1[2]+1

		if (j[139] == "Moderate-severe") or \
		   (j[139] == "Severe") or \
		   (j[139] == "Grade unknown"):
			if j[chkVals[0]] == chkVals[1]:
				hydro_grade2[1] = hydro_grade2[1]+1
			if j[chkVals[0]] == chkVals[2]:
				hydro_grade2[0] = hydro_grade2[0]+1
			hydro_grade2[2] = hydro_grade2[2]+1				
	# Hydronephrosis grading section end

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
	MasterSubList.append(circumcised)
	MasterSubList.append(uncircumcised)
	MasterSubList.append(unknown_circ)
	MasterSubList.append(race_w)
	MasterSubList.append(race_b)
	MasterSubList.append(race_a)
	MasterSubList.append(race_o)
	MasterSubList.append(race_his)
	MasterSubList.append(race_nhis)
	MasterSubList.append(etiology_myel)
	MasterSubList.append(etiology_fatt)
	MasterSubList.append(etiology_othe)
	MasterSubList.append(hx_augmentation_y)
	MasterSubList.append(hx_augmentation_n)
	MasterSubList.append(hx_cath_y)
	MasterSubList.append(hx_cath_n)
	MasterSubList.append(hx_bowel_surg_y)
	MasterSubList.append(hx_bowel_surg_n)
	MasterSubList.append(immunosuppression_y)
	MasterSubList.append(immunosuppression_n)
	MasterSubList.append(overnight_foley_y)
	MasterSubList.append(overnight_foley_n)
	MasterSubList.append(recent_uti_y)
	MasterSubList.append(recent_uti_n)
	MasterSubList.append(recent_uti_unk)
	MasterSubList.append(antibiotic_prophylaxis_y)
	MasterSubList.append(antibiotic_prophylaxis_n)
	MasterSubList.append(VUR_y)
	MasterSubList.append(VUR_n)
	MasterSubList.append(VUR_1_2)
	MasterSubList.append(VUR_3_5)
	MasterSubList.append(VUR_unk)
	MasterSubList.append(hydro_yes)
	MasterSubList.append(hydro_no)
	MasterSubList.append(hydro_grade0)
	MasterSubList.append(hydro_grade1)
	MasterSubList.append(hydro_grade2)
	MasterSubList.append(sum_list)
	
	MasterList.append(MasterSubList)
	
intermediate_string = ""
for l in HeaderPrint:
	print l

for printList in MasterList:
	intermediate_string = intermediate_string + printList[0]
	for results in printList[2:]:
		intermediate_string = intermediate_string + ", " + str(results[0]) + ", " + str(results[1])
	formattedOutput(printList[1],printList)	
	intermediate_string = intermediate_string + "\n"
print intermediate_string
