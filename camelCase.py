def camelcase(sentence):
    """ Convert sentence to camelCase """

    title_case = sentence.title() # uppercase first letter each word
    upper_camel_cased = title_case.replace(' ', '') #remove spaces
    #lowercase first letter, join string
    #slices don't produce index out of bounds errors
    #so works on empty strings
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def display_banner():
    # Display program name in banner
    msg = 'camelCaseGenerator program'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')

def main():
    display_banner()
    print("This program changes sentences into camel case words!")
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()
