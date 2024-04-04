"""Write a function makeHTMLTable(data) that when given a
 list of lists, it returns an HTML table of those values.

To make the output readable, we want a tab ("\t") before
 each <tr> and 2 tabs before each <td>.
"""


nums = [[1,2,3], [10], [12,15]]

def makeHTMLTable(listz):
    end = "<table>\n"
    for list in listz:
        end += "    <tr>\n"
        for item in list:
            end += f"        <td>{item}</td>\n"
        end += "    </tr>\n"
        
    end += "</table>"
    return end

print(makeHTMLTable(nums))
