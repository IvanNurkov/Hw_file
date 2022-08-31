from pprint import pprint 

res_dickt = {}
ready_dickt = []
def sort(doc):
    with open('task2/' + doc, encoding= "utf-8") as f:
        count = 0
        for line in f:
            count += 1
        res_dickt[doc] = count
        sorted_res_val = sorted(res_dickt.values())
        sorted_res = {}
        for v in sorted_res_val:
            for k in res_dickt.keys():
                if res_dickt[k] == v:
                    sorted_res[k] = v
    return ready_dickt.append(sorted_res)


                                
def write(doc):
    with open('task2/Ready doc', 'a', encoding= "utf-8") as w:
        for name, count in ready_dickt[-1].items():
            w.write(f'{name} \nКоличество строк: {count} \n')
        
        


sort('text1')
sort('text2')
sort('text3')
write('Ready doc')

