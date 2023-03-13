### Boas Pucker ###
### b.pucker@tu-bs.de ###

__version__ = "v1.0"

__reference__ = "Pucker, 2023"

__usage__ = """
					python3 coverage_plotter.py
					--cov <COVERAGE_FILE>
					--out <OUTPUT_DIR>
					--seq <SEQUENCE_ID>
					--start <START>
					--end <END>
					bug reports and feature requests: b.pucker@tu-braunschweig.de
					"""

import os, glob, sys, subprocess
import matplotlib.pyplot as plt

# --- end of imports --- #

def load_coverage( cov_file, seq, start, end ):
	"""! @brief load coverage values from file """
	
	coverage = []
	with open( cov_file, "r" ) as f:
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			if parts[0] == seq:
				if start <= int( parts[1] )<= end:
					coverage.append( int( parts[2] ) )
			line = f.readline()
	return coverage


def coverage_plotter( output_file, coverage, seq, start, end, exons ):
	"""! @brief plot the coverage """
	
	fig, ax = plt.subplots( figsize=(8,3) )
	ax.plot( coverage, color="green" )
	ax.set_ylabel( "coverage" )
	ax.set_xlabel( "position at locus" )
	for exon in exons:
		ax.plot( [ exon[0]-start, exon[1]-start ], [ 0, 0 ], color="black" )
	plt.subplots_adjust(left=0.1, right=0.95, top=0.99, bottom=0.3)
	fig.savefig( output_file, dpi=300 )


def save_data( data_file, seq, start, coverage ):
	"""! @brief write data into output file """
	
	with open( data_file, "w" ) as out:
		for idx, val in enumerate( coverage ):
			new_line = "\t".join( [ seq, str( start+idx ), str( val ) ] ) + "\n"
			out.write( new_line )


def load_relevant_exon_positions( gff_file, seq, start, end ):
	"""! @brief load all exon positions within region of interest """
	
	exon_pos = []
	with open( gff_file, "r" ) as f:
		line = f.readline()
		while line:
			if line[0] != '#':
				parts = line.strip().split('\t')
				if parts[0] == seq:
					if parts[2] == "exon":
						if start < int( parts[3] ) < end:
							x, y = int( parts[3] ), int( parts[4] )
							exon_pos.append( [ x, y ] )
			line = f.readline()
	return exon_pos


def main( arguments ):
	"""! @brief run everything """
	
	cov_file = arguments[ arguments.index('--cov')+1 ]
	output_file = arguments[ arguments.index('--out')+1 ]
	seq = arguments[ arguments.index('--seq')+1 ]
	start = int( arguments[ arguments.index('--start')+1 ] )
	end = int( arguments[ arguments.index('--end')+1 ] )
	
	if '--gff' in arguments:
		gff_file = arguments[ arguments.index('--gff')+1 ]
		exons = load_relevant_exon_positions( gff_file, seq, start, end )
	else:
		exons = []
	
	cov = load_coverage( cov_file, seq, start, end )
	coverage_plotter( output_file, cov, seq, start, end, exons )
	data_file = output_file + ".data.txt"
	save_data( data_file, seq, start, cov )


if '--cov' in sys.argv and '--out' in sys.argv and '--seq' in sys.argv and '--start' in sys.argv and '--end' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
