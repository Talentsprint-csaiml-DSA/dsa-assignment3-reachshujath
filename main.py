# Implement huffman coding
import heapq
from collections import Counter

def huffman_coding(input_string):
    # Count frequency of each character in the input string
    freq_tab = dict(Counter(input_string))
    huff_tree = [[freq, [char,""]] for char, freq in freq_tab.items()]
    # print(huff_tree)

    # Build a Huffman Tree based on the character encodings
    heapq.heapify(huff_tree)
    # print(f"Original Heap: \n {huff_tree}")

    while len(huff_tree) > 1:
        # pull out the lowest two nodes
        low1 = heapq.heappop(huff_tree)
        low2 = heapq.heappop(huff_tree)

        # print(f"Low 1 = {low1}")
        # print(f"Low 2 = {low2}")

        # Append the 0 code for the left and right branches
        for pair in low1[1:]:
            pair[1] = "0" + pair[1]

        for pair in low2[1:]:
            pair[1] = "1" + pair[1]

        accrued_val = low1[0] + low2[0]
        heapq.heappush(huff_tree, [accrued_val] + low1[1:] + low2[1:])

        # print(f"After Heap Push of {accrued_val} and {low1[1:]} and {low2[1:]}")
        # print(f"Modified Heap: \n {huff_tree}")
    
# Generate Binary codes for the Character tree
    huff_tree = huff_tree[0][1:]
    # print(f"Final Huffman Codes: \n {huff_tree}")

# Encode the input string
    huff_codes = {char:code for char, code in huff_tree}
    # print(f"Final Huffman Codes: \n {huff_codes}")

    encoded_string = "".join(huff_codes[char] for char in input_string)
    # print(f"Encoded String of {input_string} is {encoded_string}")
    return encoded_string
    
# huffman_coding('Hi, I am here')