# 异世界语言转换器  
  
这是一个用于将中文转换为某种特定规则下的发音符号的小程序，例如想要为某种异世界语言规定发音，又懒得编造各种词，或许可以尝试这个（）  
其原理很简单，根据文字的编码将其与一些声母韵母对应。dict文件的第一行即为规定的声母，第二行为韵母。  
通过names文件可以指定一些专有名词的翻译方式，并将其保留，例如人名、地名和一些组织的名称等。  
现在tst文件为输入，rst为输出，文件夹中提供了例子。  

（本来是用matlab写的，但是好像会有一些问题，所以想着用py吧。这也是我第一次写py，输入输出都不会，到处查了半天（），花了三个小时才写好这个，不过很高兴。）
