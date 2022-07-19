import ast
def save(book,key,num):
    path = 'record'+str(book)+'.txt'
    with open(path,'a+',encoding='utf-8') as file:
        a=ast.literal_eval(file.read())
        a[key]=num
    with open(path,'w',encoding='utf-8') as file:
        file.write(str(a))
def read(book):
    path = 'record' + str(book) + '.txt'
    with open(path, 'a+', encoding='utf-8') as file:
        a = ast.literal_eval(file.read())
    return a

save(1,0,0)
print(read(1))