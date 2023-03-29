
import argparse

def main():
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", type=str, dest="prova", help="prova comando", action="store", required=True)
    parser.add_argument("-d", type=str, help="prova comando bis", required=True)

    args = parser.parse_args()
    #     x = args.d # errore
    x = args.prova # non errore perche' ho impostato args.prova, mediante dest, come variabile di salvataggio
    print(f"gli argomenti sono {args.prova} e {args.d}")

    return 0



if __name__ == '__main__':
    main()

'''
% python3 trydest.py -p prova -d prova2
gli argomenti sono prova e prova2
'''
