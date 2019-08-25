# TODO: add a feature to tranpose to concert pitch as well, but only if C is not already specified 

# using flats because flats are nicer than sharps :))))
# DESIGN: using two lists here seems redunant, there must be a better data structure for this
list_of_flat_pitches = [ 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B' ]
list_of_sharp_pitches = [ 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B' ]

# const
NUMBER_OF_PITCHES = len( list_of_flat_pitches )

def get_valid_pitch_input( message ):
	the_input = ''
	# will break when valid input is entered
	while( True ):
		the_input = input( message )

		# the input must be a valid input and not empty because that's the terminating condition
		if( the_input and regulate_to_flat( the_input ) not in list_of_flat_pitches ):
			print( '%s is not a note in the twelve tone scale, try again...\n' % the_input )
		else:
			break
	return the_input

def regulate_to_flat( pitch ):
	# if it has a sharp, return the element of same index from the flat pitch list
	# otherwise, the element should be the same in the other list anyways so just return it
	if( pitch in list_of_sharp_pitches and '#' in pitch ):
		return list_of_flat_pitches[ list_of_sharp_pitches.index( pitch ) ]
	else:
		return pitch

transposing_from = get_valid_pitch_input( 'What key are you transposing from?\n' )
tranposing_to = get_valid_pitch_input( 'What key are you transposing into?\n' )
print()
print( 'Transposing from the key of %s into the key of %s.' % ( transposing_from, tranposing_to ) )
print()

# must regulate to flat to ensure that it will be in the list of pitches with flats
index_of_original_key = list_of_flat_pitches.index( regulate_to_flat( transposing_from ) )
index_of_new_key = list_of_flat_pitches.index( regulate_to_flat( tranposing_to ) )

# offset is the distance between the two notes
offset = ( index_of_original_key - index_of_new_key ) % NUMBER_OF_PITCHES
# print( 'DEBUGGING: offset is ' + str( offset ) )

# main loop
while True:
	pitch = get_valid_pitch_input( 'Which note would you like to tranpose? (input nothing to quit)\n' )

	# base case: exit if no input
	if not pitch:
		break

	index_of_pitch = list_of_flat_pitches.index( regulate_to_flat( pitch ) )
	index_of_new_key_pitch = ( index_of_pitch + offset ) % NUMBER_OF_PITCHES

	the_new_pitch = ''
	# these lines allow the pitch to use either sharp or flat version depending on which one the input used
	if( '#' in pitch ):
		the_new_pitch = list_of_sharp_pitches[ index_of_new_key_pitch ]
	else:
		the_new_pitch = list_of_flat_pitches[ index_of_new_key_pitch ]

	print( '%s in key of %s --> %s in key of %s.\n' % ( pitch, transposing_from, the_new_pitch, tranposing_to ) )