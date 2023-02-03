### Boas Pucker ###
### b.pucker@tu-bs.de ###
### v0.1 ###

__usage__ = """
					python3 extract_bam_region.py
					--in <INPUT_FOLDER>
					--out <OUTPUT_FOLDER>
					--seq <SEQUENCE_ID>
					--start <START_POSITION>
					--end <END_POSITION>
					"""

import os, glob, sys, subprocess

# --- end of imports --- #

def main( arguments ):
	"""! @brief run everything """
	
	input_folder = arguments[ arguments.index('--in')+1 ]
	output_folder = arguments[ arguments.index('--out')+1 ]
	
	seq = arguments[ arguments.index('--seq')+1 ]
	start = int( arguments[ arguments.index('--start')+1 ] )
	end = int( arguments[ arguments.index('--end')+1 ] )
	
	if input_folder[-1] != "/":
		input_folder += "/"
	
	if output_folder[-1] != "/":
		output_folder += "/"
	
	if not os.path.exists( output_folder ):
		os.makedirs( output_folder )

	bams = glob.glob( input_folder + "*.bam" )
	#add automatic indexing if necessary: ls *.bam | xargs -n1 -P5 samtools index
	
	# --- extract region of interest from mapping --- # 
	for bam in bams:
		ID = bam.split('/')[-1].split('.')[0]
		new_bam = output_folder + ID + '_' + seq + "_" + str( start ) + "_" + str( end ) + ".bam"
		#print( "samtools view " + bam + " " + '"' + seq + ':' + str( start ) + "-" + str( end ) + '" > ' + new_bam )
		p = subprocess.Popen( args="samtools view -b " + bam + " " + '"' + seq + ':' + str( start ) + "-" + str( end ) + '" > ' + new_bam, shell=True )
		p.communicate()
	
	# --- indexing BAM files --- #
	#ls *.bam | xargs -n1 -P5 samtools index
	

if '--in' in sys.argv and '--out' in sys.argv and '--seq' in sys.argv and '--start' in sys.argv and '--end' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
