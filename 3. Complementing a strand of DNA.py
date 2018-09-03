def reversecomplement(dna):
""" allows you to find the reverse complement of the DNA input (in string form)"""
  dna1 = dna[::-1]
	dnaoutput = ''
  for let in dna1:
    if let == 'A':
      dnaoutput += 'T'
    elif let == 'T':
      dnaoutput += 'A'
    elif let == 'G':
      dnaoutput += 'C'
    else:
      dnaoutput += 'G'
  print(dnaoutput)
