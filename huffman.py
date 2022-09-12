from base64 import decode
from bz2 import compress
from requests import head
from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *
import os.path
import codecs

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the freqency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if other is None:
            return False
        return self.freq == other.freq and self.char == other.char

    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''

        if self.freq < other.freq:
            return True
        elif self.freq == other.freq:
            return self.char < other.char
        #return False

    def __gt__(self, other):
        if self.freq > other.freq:
            return True
        elif self.freq == other.freq:
            return self.char > other.char
        return False

    def __repr__(self):
        return "Node ---- Char: {0}, Freq: {1}".format(chr(self.char), self.freq)


# what about non ascii inputs?
#
def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file'''

    ascii_lst = [0] * 256
    f = open(filename)

    for i in f.read():
        ascii_lst[ord(i)] += 1
        #print(ord(i))
    f.close()

    #print(ascii_lst)
    return ascii_lst


def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    end_lst = OrderedList()

    for i in range(len(char_freq)):
        if char_freq[i] == 0:
            continue
        else:
            #print("Ascii value for", chr(i), "is:", i, ' w/freq: ', char_freq[i])
            Nunode = HuffmanNode(i, int(char_freq[i]))
            end_lst.add(Nunode)

    while end_lst.size() > 1:
        lowest1 = end_lst.pop(0)
        lowest2 = end_lst.pop(0)

        #print("Lower node 1: ", lowest1, "Lower node 2: ", lowest2)

        nuFreq = int(lowest2.freq) + int(lowest1.freq)


        if lowest1.char < lowest2.char:
            nuNode = HuffmanNode(lowest1.char, nuFreq)
        else:
            nuNode = HuffmanNode(lowest2.char, nuFreq)

        nuNode.left = lowest1
        nuNode.right = lowest2
        #print("Adding parent node:", nuNode, "\n")
        #print("NuNode: ", nuNode)
        end_lst.add(nuNode)

    '''
    print('root node ascii: ', chr(end_lst.python_list()[0].char))
    print('root node freq: ', end_lst.python_list()[0].freq)

    print('root node left ascii: ', chr(end_lst.python_list()[0].left.char))
    print('root node left freq: ', end_lst.python_list()[0].left.freq)

    print('root node right ascii: ', chr(end_lst.python_list()[0].right.char))
    print('root node right freq: ', end_lst.python_list()[0].right.freq)

    print('root node right right ascii: ', chr(end_lst.python_list()[0].right.right.right.char))
    print('root node right right freq: ', end_lst.python_list()[0].right.right.right.freq)

    print('root node right left ascii: ', chr(end_lst.python_list()[0].right.left.char))
    print('root node right left freq: ', end_lst.python_list()[0].right.left.freq)
    '''

    return end_lst.pop(0)


def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    res = [0]*256
    code = ''
    code_helper(node, res, code)
    return res

def code_helper(node, res, code):

    if node.left is not None:
        code_helper(node.left, res, code + '0')
    if node.right is not None:
        code_helper(node.right, res, code + '1')

    if node.left is None and node.right is None:
        res[node.char] = code
        return
        #print("we've hit a bottom node! ", code, node.char)


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    result_str = ""
    for i in range(len(freqs)):
        if freqs[i] == 0:
            continue
        else:
            result_str += str(i) + ' ' + str(freqs[i]) + ' '

    result_str = result_str[0:len(result_str)-1]
    #result_str.strip()
    #file_out = open('FileOutput.txt', 'w')
    #file_out.write(result_str)
    #file_out.close()
    return result_str

def compress_name(file_name):
    return file_name[0:len(file_name)-4] + "_compressed.txt"

def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''

    ''' This section creates our occurances per character and then the respective huffman tree '''
    freqlist = cnt_freq(in_file)
    hufftree = create_huff_tree(freqlist)
    codes = create_code(hufftree)

    mapped_str = ""

    file_in = open(in_file, 'r')
    for i in file_in.read():
        mapped_str += codes[ord(i)]
    file_in.close()

    header_str = create_header(freqlist)

    ''' This writes our uncompressed file'''
    file_out = open(out_file, 'w')
    file_out.write(header_str)
    file_out.write('\n')
    file_out.write(mapped_str)
    file_out.close()

    ''' This writes our compressed file '''
    compressed_name = compress_name(out_file)
    compresso = HuffmanBitWriter(compressed_name)
    compresso.write_str(header_str)
    compresso.write_str('\n')
    for i in mapped_str:
        compresso.write_code(i)
    compresso.close()
    return


#huffman_encode("file1.txt", "file1_out_try.txt")

def parse_header(header_str):
    res_str = header_str.split(' ')
    #print('res str: ', res_str)
    cnt = 0
    ascii_val = 0
    freq_list = [0]*256
    for i in res_str:
        if cnt == 0: # first value is always ascii val of character which is the index of the freqlist
            ascii_val = int(i)
            cnt += 1
            continue
        elif cnt == 1:
            freq_list[ascii_val] = i # the wnd value is the occurance count
            cnt = 0
    return freq_list


def huffman_decode(encoded_file, decoded_file):
    if os.path.exists(encoded_file) == False:
        raise FileNotFoundError

    decode_bits = []
    to_decode = HuffmanBitReader(encoded_file)
    decoded_header = to_decode.read_str()
    decoded_header = decoded_header.decode('utf-8')
    decoded_header = decoded_header.rstrip()

    actual_freqlist = parse_header(decoded_header)

    total_num_of_letters = 0
    for freq in actual_freqlist:
        if freq != 0:
            total_num_of_letters += int(freq)
        elif freq == 0:
            pass

    capacity = 0
    while capacity != total_num_of_letters:
        decode_bits.append(str(to_decode.read_bit()))
        capacity += 1

    decode_bits_str = ""

    for i in decode_bits:
        if i == "True":
            decode_bits_str += "1"
        elif i == "False":
            decode_bits_str += "0"

    #print(decode_bits_str)

    nuTree = create_huff_tree(actual_freqlist)

    #print(nuTree.right.right)
    write_to_decoded = tree_follower(decode_bits_str, nuTree, total_num_of_letters)
    
    ''' This writes our decompressed file'''
    file_out = open(decoded_file, 'w')
    #file_out.write(decoded_header)
    #file_out.write('\n')
    file_out.write(write_to_decoded)
    file_out.close()

def tree_follower(binary_str, huff_tree, total_char):
    changing_tree = huff_tree
    res_str = ""
    #print('binary str: ', binary_str)
    for direction in binary_str:
        #print(changing_tree)
        if direction == '0':
            changing_tree = changing_tree.left
        elif direction == '1':
            changing_tree = changing_tree.right
        if changing_tree.left is None and changing_tree.right is None:
            #total_char -= 0'
            #print('we restarted & adding: ', chr(changing_tree.char))
            res_str += chr(changing_tree.char)
            changing_tree = huff_tree        

    return res_str


#huffman_decode("file_WAP_out_compressed.txt", "file_WAP_try.txt")

