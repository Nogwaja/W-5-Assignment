

# Test objects
gadget1 = Gadget("Portable Speaker", "JBL", 999.99, 10)
phone1 = Smartphone("Galaxy S21", "Samsung", 15999.00, 5, "Android", 4)
laptop1 = Laptop("XPS 13", "Dell", 24999.00, 3, 16, True)

# Demonstration
show_gadget_info(gadget1)
gadget1.apply_discount(10)
gadget1.update_stock(5)

show_gadget_info(phone1)
phone1.apply_discount(15)

show_gadget_info(laptop1)
laptop1.set_stock_quantity(6)
print(f"Updated stock: {laptop1.get_stock_quantity()}")
