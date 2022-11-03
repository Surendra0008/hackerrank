def designerPdfViewer(h, word):
    # Write your code here
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']
    pairs = {}
    for i in range(26):
        pairs[alphabets[i]] = h[i]
    numbers = []
    for l in word:
        numbers.append(pairs.get(l))
        m = max(numbers)
        n = m*len(word)
    print(n) 
      
h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)