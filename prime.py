# prime.py

def prime():
    primes = [1, 2]

    while len(primes) < 100:
        prime = False
        n = 1
        while not prime:
            i = primes[-1] + n
            false = False
            for d in range(2, i-1):
                if i%d == 0:
                    false = True
            if not false:
                prime = True
                primes.append(i)
            else:
                n += 1
            
        
       

    return primes

def main():
    print('OUTPUT', prime())

if __name__ == "__main__":
    main()
