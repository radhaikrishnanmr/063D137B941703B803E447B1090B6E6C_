def linear_search_product(productlist,targetproduct):
    indius=[]
    for index,product in enumerate(productlist):
        if product==targetproduct:
            indius.append(index)
    return indius
product=["shoes","boot","loater","shoes","sandal","shoes"]
target="shoes"
target2="apple"
result=linear_search_product(product,target)
print(result)
result=linear_search_product(product,target)
print(result)
