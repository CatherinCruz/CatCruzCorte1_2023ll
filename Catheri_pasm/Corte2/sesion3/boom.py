def boom(x):
    if x>0:
        print(x)
        boom(x-1)
        #pass
    else:
        print('boooom!')
    print(f'finalizo{x}')


def main():
    boom(5)


if __name__=='__main__':
    main()