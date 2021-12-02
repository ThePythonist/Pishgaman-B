info = [
    {"Name":"Navid Mohammadzadeh","Job":"Actor","Age":"35"},
    {"Name":"Asghar Farhadi","Job":"Director","Age":"49"},
    {"Name":"Ebi","Job":"Singer","Age":"72"}
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #40aa77;
  color: white;
}
</style>
</head>
<body>

<table id="customers">
    <tr>
    <th>Name</th>
    <th>Job Title</th>
    <th>Age</th>
    </tr>
"""

for person in info :
    html += """
    <tr>
    <td>{Name}</td>
    <td>{Job}</td>
    <td>{Age}</td>
    </tr>
    """.format(
        Name=person["Name"],
        Age=person["Age"],
        Job=person["Job"]
               )

html += """
</table>
</body>
</html>
"""

open("Info.html","w").write(html)
print("Done")
