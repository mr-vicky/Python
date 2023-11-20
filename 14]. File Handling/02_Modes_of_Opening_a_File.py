file = open("modesDemo.txt", "w")

file.write("We are writing in this file using write mode!\n")
file.write("using write mode...\n")
file.write("using write mode...\n")
file.write("using write mode...\n")
file.write("using write mode...\n")
file.write("using write mode...\n")
file.write("using write mode...\n")
file.write("using write mode...\n")


file.close()

file = open("modesDemo.txt", "a")

file.write("\n\nThis is written by using append mode...")
file.write("using append mode...\n")
file.write("using append mode...\n")
file.write("using append mode...\n")
file.write("using append mode...\n")
file.write("using append mode...\n")
file.write("using append mode...\n")

for i in range(0, 100):
    file.write("using append mode...\n")

file.close()