import ProductsDL as dl
import os
def main_menu():
    print("1. Show All Products")
    print("2. Add New Products")
    print("3. Delete a Product")
    print("4. Upadate a Product")
    print("5. Exit")
    option=int (input("Enter the Option Number:"))
    return option
def show_products_ui():
     df=dl.get_all_products()
     for idx in df.index:
         product=df.loc[idx]
         rw = "{0:<5} {1:<30} \t {2} \t {3} \t {4} \t {5}".format(product['pid'], product['name'], product['description'], product['price'], product['image'], product['rating'])
         print(rw)
         
def add_products_ui():
    pid=input("Enter Product Id:")
    name=input("Enter Product Name:")
    description=input("Enter Description:")
    price=float(input("Enter Product price:"))
    image=input("Enter Image Path:")
    rating=float(input("Enter Product Rating:"))
    dl.add_product(pid,name,description,price,image,rating)
    print("Product added successfully....")
   
def delete_product_ui():
    show_products_ui()
    pid=input("product id to delete:")
    dl.delete_product(pid)
    print("{0} is deleted successfully....".format(pid))
    
def update_product_ui():
    show_products_ui()
    pid=input("Enter Product id to update rating:")
    new_rating=float(input("Enter new Rating"))
    dl.update_rating(pid)
    print("{0} has successfully updated with new rating....{1}".format())
    
def press_any_key():
    input("Press Enter to Continue")
op=10
while(op !=5):
     os.system("cls")   
     op=main_menu()
     press_any_key
     if op==1:
        show_products_ui()
        press_any_key()
        
    #Write code to show all products
     if op==2:
        add_products_ui() 
        press_any_key() 
     if op==3:
         delete_product_ui()
         press_any_key()
     if op==4:
        update_product_ui()
        press_any_key()
