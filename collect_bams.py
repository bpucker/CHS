### Boas Pucker ###
### b.pucker@tu-bs.de ###
### v0.1 ###

__usage__ = """
					python3 collect_bams.py
					--in <INPUT_FOLDER>
					--out <OUTPUT_FOLDER>
					"""

import os, glob, sys, subprocess

# --- end of imports --- #

def main( arguments ):
	"""! @brief run everything """
	
	input_folder = arguments[ arguments.index('--in')+1 ]
	output_folder = arguments[ arguments.index('--out')+1 ]
	
	if input_folder[-1] != "/":
		input_folder += "/"
	
	if output_folder[-1] != "/":
		output_folder += "/"
	
	if not os.path.exists( output_folder ):
		os.makedirs( output_folder )

	bams = glob.glob( input_folder + "*/*.bam" )
	for bam in bams:
		if "_" in bam.split('/')[-2]:
			new_bam = output_folder + bam.split('/')[-2].split('_')[0] + ".bam"
		else:
			new_bam = output_folder + bam.split('/')[-2] + ".bam"
		p = subprocess.Popen( args="cp " + bam + " " + new_bam, shell=True )
		p.communicate()


if '--in' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
