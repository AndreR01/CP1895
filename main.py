def main():
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    i = 0
    for name in animals.values():
        print(name)
        for value in name:
            i+=1
            print(value)
    print(i)
    # total = (len(name))
    # print(total)
    print(animals)

if __name__ == "__main__":
    main()
