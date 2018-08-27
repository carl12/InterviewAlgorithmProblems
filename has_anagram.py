# Anagram
# Given two strings s and t, determine whether some anagram of t
# is a substring of s. For example: if s = "udacity" and t = "ad",
# then the function returns True. Your function definition should
# look like: question1(s, t) and return a boolean True or False.

'''
There are several different functions, which all give the correct output. Has_anagram2 
is my first attempt which runs normally in linear time. The only issue is that the function
completely reinitializes the dictionary every time it finishes a series of valid characters. 
That means that the function might run in O(mn) time if many of the characters in the long 
string are found in the substring seperated by characters which are not in the substring. 
I created has_anagram3 with cleaner logic and which sequentially re-increments values into 
the dict. That means the function runs in linear time even on bad inputs. 
    
Despite this better theoretical runtime, has_anagram2 appears to run faster even on 'bad input'
when the substring size is small. If the strings are given max sizes of 1000, and 100, however, 
has_anagram3_2 outperforms it. 

One thing that is more optimal about has_anagram2 is that is does not increment anything
if correct value is found. This will be the majority of cases, so it might explain it 
running faster. However, keeping a running value of start makes more intuitive sense to 
me than changing it from None to a value. It simulates the window moving forwards.
'''



from itertools import permutations
from functools import reduce
import random
import string
import f_timer
# Simple function that will take a string of latin characters and return a unique hash
def hashString(str):
  # Map characters to prime numbers to multiply
    charMap = {
    'a': 2,
    'b': 3,
    'c': 5,
    'd': 7,
    'e': 11,
    'f': 13,
    'g': 17,
    'h': 19,
    'i': 23,
    'j': 29,
    'k': 31,
    'l': 37,
    'm': 41,
    'n': 43,
    'o': 47,
    'p': 53,
    'q': 59,
    'r': 61,
    's': 67,
    't': 71,
    'u': 73,
    'v': 79,
    'w': 83,
    'x': 89,
    'y': 97,
    'z': 101,
    'A': 103,
    'B': 107,
    'C': 109,
    'D': 113,
    'E': 127,
    'F': 131,
    'G': 137,
    'H': 139,
    'I': 149,
    'J': 151,
    'K': 163,
    'L': 167,
    'M': 173,
    'N': 179,
    'O': 181,
    'P': 191,
    'Q': 193,
    'R': 197,
    'S': 199,
    'T': 211,
    'U': 223,
    'V': 227,
    'W': 229,
    'X': 233,
    'Y': 239,
    'Z': 241
  }

    return reduce(lambda memo, char: memo * charMap[char], list(str), 1);

def has_anagram4(parent, child):
    '''
    Code and helper function from 
    '''
    length = len(child)
    anagram = hashString(child)
    total = 0

    for i in range(0, len(parent) - length + 1):
        if hashString(parent[i: i + length]) == anagram:
            total = total + 1
    # print(total)
    return total > 0



def has_anagram2(s, t, debug = False):
    # make a hashmap of all characters in t
        # all characters map to the number of that character in t
    # for each char in s
        # if that char is in t, decrement the hashmap
    # Check to see if all values in hashmap are less than zero

    if len(t) == 0:
        return True

    if len(s) < len(t):
        return False


    char_map = {}
    for c in t:
        if char_map.get(c):
            char_map[c] += 1;
        else:
            char_map[c] = 1

    char_map_copy = char_map.copy()

    start = None
    for i,c in enumerate(s):
        
        # print(c)
        # if start:
            # print(i - start)
        # print('---')
        if start is not None:
            # print(i,start,char_map_copy)
            # print(char_map_copy)
            if char_map_copy.get(c) is not None and char_map_copy[c] <= 0:
                # print('asdf',i,s[start])
                while start <= i:
                    char_map_copy[s[start]]+=1
                    start+=1
                    # print(char_map_copy)
                    if c == s[start-1]:
                        break
                char_map_copy[c] -= 1
            elif char_map_copy.get(c) is None:
                start = None
                char_map_copy = char_map.copy()
            else: 
                char_map_copy[c] -= 1
        elif char_map_copy.get(c) is not None:
            start = i
            char_map_copy[c] -= 1

        if (start is not None) and i-start == len(t)-1:
            # print(start,i,char_map)
            # print(i,start,char_map_copy)
            # print(i)
            if(debug):
                print(i)
            return True



    return False

def has_anagram3(s,t, debug = False):
    if t is None or len(t) == 0:
        return True
    if s is None or len(s) == 0:
        return False

    # Build hash tracker
    track = {};
    for c in t:
        if(track.get(c)):
            track[c] += 1
        else:
            track[c] = 1

    #Init place values
    start = 0
    curr = 0
    anLen = len(t)
    track = track

    while(curr < len(s)):
        c = s[curr]
        if debug and curr != start:
            print('---------')
            print(curr, start)
            print(s[start:curr])
            print(track)

        if track.get(c) is not None:
            if track[c] > 0:
                track[c] -= 1
            elif track[c] == 0:
                while(track[c] == 0 and start < curr):

                    track[s[start]] += 1
                    start+=1
                track[c] = 0

        else:
            while(start < curr):
                track[s[start]] += 1
                start += 1
            # track = trackOg.copy()
            start = curr+1

        if curr - start == anLen - 1:
            if debug: print(curr)
            return True

        curr += 1

    return False

def has_anagram3_2(s,t, debug = False):
    if t is None or len(t) == 0:
        return True
    if s is None or len(s) == 0:
        return False

    # Build hash tracker
    trackOg = {};
    for c in t:
        if(trackOg.get(c)):
            trackOg[c] += 1
        else:
            trackOg[c] = 1

    #Init place values
    start = 0
    curr = 0
    anLen = len(t)
    track = trackOg.copy()

    for i,c in enumerate(s):
        # c = s[i]
        if debug and i != start:
            print('---------')
            print(i, start)
            print(s[start:i])
            print(track)

        if track.get(c) is not None:
            if track[c] > 0:
                track[c] -= 1
            elif track[c] == 0:
                while(track[c] == 0 and start < i):
                    track[s[start]] += 1
                    start+=1
                track[c] = 0

        elif start == i:
            start += 1
        else:
            track = trackOg.copy()
            start = i+1

        if i - start == anLen - 1:
            if debug: print(i)
            return True


    return False

def gen_rand_str(maxLong, maxSub):
    len_long = random.randint(0,maxLong)
    len_sub = random.randint(0,maxSub)

    str_long = ''.join(random.choices(string.ascii_lowercase, k=len_long))
    str_sub = ''.join(random.choices(string.ascii_lowercase, k=len_sub))

    return (str_long, str_sub)

def gen_bad_str(maxLong, maxSub):
    return ['ab'*maxLong, 'a'*maxSub]


print(f_timer.time_funcs([ has_anagram2, has_anagram3, has_anagram3_2],gen_rand_str, [1000,11],10000))


# s1 = "vmdnmfaxkqbhxvvrcgwtjvnumpsrfkofnwbnmjbelkxmwefdkweerdppxvepbxqsqqoczleuoemizwgznrlpzzaeylxizuhgkkslmlfnrspbgoodqricguajnagngvylahrduquyrcdhpptkyyotyjyfaplifutjgncfjwgyfnmztjurbikhqduvjurkbqrhgdtgxurkkfgglduifllccyewlofsaeeetmdoivuliortwkjxrrmbwbfodnfttvgmdkitkhpvqrhrhrqodlguacxzuiybkmxddikzwdvprtxtwkabsdaixjpiwskkepklqxdicqtddvtimufrmyoygh"
# print(len(s1))
# s12 = s1[338:342]
# print(s12)
# s2 = "yogh"

# print(has_anagram1(s12,s2))
# print(has_anagram2(s12,s2,))
# print(has_anagram3(s12,s2,))
# print(has_anagram4(s12,s2,))
