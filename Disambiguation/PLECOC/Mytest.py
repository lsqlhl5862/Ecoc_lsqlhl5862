import numpy as np
# rand_col = np.int8(np.random.rand(10) > 0.5)
# print(rand_col)

# a = np.array([1, 2, 3, 4])
# b = np.array([1, 2, 3, 5])
# print(np.int8(a == b))


# a = np.array([1,0,1,0])
# print(np.int8(np.logical_not(a)))

# a = [0.38877755511022044, 0.39478957915831664, 0.2685370741482966, 0.46893787575150303, 0.36472945891783565, 0.43286573146292584, 0.3527054108216433, 0.39879759519038077, 0.3667334669338677, 0.37074148296593185]
a=[1,0,0,1]
a=np.array(a)
b=[0,0,0,1]
b=np.array(b)
# print(np.mean(a))

tmp_a=np.where(a==1)[0]
tmp_b=np.argmax(b)
print(tmp_a)
print(tmp_b)
result=(tmp_a==tmp_b)
print(np.argwhere(result==True).shape[0]==0)
# a = [1.0, 2.0]
# a = [int(e) for e in a]
# temp=[]
# a=1
# temp.append([2,3])
# print(temp)