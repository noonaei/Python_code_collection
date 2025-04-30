def cows_and_bools(word, guess):
    placement=[]
    bools=0
    almosts=[]
    for i in guess:
        if word[i] is guess[i]:
            bools+=1
            placement.append(index(i)+1)
            print(i+ " is in the word, in the right place")

        elif word[i] in guess:
            print(i+ " is in the word but somewhere else")
            almosts.append(i)
    if bools>0: print(f" you've got {bools} bools in letters: {placement}" )
    if len(almosts)>0: print(f"the letters {alomsts} also apear but not quite there")


cows_and_bools("rouge","right")
