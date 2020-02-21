#This is a script is made for us to test how to run a script like this on the glycine server
#Author: Miguel Guardado
import numpy as np
import os
from pysam import VariantFile
os.chdir('/home/rohlfslab/1000genomes/GR37_Phase3_Data')

# To save time I am only going to look at chromosomes that are in these STR regions
VCFfileChr1 = VariantFile('ALL.chr1.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz')


os.chdir('/home/rohlfslab/TempFolder')
# Chr1-230769450,230769763

# For the STR region I will abstract all regions inside a 100kb(100,000)
# and along with that abstrat all indels inside a 10000kb region(10,000,000)

D1S1656file = [VCFfileChr1.header]
D1S1656Start = 230905196
D1S1656End = 230905196
print('Extracting CHR 1')
for snp in VCFfileChr1:
    if snp.pos in range(D1S1656Start - 50000, D1S1656End + 50000):
        D1S1656file.append(str(snp))


np.savetxt("STR_D1S1656STR_1000Genomes.vcf", D1S1656file, fmt='%s')

