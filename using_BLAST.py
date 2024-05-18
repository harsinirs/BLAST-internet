#!usr/bin/python
#Running BLAST over the Internet
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import sys
import getopt


filename=sys.argv[1]

try:
    f=open(filename)
except IOError:
    print("file %s does not exist" % filename)
    
print("running BLAST over internet")

fasta_string = open(f).read()
result_handle = NCBIWWW.qblast("blastn","nt", fasta_string)#get ID/handle of query results

blast_record = NCBIXML.read(result_handle)#runs a special method to read XML (web-friendly ata format) of results
len(blast_record.alignments) #get all alignments

print("processing results")

E_value_thresh=0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect <E_value_thresh:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e-value:', hsp.expect)
            print(hsp.query)#query itself
            print(hsp.match)#how it matches
            print(hsp.sbjct)#print target that matches
            
print("End of page results.")
