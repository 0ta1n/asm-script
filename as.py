import  subprocess


x = input()
y = " nasm -f elf64 " + x +".asm"
z =" ld -m elf_x86_64 -o " + x +" " + x +".o"  

outputY = subprocess.getoutput(y)
outputZ = subprocess.getoutput(z)

print(outputY)
print (outputZ)
