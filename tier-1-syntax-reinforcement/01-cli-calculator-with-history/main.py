y = "stop"
z = "timeline"
results = []
timeline = []
operators = ['+','-','*','\\']
print("""Welcome to the Calculator!
      Use the following commands to run:
      - type in a calculation + enter -> gives solution & stores result
      - stop -> ends program
      - rn -> prints n'th result
      - timeline -> Prints calculation history""")
      
while True:
    x = input("Enter to calculate")
    if x==z or x==y or x.isdigit() or all(i.isdigit or i in operators for i in x) or x[x.index('r')+1].isdigit():
        if x!=z:
            timeline.append(x)
        if x == y:
            break
        if x == z:
            print(timeline)
        
        if "r" in x:
            i = x.index('r')+1
            while i<len(x) and x[i].isdigit():
                i+=1
            b = x.replace(x[x.index('r'):i],str(results[int(x[x.index('r')+1:i])]))
            print(eval(b))
        else:
            print(eval(x))
            results.append(eval(x))
            print(results)
    else:
        print("Enter a valid argument")
