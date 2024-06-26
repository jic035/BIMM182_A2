import argparse
from randomDNA import generate_pairs
from locAL import LocalAlignment

def process_pairs(pairs, match, mismatch, indel):
    results = []
    for seq1, seq2 in pairs:
        score, aligned_seq1, aligned_seq2 = LocalAlignment(seq1, seq2, match, mismatch, indel)
        results.append((score, aligned_seq1, aligned_seq2))
    return results

def main():
    parser = argparse.ArgumentParser(description="Generate random DNA pairs and align them.")
    parser.add_argument('number_of_pairs', type=int, help="Number of pairs of sequences to generate and align")
    parser.add_argument('length_of_seq', type=int, help="Length of each sequence in a pair")
    parser.add_argument('-m', '--match', type=float, default=1, help='Match reward')
    parser.add_argument('-s', '--mismatch', type=float, default=-1, help='Mismatch penalty')
    parser.add_argument('-d', '--indel', type=float, default=-1, help='Indel penalty')
    parser.add_argument('-o', '--output', type=str, default="./Alignment_out/results.txt", help='Output file for alignment scores')

    args = parser.parse_args()
    sequence_pairs = generate_pairs(args.number_of_pairs, args.length_of_seq)
    alignment_results = process_pairs(sequence_pairs, args.match, args.mismatch, args.indel)
    
    filename = './Alignment_out/' + args.output
    with open(filename, 'w') as file:
        for i, (_, alignment, _) in enumerate(alignment_results):
            file.write(f"Pair {i+1}: Length = {len(alignment)}\n")

if __name__ == "__main__":
    main()
