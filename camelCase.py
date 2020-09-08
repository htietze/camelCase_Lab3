def camelcase(sentence):
    """ Convert sentece to camelCase """

    title_case = sentence.title() # uppercase first letter each word
    upper_camel_cased = title_case.replace(' ', '') #remove spaces
    #lowercase first letter, join string
    #slices don't produce index out of bounds errors
    #so works on empty strings
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)

if __name__ == '__main__':
    main()
    