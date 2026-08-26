

secret_word = "joseph"
guss = ""
guss_count = 0
guss_limit = 3

out_of_guss = False

while guss != secret_word and not out_of_guss:
    
    if guss_count < guss_limit:
        guss = input("Enter The Word: ")
        guss_count += 1 
    else:
        out_of_guss = True
        
if out_of_guss:
    print("You Lose")
else:
    print("You Win")



