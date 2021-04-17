Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nama = 'ucok'
>>> nama
'ucok'
>>> umur = 20
>>> print(nama,"berumur", umur,"tahun")
ucok berumur 20 tahun
>>> 
>>> print("Hello World!")
Hello World!
>>> 
>>> x = 9
>>> type(x)
<class 'int'>
>>> x = True
>>> type(x)
<class 'bool'>
>>> x = 'contoh'
>>> type(x)
<class 'str'>
>>> 
>>> x = 9
>>> id(x)
2067613641264
>>> 
>>> x = 9
>>> id(x)
2067613641264
>>> y = 9
>>> id(y)
2067613641264
>>> 
>>> y = 7
>>> id(y)
2067613641200
>>> 
>>> x = 9
>>> id(x)
2067613641264
>>> y = 9
>>> id(y)
2067613641264
>>> del y
>>> y
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> x
9
>>> id(x)
2067613641264
>>> x = True
>>> x
True
>>> 
>>> posisi = (300,300)
>>> posisi
(300, 300)
>>> Posisi
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Posisi
NameError: name 'Posisi' is not defined
>>> 
>>> a = 1; b = 2; c = 3
>>> print(a); print(b); print(c)
1
2
3
>>> 
>>> x = 9
>>> if isinstance(x,int) and \
   x > 0 and \
   x % 2 == 1:
	print("%d adalah bilangan bulat ganjil positif" %x)

	
9 adalah bilangan bulat ganjil positif
>>> 
>>> print("Pemrograman GUI" +
      "dengan Python dan PyQt")
Pemrograman GUIdengan Python dan PyQt
>>> data = [
	100,
	200,
	300
	]
>>> kamus = {
	'one':'satu',
	'two':'dua',
	'three':'tiga'
	}
>>> data
[100, 200, 300]
>>> kamus
{'one': 'satu', 'two': 'dua', 'three': 'tiga'}
>>> 
>>> #bilangan biner
>>> a = 0b1001
>>> #bilangan oktal
>>> b = 0o23
>>> #bilangan heksadesimal
>>> c = 0x2f
>>> a
9
>>> b
19
>>> c
47
>>> 
>>> a = True
>>> type(a)
<class 'bool'>
>>> int(a)
1
>>> 
>>> a = 15
>>> id(a)
2067613641456
>>> a += 5
>>> a
20
>>> id(a)
2067613641616
>>> 
>>> a = 123.456
>>> a
123.456
>>> a * 2
246.912
>>> 
>>> s1 = 'pemrograman python'
>>> s2 = "pemrograman python 2"
>>> s3 = '''pemrograman
	python 3'''
>>> 
>>> s1[0], s1[1], s1[2]
('p', 'e', 'm')
>>> 
>>> data = 'p001\tspidol\t\t9000\np002\tpensil\t\t6000'
>>> print(data)
p001	spidol		9000
p002	pensil		6000
>>> 
>>> data = '\tharga\n' + data
>>> print(data)
	harga
p001	spidol		9000
p002	pensil		6000
>>> 
>>> s1 = 'python'
>>> s2 = 'PYTHON'
>>> s1 == s2
False
>>> s1 != s2
True
>>> s1 < s2
False
>>> 
>>> s = 'Pemrograman Python dan PyQt'
>>> s1 = s[0:11]
>>> s1
'Pemrograman'
>>> len(s1)
11
>>> 
>>> s = s[:11]
>>> s = s[:8]
>>> s = s[8:]
>>> s = s[0:11:1]
>>> s = s[0:11:2]
>>> s = s[0:11:3]
>>> 
>>> s = 'balonku ada %d, kempes %d tinggal %f' % (5,1,4.5)
>>> s
'balonku ada 5, kempes 1 tinggal 4.500000'
>>> list = ['balon', 'budi', 'ada', 5]
>>> for item in list:
	print(item)

	
balon
budi
ada
5
>>> 
>>> del list[2]
>>> list
['balon', 'budi', 5]
>>> 
>>> list[1] = 'ada'
>>> list
['balon', 'ada', 5]
>>> 
>>> list.extend([loh])
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    list.extend([loh])
NameError: name 'loh' is not defined
>>> list.extend([6])
>>> list
['balon', 'ada', 5, 6]
>>> del list[3]
>>> list
['balon', 'ada', 5]
>>> list.extend(['loh'])
>>> list
['balon', 'ada', 5, 'loh']
>>> 
>>> s = 'balonku ada %d, kempes %d tinggal %f' % (5,1,4.5)
>>> s
'balonku ada 5, kempes 1 tinggal 4.500000'
>>> 
>>> hogwarts geng = [1, 'Harry','Hermione', 'Ron']
SyntaxError: invalid syntax
>>> hogwarts = [1, 'Harry','Hermione', 'Ron']
>>> hogwarts
[1, 'Harry', 'Hermione', 'Ron']
>>> del hogwarts[0]
>>> hogwarts
['Harry', 'Hermione', 'Ron']
>>> hogwarts[3] = 'Dumbledore'
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    hogwarts[3] = 'Dumbledore'
IndexError: list assignment index out of range
>>> hogwarts = [1,2,'Harry','Hermione','Ron']
>>> 
>>> hogwarts = [1,2,'Harry','Hermione','Ron']
>>> hogwarts
[1, 2, 'Harry', 'Hermione', 'Ron']
>>> del hogwarts[0]
>>> hogwarts
[2, 'Harry', 'Hermione', 'Ron']
>>> hogwarts[0] = 'Dumbledore'
>>> hogwarts
['Dumbledore', 'Harry', 'Hermione', 'Ron']
>>> hogwarts.extend(['Lily'])
>>> hogwarts
['Dumbledore', 'Harry', 'Hermione', 'Ron', 'Lily']
>>> 