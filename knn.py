import math

def knn_classify(points,p,k=3):
	distance=[]
	for group in points:
		for feature in points[group]:

			#öklid fonk. kullanark uzaklık hesaplama
			euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2)

			# distace listesine (uzaklık, 0 ya da 1 gurubu belirleme)
			distance.append((euclidean_distance,group))

	# uzaklıkları küçükten büyüğe kadar sıralamak ve ilk k uzaklık seçmek
	distance = sorted(distance)[:k]

	freq1 = 0 # 1.grup tekrar sayısı
	freq2 = 0 # 2.grup tekrar sayısı

	for d in distance:
		if d[1] == 0:
			freq1 += 1
		elif d[1] == 1:
			freq2 += 1
	return 0 if freq1>freq2 else 1

def main():

	points = {0:[(2,4),(4,10),(5,8),(9,7),(11,7),(10,2)],
			  1:[(3,6),(3,4),(6,3),(7,9)]}

	#test etmek istediğimiz nokta (x,y) 
	p = (8,4)

	# k'ye vermek istediğimiz değer
	k = 3
	group_name= "" 
	if   (knn_classify(points,p,k))==0:
		group_name= "Bad" 
	elif (knn_classify(points,p,k))==1:
		group_name= "Good" 

	print ("test ettiğimiz nokta  "+ group_name +"  sınıfına aittir")


main()
	
