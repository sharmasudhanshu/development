pip install yara-python  ### this installs yara-python (4.0.5)



root@anshuvm:~/yara# python test.py
[hello_yara]

root@anshuvm:~/yara# cat example.yara

rule hello_yara
{
   strings:
       $a = "hello yara"
       $b = "www.google.com"
   condition:
       $a or $b
}

rule caseInsensitiveTextExample
{
   strings:
       $a = "foobar" nocase
   condition:
       $a
}

root@anshuvm:~/yara# cat test.py
import yara
#rule = yara.compile(source='rule foo: bar {strings: $a = "lmn" condition: $a}')


rules = yara.compile('example.yara')
#matches = rules.match(data='www.google.com abcdefgjiklmnoprstuvwxyz')

matches = rules.match(filepath='test.txt')

#########################################################
now run as 
python test.py

if matches:

    print(matches)

