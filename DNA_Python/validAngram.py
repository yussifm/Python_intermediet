# Check to see if two strings are anagrams
# anagrams are words with the same char and frequences


from collections import Counter


def anagram_checker(s1, s2):
    
    if(len(s1) != len(s2)):
        return False
    else:
        freq1 = {}
        freq2 = {}

        for ch in s1:
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
        for ch in s2:
            if ch in freq2:
                freq2[ch] += 1
            else:
                freq2[ch] = 1

        for key in freq1:
            if key not in freq2 or freq1[key] != freq2[key]:

                return False

        return True

# Implention type 1
def anagram_check_1(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        return sorted(s1) == sorted(s2)

# Implentation type 2
def anagram_check_2(s1,s2):
    if len(s1)!= len(s2):
        return False
    else:
        return Counter(s1) == Counter(s2)

if __name__ == "__main__":
    print(anagram_checker("danger", "garden"))
    print("-----------------------------")
    print(anagram_checker("wife", "fire"))
    print("-----------------------------")
    print(anagram_checker("girl", "boy"))
