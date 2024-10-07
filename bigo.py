"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Nathaniel Roe, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: nr25328
"""


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """

    length = 0
    longest_length = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            frequency_list = [0] * 256
            substring = s[i:j + 1]
            for elem in substring:
                numerical_element = ord(elem)
                frequency_list[numerical_element] += 1
                length = j - i + 1
                if length > longest_length:
                    longest_length = length


    return longest_length
            
            
            



# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """


    longest_length = 0
    for i in range(len(s)):
        length = 0
        frequency_list = [0] * 256
        for j in range(i, len(s)):
            numerical_element = ord(s[j])
            frequency_list[numerical_element] += 1 
            length += 1
            if length > longest_length:
                    longest_length = length

    return longest_length
            



# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """

    longest_length = 0
    for i in range(len(s)):
        length = 0
        frequency_list = [0] * 256
        for j in range(i, len(s)):
            numerical_element = ord(s[j])
            frequency_list[numerical_element] += 1
            if frequency_list[numerical_element] > 1:
                    break
            else:
                length += 1
                if length > longest_length:
                        longest_length = length

    return longest_length
            








            
