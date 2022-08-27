from pprint import pprint 

class Write_doc:
    def __init__(self, doc):
        self.name = doc 
        
    def write(self, doc):
        with open("task2/Ready doc", "a", encoding= "utf-8") as f:
            with open('task2/' + doc, encoding= "utf-8") as w:
                count = 0
                for line in w: 
                    count += 1
                count_str = print(f'{doc} \nКоличество строк: {count}')
                f.write(f'{doc} \nКоличество строк: {count} \n')

    # def sort(self, doc): 
    #     with open("task2/Ready doc", encoding= "utf-8") as f:
    #         res = []
    #         a=  f.readlines()
    #         for x in a:
    #         print(a)



tx1 = Write_doc('text1')
tx1.write('text1')
tx2 = Write_doc('text2')
tx2.write('text2')
tx3 = Write_doc('text3')
tx3.write('text3')

