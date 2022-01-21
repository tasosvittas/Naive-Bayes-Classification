import io
import csv
from random import shuffle
from random import random
import numpy as np
from io import StringIO
from numpy import genfromtxt

with io.open('conatct-lenses.txt') as csvfile:
    data = csvfile.read()
    csvfile.close()

dataset = np.genfromtxt(StringIO(data), dtype=str, delimiter=' ')
shuffle(dataset)
print(dataset)
print(" ")
total_counter = 0
none_cnt = 0
soft_cnt = 0
hard_cnt = 0 
for i in range(len(dataset)):
    if dataset[i,4] == 'none':
        none_cnt = none_cnt+ 1
    elif dataset[i,4] == 'soft':
        soft_cnt = soft_cnt + 1
    elif dataset[i,4] == 'hard':
        hard_cnt = hard_cnt + 1
    total_counter = total_counter + 1
       
none_freq = none_cnt/total_counter
soft_freq = soft_cnt/total_counter
hard_freq = hard_cnt/total_counter

def frequency_counter(position, dataset_value, counter_name1, counter_name2, counter_name3):
    for i in range(len(dataset)):
        if dataset[i,position] == dataset_value:
            if dataset[i,4] == 'none': 
                counter_name1 = counter_name1 + 1
            if dataset[i,4] == 'soft':
                counter_name2 = counter_name2 + 1
            if dataset[i,4] == 'hard':
                counter_name3 = counter_name3 + 1
    return counter_name1, counter_name2, counter_name3

def laplace_estimation_class3(value_freq1, p1, value_freq2, p2, value_freq3, p3, cnt):
    if value_freq1 == 0 or value_freq2 == 0 or value_freq3 == 0:
        value_freq1,value_freq2,value_freq3=0,0,0
        p1 = p1 + 1
        p2 = p2 + 1
        p3 = p3 + 1
        cntsum = cnt + 3
        value_freq1 = p1 / cntsum
        value_freq2 = p2 / cntsum
        value_freq3 = p3 / cntsum
    return value_freq1, value_freq2, value_freq3

def laplace_estimation_class2(value_freq1,p1,value_freq2,p2,cnt):
    if value_freq1 == 0 or value_freq2 == 0:
        value_freq1,value_freq2=0,0
        cntsum = cnt + 2
        p1 = p1 + 1
        p2 = p2 + 1
        value_freq1 = p1 / cntsum
        value_freq2 = p2 / cntsum
    return value_freq1,value_freq2

#first column
young_none,young_soft,young_hard = 0,0,0
name0 = 'young'
young_none,young_soft,young_hard = frequency_counter(0, name0, young_none, young_soft, young_hard)    

prepresb_none, prepresb_soft, prepresb_hard = 0,0,0
name1 = 'prepresbyopic'
prepresb_none, prepresb_soft, prepresb_hard = frequency_counter(0, name1, prepresb_none, prepresb_soft, prepresb_hard)

presb_none, presb_soft, presb_hard = 0,0,0
name2 = 'presbyopic'
presb_none, presb_soft, presb_hard = frequency_counter(0, name2, presb_none, presb_soft, presb_hard)

fyoungnone = young_none/none_cnt
fppresbnone = prepresb_none/none_cnt
fpresbnone = presb_none/none_cnt
fyoungnone,fppresbnone,fpresbnone = laplace_estimation_class3(fyoungnone, young_none, fppresbnone, prepresb_none, fpresbnone, presb_none, none_cnt)

fyoungsoft = young_soft/soft_cnt
fppresbsoft = prepresb_soft/soft_cnt
fpresbsoft = presb_soft/soft_cnt
fyoungsoft,fppresbsoft,fpresbsoft = laplace_estimation_class3(fyoungsoft, young_soft ,fppresbsoft, prepresb_soft ,fpresbsoft, presb_soft ,soft_cnt)

fyounghard = young_hard/hard_cnt
fppresbhard = prepresb_hard/hard_cnt
fpresbhard = presb_hard/hard_cnt
fyounghard,fppresbhard,fpresbhard = laplace_estimation_class3(fyounghard,young_hard,fppresbhard,prepresb_hard,fpresbhard,presb_hard,hard_cnt)

#second column
myope_none, myope_soft, myope_hard = 0,0,0
name01 = 'myope'
myope_none, myope_soft,myope_hard = frequency_counter(1, name01, myope_none, myope_soft, myope_hard)

hypermetrope_none, hypermetrope_soft, hypermetrope_hard = 0,0,0
name02 = 'hypermetrope'
hypermetrope_none, hypermetrope_soft, hypermetrope_hard = frequency_counter(1, name02, hypermetrope_none, hypermetrope_soft, hypermetrope_hard)

fmyopenone = myope_none / none_cnt
fhypernone = hypermetrope_none /none_cnt
fmyopenone,fhypernone = laplace_estimation_class2(fmyopenone,myope_none,fhypernone,hypermetrope_none,none_cnt)

fmyopesoft = myope_soft / soft_cnt
fhypersoft = hypermetrope_soft / soft_cnt
fmyopesoft,fhypersoft = laplace_estimation_class2(fmyopesoft,myope_soft,fhypersoft,hypermetrope_soft,soft_cnt)

fmyopehard = myope_hard / hard_cnt
fhyperhard = hypermetrope_hard / hard_cnt
fmyopehard,fhyperhard = laplace_estimation_class2(fmyopehard,myope_hard,fhyperhard,hypermetrope_hard,hard_cnt)   

#third column
yes_none, yes_soft, yes_hard = 0,0,0
name001 = 'yes'
yes_none, yes_soft, yes_hard = frequency_counter(2, name001, yes_none, yes_soft, yes_hard)

no_none, no_soft, no_hard = 0,0,0
name002 = 'no'
no_none, no_soft, no_hard = frequency_counter(2, name002, no_none, no_soft, no_hard)

fynone = yes_none / none_cnt
fnnone = no_none / none_cnt
fynone,fnnone = laplace_estimation_class2(fynone,yes_none,fnnone,no_none,none_cnt)

fysoft =  yes_soft / soft_cnt
fnsoft = no_soft / soft_cnt
fysoft,fnsoft = laplace_estimation_class2(fysoft,yes_soft,fnsoft,no_soft,soft_cnt)

fyhard = yes_hard / hard_cnt
fnhard = no_hard / hard_cnt
fyhard,fnhard = laplace_estimation_class2(fyhard,yes_hard,fnhard,no_hard,hard_cnt)

#fourth column
normal_none, normal_soft, normal_hard = 0,0,0
name0001 = 'normal'
normal_none, normal_soft, normal_hard = frequency_counter(3, name0001, normal_none, normal_soft, normal_hard)

reduced_none, reduced_soft, reduced_hard = 0,0,0
name0002 = 'reduced'
reduced_none, reduced_soft, reduced_hard = frequency_counter(3, name0002, reduced_none, reduced_soft, reduced_hard)

fnormalnone = normal_none / none_cnt
freducednone = reduced_none/ none_cnt
fnormalnone,freducednone = laplace_estimation_class2(fnormalnone,normal_none,freducednone,reduced_none,none_cnt)

fnormalsoft = normal_soft / soft_cnt
freducedsoft = reduced_soft / soft_cnt
fnormalsoft,freducedsoft = laplace_estimation_class2(fnormalsoft,normal_soft,freducedsoft,reduced_soft,soft_cnt)

fnormalhard = normal_hard / hard_cnt
freducedhard = reduced_hard / hard_cnt
fnormalhard,freducedhard = laplace_estimation_class2(fnormalhard,normal_hard,freducedhard,reduced_hard,hard_cnt)

def none_switch(freq1,freq2,freq3,freq4):
    calc_none = freq1*freq2*freq3*freq4*none_freq
    return calc_none

def soft_switch(freq1,freq2,freq3,freq4):
    calc_soft = freq1*freq2*freq3*freq4*soft_freq
    return calc_soft

def hard_switch(freq1,freq2,freq3,freq4):
    calc_hard = freq1*freq2*freq3*freq4*hard_freq
    return calc_hard

def propability_calculator(calc_none,calc_soft,calc_hard):
    sum = calc_none+calc_soft+calc_hard
    pnone = float(calc_none / sum)
    psoft = float(calc_soft / sum)
    phard = float(calc_hard / sum)
    print('P(none): ',pnone)
    print('P(soft): ',psoft)
    print('P(hard): ',phard)

age = input("Age (young, prepresbyopic, presbyopic): ")
spectacle_prescription = input("Spectacle Prescription (myope, hypermetrope): ")
astigmatic = input("Astigmatic (no, yes): ")
tear_prod = input("Tear Production Rate (reduced, normal): ")

if age == 'young':
    if spectacle_prescription == 'myope':
        if astigmatic == 'no':
            if tear_prod == 'reduced':
                a = none_switch(fyoungnone,fmyopenone,fnnone,freducednone)
                b = soft_switch(fyoungsoft,fmyopesoft,fnsoft,freducedsoft)
                c = hard_switch(fyounghard,fmyopehard,fnhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fyoungnone,fmyopenone,fnnone,fnormalnone)
                b = soft_switch(fyoungsoft,fmyopesoft,fnsoft,fnormalsoft)
                c = hard_switch(fyounghard,fmyopehard,fnhard,fnormalhard)
                propability_calculator(a,b,c)
        if astigmatic == 'yes':
            if tear_prod == 'reduced':
                a = none_switch(fyoungnone,fmyopenone,fynone,freducednone)
                b = soft_switch(fyoungsoft,fmyopesoft,fysoft,freducedsoft)
                c = hard_switch(fyounghard,fmyopehard,fyhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fyoungnone,fmyopenone,fynone,fnormalnone)
                b = soft_switch(fyoungsoft,fmyopesoft,fysoft,fnormalsoft)
                c = hard_switch(fyounghard,fmyopehard,fyhard,fnormalhard)
                propability_calculator(a,b,c)
    if spectacle_prescription == 'hypermetrope':
        if astigmatic == 'no':
            if tear_prod == 'reduced':
                a = none_switch(fyoungnone,fhypernone,fnnone,freducednone)
                b = soft_switch(fyoungsoft,fhypersoft,fnsoft,freducedsoft)
                c = hard_switch(fyounghard,fhyperhard,fnhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fyoungnone,fhypernone,fnnone,fnormalnone)
                b = soft_switch(fyoungsoft,fhypersoft,fnsoft,fnormalsoft)
                c = hard_switch(fyounghard,fhyperhard,fnhard,fnormalhard)
                propability_calculator(a,b,c)
        if astigmatic == 'yes':
            if tear_prod == 'reduced':
                a = none_switch(fyoungnone,fhypernone,fynone,freducednone)
                b = soft_switch(fyoungsoft,fhypersoft,fysoft,freducedsoft)
                c = hard_switch(fyounghard,fhyperhard,fyhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fyoungnone,fhypernone,fynone,fnormalnone)
                b = soft_switch(fyoungsoft,fhypersoft,fysoft,fnormalsoft)
                c = hard_switch(fyounghard,fhyperhard,fyhard,fnormalhard)
                propability_calculator(a,b,c)
if age == 'prepresbyopic':
    if spectacle_prescription == 'myope':
        if astigmatic == 'no':
            if tear_prod == 'reduced':
                a = none_switch(fppresbnone,fmyopenone,fnnone,freducednone)
                b = soft_switch(fppresbsoft,fmyopesoft,fnsoft,freducedsoft)
                c = hard_switch(fppresbhard,fmyopehard,fnhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fppresbnone,fmyopenone,fnnone,fnormalnone)
                b = soft_switch(fppresbsoft,fmyopesoft,fnsoft,fnormalsoft)
                c = hard_switch(fppresbhard,fmyopehard,fnhard,fnormalhard)
                propability_calculator(a,b,c)
        if astigmatic == 'yes':
            if tear_prod == 'reduced':
                a = none_switch(fppresbnone,fmyopenone,fynone,freducednone)
                b = soft_switch(fppresbsoft,fmyopesoft,fysoft,freducedsoft)
                c = hard_switch(fppresbhard,fmyopehard,fyhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fppresbnone,fmyopenone,fynone,fnormalnone)
                b = soft_switch(fppresbsoft,fmyopesoft,fysoft,fnormalsoft)
                c = hard_switch(fppresbhard,fmyopehard,fyhard,fnormalhard)
                propability_calculator(a,b,c)
    if spectacle_prescription == 'hypermetrope':
        if astigmatic == 'no':
            if tear_prod == 'reduced':
                a = none_switch(fppresbnone,fhypernone,fnnone,freducednone)
                b = soft_switch(fppresbsoft,fhypersoft,fnsoft,freducedsoft)
                c = hard_switch(fppresbhard,fhyperhard,fnhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fppresbnone,fhypernone,fnnone,fnormalnone)
                b = soft_switch(fppresbsoft,fhypersoft,fnsoft,fnormalsoft)
                c = hard_switch(fppresbhard,fhyperhard,fnhard,fnormalhard)
                propability_calculator(a,b,c)
        if astigmatic == 'yes':
            if tear_prod == 'reduced':
                a = none_switch(fppresbnone,fhypernone,fynone,freducednone)
                b = soft_switch(fppresbsoft,fhypersoft,fysoft,freducedsoft)
                c = hard_switch(fppresbhard,fhyperhard,fyhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fppresbnone,fhypernone,fynone,fnormalnone)
                b = soft_switch(fppresbsoft,fhypersoft,fysoft,fnormalsoft)
                c = hard_switch(fppresbhard,fhyperhard,fyhard,fnormalhard)
                propability_calculator(a,b,c)
if age == 'presbyopic':
    if spectacle_prescription == 'myope':
        if astigmatic == 'no':
            if tear_prod == 'reduced':
                a = none_switch(fpresbnone,fmyopenone,fnnone,freducednone)
                b = soft_switch(fpresbsoft,fmyopesoft,fnsoft,freducedsoft)
                c = hard_switch(fpresbhard,fmyopehard,fnhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fpresbnone,fmyopenone,fnnone,fnormalnone)
                b = soft_switch(fpresbsoft,fmyopesoft,fnsoft,fnormalsoft)
                c = hard_switch(fpresbhard,fmyopehard,fnhard,fnormalhard)
                propability_calculator(a,b,c)
        if astigmatic == 'yes':
            if tear_prod == 'reduced':
                a = none_switch(fpresbnone,fmyopenone,fynone,freducednone)
                b = soft_switch(fpresbsoft,fmyopesoft,fysoft,freducedsoft)
                c = hard_switch(fpresbhard,fmyopehard,fyhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fpresbnone,fmyopenone,fynone,fnormalnone)
                b = soft_switch(fpresbsoft,fmyopesoft,fysoft,fnormalsoft)
                c = hard_switch(fpresbhard,fmyopehard,fyhard,fnormalhard)
                propability_calculator(a,b,c)
    if spectacle_prescription == 'hypermetrope':
        if astigmatic == 'no':
            if tear_prod == 'reduced':
                a = none_switch(fpresbnone,fhypernone,fnnone,freducednone)
                b = soft_switch(fpresbsoft,fhypersoft,fnsoft,freducedsoft)
                c = hard_switch(fpresbhard,fhyperhard,fnhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fpresbnone,fhypernone,fnnone,fnormalnone)
                b = soft_switch(fpresbsoft,fhypersoft,fnsoft,fnormalsoft)
                c = hard_switch(fpresbhard,fhyperhard,fnhard,fnormalhard)
                propability_calculator(a,b,c)
        if astigmatic == 'yes':
            if tear_prod == 'reduced':
                a = none_switch(fpresbnone,fhypernone,fynone,freducednone)
                b = soft_switch(fpresbsoft,fhypersoft,fysoft,freducedsoft)
                c = hard_switch(fpresbhard,fhyperhard,fyhard,freducedhard)
                propability_calculator(a,b,c)
            if tear_prod == 'normal':
                a = none_switch(fpresbnone,fhypernone,fynone,fnormalnone)
                b = soft_switch(fpresbsoft,fhypersoft,fysoft,fnormalsoft)
                c = hard_switch(fpresbhard,fhyperhard,fyhard,fnormalhard)
                propability_calculator(a,b,c)





