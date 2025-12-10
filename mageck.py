#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 19:45:48 2025

@author: mariarf
"""

source activate mageck_env


#####mageck count
print("Inicializing sgRNA counts from trimmed fastq files")
mageck count -l /Users/mariarf/Desktop/IR/c231/Human_GeCKOv2_Library_A_MAGECK_format.csv --pdf-report --trim-5 0 -n 231_controlvsIR --sample-label R1,R8,R2,R5 --fastq /Users/mariarf/Desktop/IR/c231/TrimmedIR-R1_S1_L001_R1_001.fastq /Users/mariarf/Desktop/IR/c231/TrimmedIR-R8_S8_L001_R1_001.fastq /Users/mariarf/Desktop/IR/c231/TrimmedIR-R2_S2_L001_R1_001.fastq /Users/mariarf/Desktop/IR/c231/TrimmedIR-R5_S5_L001_R1_001.fastq

print("Done!")

#####mageck test 
print("Inicializing MAGeCK RRA test")
mageck test -k /Users/mariarf/Desktop/IR/c231/231_controlvsIR.count.txt -t R2,R5 -c R1,R8 -n 231_CvsIR --pdf-report --norm-method total —control-sgrna /Users/mariarf/Desktop/IR/c231/Control_sgRNAs_GeCKO.txt --paired
print("Done!")