m = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] # verilen input

new_m = []
def flatten(x):
    for y in x:
        if isinstance(y, list):
            flatten(y)
        else:
            new_m.append(y)
flatten(m)
print(new_m)