s[0]
s[5]
s[:-2]
s[1:-2]
s[4:]
s.reverse()


l = [3, 7, [1, 4, 'hello']]
l[2][2] = "goodbye"


d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
d1["simple_key"]
d2["k1"]["k2"]
d3["k1"][0]["nest_key"][1][0]


print("Hello my dog's name is " + name + " and he is " + age + " years old")
