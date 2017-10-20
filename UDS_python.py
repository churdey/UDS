import csv

with open('forchris_pythong.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

i = 0
#for j in your_list[0]:
#	print str(i) + " " + j
#	i = i + 1

# Initialization of variables
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

# Script Parsing
for j in your_list[1:]:

# Age counting section begin
	if float(j[4]) <= 1.0:  #Age function
		if j[231] == "negative":
			sum_less_one[1] = sum_less_one[1]+1
		if j[231] == "positive":
			sum_less_one[0] = sum_less_one[0]+1
		sum_less_one[2] = sum_less_one[2]+1

	if (float(j[4]) > 1.0) and (float(j[4]) <= 6.0):  #Age function
		if j[231] == "negative":
			sum_one_six[1] = sum_one_six[1]+1
		if j[231] == "positive":
			sum_one_six[0] = sum_one_six[0]+1
		sum_one_six[2] = sum_one_six[2]+1

	if (float(j[4]) > 6.0) and (float(j[4]) <= 11.0):  #Age function
		if j[231] == "negative":
			sum_six_eleven[1] = sum_six_eleven[1]+1
		if j[231] == "positive":
			sum_six_eleven[0] = sum_six_eleven[0]+1
		sum_six_eleven[2] = sum_six_eleven[2]+1

	if (float(j[4]) > 11.0) and (float(j[4]) <= 15.0):  #Age function
		if j[231] == "negative":
			sum_eleven_fifteen[1] = sum_eleven_fifteen[1]+1
		if j[231] == "positive":
			sum_eleven_fifteen[0] = sum_eleven_fifteen[0]+1
		sum_eleven_fifteen[2] = sum_eleven_fifteen[2]+1		

	if (float(j[4]) > 15.0) and (float(j[4]) <= 18.0):  #Age function
		if j[231] == "negative":
			sum_fifteen_eighteen[1] = sum_fifteen_eighteen[1]+1
		if j[231] == "positive":
			sum_fifteen_eighteen[0] = sum_fifteen_eighteen[0]+1
		sum_fifteen_eighteen[2] = sum_fifteen_eighteen[2]+1

	if (float(j[4]) > 18.0):  #Age function
		if j[231] == "negative":
			sum_greater_eighteen[1] = sum_greater_eighteen[1]+1
		if j[231] == "positive":
			sum_greater_eighteen[0] = sum_greater_eighteen[0]+1
		sum_greater_eighteen[2] = sum_greater_eighteen[2]+1
# Age counting section end

# Gender counting section begin
	if j[5] == "Female":
		if j[231] == "negative":
			sex_f[1] = sex_f[1]+1
		if j[231] == "positive":
			sex_f[0] = sex_f[0]+1
		sex_f[2] = sex_f[2]+1
	
	if j[5] == "Male":
		if j[231] == "negative":
			sex_m[1] = sex_m[1]+1
		if j[231] == "positive":
			sex_m[0] = sex_m[0]+1
		sex_m[2] = sex_m[2]+1
# Gender counting section end		


# Ethnicity counting section begin
	if j[8] == "White":
		if j[231] == "negative":
			race_w[1] = race_w[1]+1
		if j[231] == "positive":
			race_w[0] = race_w[0]+1
		race_w[2] = race_w[2]+1
	
	if j[8] == "Black/African American":
		if j[231] == "negative":
			race_b[1] = race_b[1]+1
		if j[231] == "positive":
			race_b[0] = race_b[0]+1
		race_b[2] = race_b[2]+1

	if j[8] == "Asian":
		if j[231] == "negative":
			race_a[1] = race_a[1]+1
		if j[231] == "positive":
			race_a[0] = race_a[0]+1
		race_a[2] = race_a[2]+1
	
	if j[8] == "Other":
		if j[231] == "negative":
			race_o[1] = race_o[1]+1
		if j[231] == "positive":
			race_o[0] = race_o[0]+1
		race_o[2] = race_o[2]+1	
# Ethnicity counting section end

# Race counting section begin
	if j[7] == "Hispanic":
		if j[231] == "negative":
			race_his[1] = race_his[1]+1
		if j[231] == "positive":
			race_his[0] = race_his[0]+1
		race_his[2] = race_his[2]+1
	
	if j[7] == "Non-Hispanic":
		if j[231] == "negative":
			race_nhis[1] = race_nhis[1]+1
		if j[231] == "positive":
			race_nhis[0] = race_nhis[0]+1
		race_nhis[2] = race_nhis[2]+1
# Race counting section end		

# Cicumcision counting section begin
	if j[6] == "Circumcised":
		if j[231] == "negative":
			circumcised[1] = circumcised[1]+1
		if j[231] == "positive":
			circumcised[0] = circumcised[0]+1
		circumcised[2] = circumcised[2]+1
	
	if j[6] == "Uncircumcised":
		if j[231] == "negative":
			uncircumcised[1] = uncircumcised[1]+1
		if j[231] == "positive":
			uncircumcised[0] = uncircumcised[0]+1
		uncircumcised[2] = uncircumcised[2]+1
		
	if j[6] == "Unknown":
		if j[231] == "negative":
			unknown_circ[1] = unknown_circ[1]+1
		if j[231] == "positive":
			unknown_circ[0] = unknown_circ[0]+1
		unknown_circ[2] = unknown_circ[2]+1
# Cicumcision counting section end	

# Hydronephrosis counting section begin
	if j[137] == "Yes":
		if j[231] == "negative":
			hydro_yes[1] = hydro_yes[1]+1
		if j[231] == "positive":
			hydro_yes[0] = hydro_yes[0]+1
		hydro_yes[2] = hydro_yes[2]+1
	
	if j[137] == "No":
		if j[231] == "negative":
			hydro_no[1] = hydro_no[1]+1
		if j[231] == "positive":
			hydro_no[0] = hydro_no[0]+1
		hydro_no[2] = hydro_no[2]+1

	if (j[137] == "N/A") or (j[137] == "Unknown"):
		if j[231] == "negative":
			hydro_unk[1] = hydro_unk[1]+1
		if j[231] == "positive":
			hydro_unk[0] = hydro_unk[0]+1
		hydro_unk[2] = hydro_unk[2]+1
# Hydronephrosis counting section end

# HxAugmentation counting section begin
	if j[177] == "Checked": #This means yes
		if j[231] == "negative":
			hx_augmentation_y[1] = hx_augmentation_y[1]+1
		if j[231] == "positive":
			hx_augmentation_y[0] = hx_augmentation_y[0]+1
		hx_augmentation_y[2] = hx_augmentation_y[2]+1
	
	if j[177] == "Unchecked": #This means no
		if j[231] == "negative":
			hx_augmentation_n[1] = hx_augmentation_n[1]+1
		if j[231] == "positive":
			hx_augmentation_n[0] = hx_augmentation_n[0]+1
		hx_augmentation_n[2] = hx_augmentation_n[2]+1
# HxAugmentation counting section end

# HxCatheterizable Channel counting section begin
	if (j[175] == "Checked") or (j[176] == "Checked"): #This means yes
		if j[231] == "negative":
			hx_cath_y[1] = hx_cath_y[1]+1
		if j[231] == "positive":
			hx_cath_y[0] = hx_cath_y[0]+1
		hx_cath_y[2] = hx_cath_y[2]+1
	
	if (j[175] == "Unchecked") and (j[176] == "Unchecked"): #This means no
		if j[231] == "negative":
			hx_cath_n[1] = hx_cath_n[1]+1
		if j[231] == "positive":
			hx_cath_n[0] = hx_cath_n[0]+1
		hx_cath_n[2] = hx_cath_n[2]+1
# HxCatheterizable Channel counting section end	

# Recent UTI counting section begin
	if j[188] == "Yes":
		if j[231] == "negative":
			recent_uti_y[1] = recent_uti_y[1]+1
		if j[231] == "positive":
			recent_uti_y[0] = recent_uti_y[0]+1
		recent_uti_y[2] = recent_uti_y[2]+1
	
	if j[188] == "No":
		if j[231] == "negative":
			recent_uti_n[1] = recent_uti_n[1]+1
		if j[231] == "positive":
			recent_uti_n[0] = recent_uti_n[0]+1
		recent_uti_n[2] = recent_uti_n[2]+1

	if (j[188] == "N/A") or (j[188] == "Unknown"):
		if j[231] == "negative":
			recent_uti_unk[1] = recent_uti_unk[1]+1
		if j[231] == "positive":
			recent_uti_unk[0] = recent_uti_unk[0]+1
		recent_uti_unk[2] = recent_uti_unk[2]+1
# Recent UTI Channel counting section end	

# Total counting section begin	
	if j[231] == "negative":
		sum_no = sum_no+1
	if j[231] == "positive":
		sum_yes = sum_yes+1
	sum_total = sum_total+1
# Total counting section end


print "<1       - yes: " + str(sum_less_one[0]) + "\t no: " + str(sum_less_one[1]) + "\t total: " + str(sum_less_one[2])
	
print "1 - <6   - yes: " + str(sum_one_six[0]) + "\t no: " + str(sum_one_six[1]) + "\t total: " + str(sum_one_six[2])

print "6 - <11  - yes: " + str(sum_six_eleven[0]) + "\t no: " + str(sum_six_eleven[1]) + "\t total: " + str(sum_six_eleven[2])

print "11 - <15 - yes: " + str(sum_eleven_fifteen[0]) + "\t no: " + str(sum_eleven_fifteen[1]) + "\t total: " + str(sum_eleven_fifteen[2])

print "15 - <18 - yes: " + str(sum_fifteen_eighteen[0]) + "\t no: " + str(sum_fifteen_eighteen[1]) + "\t total: " + str(sum_fifteen_eighteen[2])

print ">18      - yes: " + str(sum_greater_eighteen[0]) + "\t no: " + str(sum_greater_eighteen[1]) + "\t total: " + str(sum_greater_eighteen[2])
print
#----
print "Female   - yes: " + str(sex_f[0]) + "\t no: " + str(sex_f[1]) + "\t total: " + str(sex_f[2])

print "Male     - yes: " + str(sex_m[0]) + "\t no: " + str(sex_m[1]) + "\t total: " + str(sex_m[2])
print
#----
print "White    - yes: " + str(race_w[0]) + "\t no: " + str(race_w[1]) + "\t total: " + str(race_w[2])

print "Black    - yes: " + str(race_b[0]) + "\t no: " + str(race_b[1]) + "\t total: " + str(race_b[2])

print "Asian    - yes: " + str(race_a[0]) + "\t no: " + str(race_a[1]) + "\t total: " + str(race_a[2])

print "Other    - yes: " + str(race_o[0]) + "\t no: " + str(race_o[1]) + "\t total: " + str(race_o[2])
print
#----
print "Hispanic - yes: " + str(race_his[0]) + "\t no: " + str(race_his[1]) + "\t total: " + str(race_his[2])

print "nonHispa - yes: " + str(race_nhis[0]) + "\t no: " + str(race_nhis[1]) + "\t total: " + str(race_nhis[2])
print
#----
print "Circumci - yes: " + str(circumcised[0]) + "\t no: " + str(circumcised[1]) + "\t total: " + str(circumcised[2])

print "UnCircum - yes: " + str(uncircumcised[0]) + "\t no: " + str(uncircumcised[1]) + "\t total: " + str(uncircumcised[2])

print "Unknown  - yes: " + str(unknown_circ[0]) + "\t no: " + str(unknown_circ[1]) + "\t total: " + str(unknown_circ[2])
print
#----
print "Hydro No - yes: " + str(hydro_no[0]) + "\t no: " + str(hydro_no[1]) + "\t total: " + str(hydro_no[2])

print "HydroYes - yes: " + str(hydro_yes[0]) + "\t no: " + str(hydro_yes[1]) + "\t total: " + str(hydro_yes[2])

print "HydroUnk - yes: " + str(hydro_unk[0]) + "\t no: " + str(hydro_unk[1]) + "\t total: " + str(hydro_unk[2])
print
#----
print "AugmentY - yes: " + str(hx_augmentation_y[0]) + "\t no: " + str(hx_augmentation_y[1]) + "\t total: " + str(hx_augmentation_y[2])

print "AugmentN - yes: " + str(hx_augmentation_n[0]) + "\t no: " + str(hx_augmentation_n[1]) + "\t total: " + str(hx_augmentation_n[2])
print
#----
print "CathY    - yes: " + str(hx_cath_y[0]) + "\t no: " + str(hx_cath_y[1]) + "\t total: " + str(hx_cath_y[2])

print "CathN    - yes: " + str(hx_cath_n[0]) + "\t no: " + str(hx_cath_n[1]) + "\t total: " + str(hx_cath_n[2])
print
#----
print "UTI No   - yes: " + str(recent_uti_n[0]) + "\t no: " + str(recent_uti_n[1]) + "\t total: " + str(recent_uti_n[2])

print "UTI Yes  - yes: " + str(recent_uti_y[0]) + "\t no: " + str(recent_uti_y[1]) + "\t total: " + str(recent_uti_y[2])

print "UTI Unk  - yes: " + str(recent_uti_unk[0]) + "\t no: " + str(recent_uti_unk[1]) + "\t total: " + str(recent_uti_unk[2])
print
#----
		
print "Total    - yes: " + str(sum_yes) + "\t no: " + str(sum_no) + "\t total: " + str(sum_total)
	