'''
Count Character Frequency Example: "selenium" → {'s':1, 'e':2, ...}
'''


def characterfrequency():
    S="Selenium"

    frequency = {}

    for i in S:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    for key,value in frequency.items():
        print(f"CharacterKey is {key},frequency is {value}")

characterfrequency()








