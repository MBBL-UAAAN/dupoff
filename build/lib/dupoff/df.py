#!/usr/bin/env python3

from Bio import SeqIO
import click as CLK


@CLK.command()
@CLK.option('--fasta', \
            help = 'Fasta file name', \
            required = True, \
            type = str)
@CLK.option('--out', \
            help = 'Fasta output file', \
            required = True, \
            type = str)
def main(fasta, out):
    '''
        Takes off duplicate sequences from fasta file and returns a log file and a fasta file with unique sequences.
    '''

    ids = [rec.id for rec in SeqIO.parse(fasta, 'fasta')]
    ids = set(sorted(ids))
    filt_seqs = []
    with open(fasta, 'r') as FHIN:
        for rec in SeqIO.parse(FHIN, 'fasta'):
            if rec.id in ids:
                filt_seqs.append(rec)
                ids.remove(rec.id)
        
    with open(out, 'w+') as FHOUT:
        SeqIO.write(filt_seqs, FHOUT, 'fasta')

if __name__ == '__main__':
    main()
