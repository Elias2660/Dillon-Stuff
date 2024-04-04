#problem  1
def make_stupid_table(n):
    out = "<table>\n"
    for x in range(n): out += f"<tr><td>{x}</td></tr>\n"
    return out + "</table>"

#print(make_stupid_table(5))


#problem 2
def make_less_stupid_table(n):
    out = "<tr><th>Number</th><th>Square</th></tr>\n"
    for x in range(n): out += f"    <tr><td>{x}</td><td>{x**2}</td></tr>\n"
    return out + "</table>"


#print(make_less_stupid_table(4))


#problem 3
def make_poly_tab(low, high):
    out = "<table>\n "" <tr><th>Number</th><th>y = x^2 + 2x + 3</th></tr>\n"
    for x in range(low, high + 1): out += f"    <tr><td>{x}</td><td>{x**2 + 2*x + 3}</td></tr>\n"
    return out + "</table>"

print(make_poly_tab(-2,2))

