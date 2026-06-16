class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        
        def parse(i):
            counter = defaultdict(int)
            
            while i < len(formula):
                if formula[i] == '(':
                    nested_counter, i = parse(i + 1)
                    
                    multiplier = 1
                    start = i
                    while i < len(formula) and formula[i].isdigit():
                        i += 1
                    if i > start:
                        multiplier = int(formula[start:i])
                    
                    for element, count in nested_counter.items():
                        counter[element] += count * multiplier
                        
                elif formula[i] == ')':
                    return counter, i + 1
                    
                else:
                    start = i
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        i += 1
                    element = formula[start:i]
                    
                    count_start = i
                    while i < len(formula) and formula[i].isdigit():
                        i += 1
                    count = int(formula[count_start:i]) if i > count_start else 1
                    
                    counter[element] += count
            
            return counter, i
        
        counter = parse(0)[0]
        
        return ''.join(element + (str(count) if count > 1 else '') 
                      for element, count in sorted(counter.items()))
