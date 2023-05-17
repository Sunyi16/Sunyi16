"""test2"""

num1 = 2;
num2 = None;
num3 = 10E5;
num4 = complex(10 , 2);
str1 = "空谷";
str2 = str1 + "幽兰";
str3 = "一行白鹭"\
        "上青天"

print(str2);
print(str3);
print('空谷\n"幽兰"');
print('空谷\n\t"幽兰"');
print(num4.real);
print(num4.imag);
print(num4.conjugate);
print(num1 * num3);
print(type(num1) , type(num2) , type(num3) , type(num4));
