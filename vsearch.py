def search4vowels(phrase:str) -> set:
    """Return vowesl in a phrase"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    return set(vowels).intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of letters in a phrase"""
    return set(letters).intersection(set(phrase))
