# Anagram
# Given two strings s and t, determine whether some anagram of t
# is a substring of s. For example: if s = "udacity" and t = "ad",
# then the function returns True. Your function definition should
# look like: question1(s, t) and return a boolean True or False.



from itertools import permutations
import random
import string
import f_timer


def has_anagram1(s, t):

    # We confirm that s is longer than t.
    # If not, we know it cannot be a substring.
    if (len(t) > len(s)):
        return False

    # Convert to lowercase so this function is not case-sensitive.
    s = s.lower()
    t = t.lower()

    t = list(t)
    for j in permutations(t):
        if ''.join(j) in s:
            return True

    return False

def has_anagram2(s_raw,t_raw):
    # make a hashmap of all characters in t
        # all characters map to the number of that character in t
    # for each char in s
        # if that char is in t, decrement the hashmap
    # Check to see if all values in hashmap are less than zero

    if len(t_raw) == 0:
        return True

    if len(s_raw) == 0:
        return False

    s = s_raw.lower()
    t = t_raw.lower()

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
        elif char_map_copy.get(c):
            start = i
            char_map_copy[c] -= 1

        if (start is not None) and i-start == len(t)-1:
            # print(start,i,char_map)
            # print(i,start,char_map_copy)
            return True



    return False


def gen_rand_str(maxLong, maxSub):
    len_long = random.randint(0,maxLong)
    len_sub = random.randint(0,maxSub)

    str_long = ''.join(random.choices(string.ascii_lowercase, k=len_long))
    str_sub = ''.join(random.choices(string.ascii_lowercase, k=len_sub))

    return (str_long, str_sub)


print(f_timer.time_funcs([has_anagram1, has_anagram2],gen_rand_str, [1000,11],10000))
# a = 'haqlkwbocnxjvfqbulrzvvvkfmtcceknszwvjaznqybyrqrjdybwpobcuegtlevnxcvgngeiwcgainuydkaywctchcqwqlbidoamhuazrvcpwotnwicogzcfkycblzyyogrtptvpuunuxhokmqcwkmzedjunilhiasgewwykludsocjfhsenolrlejoyryqkjyoehadepksfnxjulzmzcaeugypcrimmioszxgyiibdzccjhnfzsjfysofwcsuwdlaxmimzprmuooyrkwsebacmnmwahgiqgmprzyycybojxlycgafgvupvzwzfdkewdrawrfpxckxfddlhonluzkqsvmvzwvkrbyofohtveiqqiwzqfurwiyoczfggzijanbywiutkxgpvzjvkkweukuetkzhuvemnzefkhptjoxfjvpkhdjixpdjodplyterovywjmtooqpasjswcscqspoarpwgwpbhcwkwimlqidqqbvebrrnpvbsqozdercaivpkuiuxnohrilaqwznhqjxggcypstyesbzosdg'
# print(len(a))
# c = a[290:296]
# print(c)
# b = 'ecy'
# print(has_anagram2(c,b))
# print(has_anagram1(c,b))

# print(has_anagram2('qpxpqo','poxq'))

# 'abcbda','abc'