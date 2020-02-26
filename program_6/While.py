right = ("false") #للتحكم
i = 0 #يحسب العدد المحاولات الفاشلة


while right == ("false"): #دائرة تحكم
	car_type = input (" your car type : ")
	if car_type ==("sonata"):	
		print (" your car is cool " , car_type )
		right = "true"
	else:
		print ("Try Agian Please")
		right = "false"
		i = i + 1
	
	if right == "true":
		print ("Ty for using the My program")
		print (i)
