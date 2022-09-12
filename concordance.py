from msilib.schema import File
from hash_quad import *
import string
import os.path

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def is_punctuation_or_number(self, string_):
        for char in string_:
            if char.isnumeric():
                return True
            if char in string.punctuation:
                return True
        return False

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        if not os.path.exists(filename):        
            raise FileNotFoundError
        file = open(filename, 'r')
        self.stop_table = HashTable(191)
        for i in file.readlines():
            self.stop_table.insert(i[:len(i)-1], None)
        file.close()
        #print(self.stop_table.hash_table)


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        if not os.path.exists(filename):        
            raise FileNotFoundError
        line_number = 1
        file = open(filename, 'r')
        self.concordance_table = HashTable(191)
        for i in file.readlines():
            if "\n" not in i:
                i = i
            else:
                i = i[:len(i)-1] # remove the '\n' suffix
            listt = i.split()
            for j in listt: # listt will break 'a b c' into ['a', 'b', 'c']
                j = j.lower()
                #print('such is not getting picked up at 22, 23: ', j, line_number)
                for char_ in j:
                    if not char_.isalpha() and char_ not in ['"', "'", "-"]:
                        j = j.replace(char_, '')
                if '"' in j:
                    j = j.replace('"','')
                if "'" in j:
                    j = j.replace("'", '')
                if self.stop_table.in_table(j.lower()):
                    continue
                if "-" in j:
                    hyphen_list = j.split('-')
                    #print('hyphen list: ', hyphen_list)
                    for word_ in hyphen_list:
                        if not word_.isalpha():
                            continue
                        if self.concordance_table.in_table(word_.lower()):
                            value = self.concordance_table.get_value(word_.lower())
                            most_recent_line_number = value.split()[-1]
                            if most_recent_line_number == str(line_number):  # if it's a repeated word in the same line
                                continue
                            value += " " + str(line_number)  # take the previous value and add it with the new line
                            idx_where_it_repeats = self.concordance_table.get_index(word_.lower())
                            self.concordance_table.hash_table[idx_where_it_repeats][1] = value
                            continue
                        self.concordance_table.insert(word_.lower(), str(line_number))
                    continue
                #print('do we get here, j, line number: ', j, line_number)
                #print('does such get here?: ', j, line_number)
                #print(self.concordance_table.hash_table)
                if self.concordance_table.in_table(j.lower()): # if the data is already in the table
                    #print('already in table!')
                    value = self.concordance_table.get_value(j.lower())
                    most_recent_line_number = value.split()[-1]
                    if most_recent_line_number == str(line_number): # if it's a repeated word in the same line
                        #print('does such at line 32 thinks it is the same line?')
                        continue
                    value += " " + str(line_number) # take the previous value and add it with the new line
                    idx_where_it_repeats = self.concordance_table.get_index(j)
                    #print('table couple at repeat idx: ', self.concordance_table.hash_table[idx_where_it_repeats])
                    #print('idx where it repeats: ', idx_where_it_repeats, j, " value to be inserted: ", value )
                    self.concordance_table.hash_table[idx_where_it_repeats][1] = value
                    #print('table value post assignment: ', self.concordance_table.hash_table[idx_where_it_repeats])
                    continue
                if not j.isalpha():
                    continue
                self.concordance_table.insert(j.lower(), str(line_number)) # this will give us values like '1 3 14' so .split() values to obtain each line number
            line_number += 1

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        file = open(filename, 'w')
        alphabetical_idx = []
        for i in self.concordance_table.hash_table:
            if i is not None:
                alphabetical_idx.append(i[0] + " " + str(self.concordance_table.get_index(i[0])))

        alphabetical_idx = sorted(alphabetical_idx)
        #print('sorted: ', alphabetical_idx)
        #print('first val of alph idx: ', alphabetical_idx[0])
        size = len(alphabetical_idx)
        count = 0
        for i in alphabetical_idx:
            listt = i.split()
            idx_listt = int(listt[1])
            if count == size - 1:
                result_str = self.concordance_table.hash_table[idx_listt][0] + ': ' + self.concordance_table.hash_table[idx_listt][1]
            else:
                result_str = self.concordance_table.hash_table[idx_listt][0] + ': ' + self.concordance_table.hash_table[idx_listt][1] + '\n'
            file.write(result_str)
            count += 1

        file.close()

