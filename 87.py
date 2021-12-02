content = input("Content : ")
tag = input("Tag : ")

output = f"<{tag}>{content}</{tag}>"

open("Home.html","w").write(output)
print("done")
