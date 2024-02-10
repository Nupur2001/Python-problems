'''
Calculate the Hamming difference between two DNA strands.

A mutation is simply a mistake that occurs during the creation or copying of a nucleic acid, in particular DNA. Because nucleic acids are vital to cellular functions, mutations tend to cause a ripple effect throughout the cell. Although mutations are technically mistakes, a very rare mutation may equip the cell with a beneficial attribute. In fact, the macro effects of evolution are attributable by the accumulated result of beneficial microscopic mutations over many generations.

The simplest and most common type of nucleic acid mutation is a point mutation, which replaces one base with another at a single nucleotide.

By counting the number of differences between two homologous DNA strands taken from different genomes with a common ancestor, we get a measure of the minimum number of point mutations that could have occurred on the evolutionary path between the two strands.

This is called the 'Hamming distance'

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
The Hamming distance between these two DNA strands is 7.

Implementation notes
The Hamming distance is only defined for sequences of equal length. Hence you may assume that only sequences of equal length will be passed to your hamming distance function.

Note: This problem is deprecated, replaced by the one called hamming.

Test cases:
Test: No Difference Between Empty Strands

Test: No Difference Between Identical Strands

Test: Complete Hamming Distance In Small Strand

Test: Hamming Distance In Off By One Strand

Test: Small Hamming Distance In Middle Somewhere

Test: Larger Distance

Test: Ignores Extra Length On Other Strand When Longer

Test: Ignores Extra Length On Original Strand When Longer
'''


import time
def hamming_distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError("Invalid Strand Length Error")
    if len(strand1) == 0 or len(strand2) == 0:
        raise ValueError("Empty Strand Error")

    distance = sum(c1 != c2 for c1, c2 in zip(strand1, strand2))
    matching_frequency = len(strand1) - distance
    return matching_frequency

original_strand = input("Enter strand 1:\n")
comparison_strand = input("Enter strand 2:\n")

start_time = time.time()


try:
    result = hamming_distance(original_strand, comparison_strand)
    print('The matching frequency between "{}" and "{}" is {}'.format(original_strand, comparison_strand, result))

except ValueError as e:
    print(e)



end_time = time.time()
execution_time = end_time - start_time
print("Execution Time: {:.6f} seconds".format(execution_time))