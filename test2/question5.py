# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST
total_price = 0
for i in range(5):
    price = float(input(f"Enter the price of product {i+1}: "))
    total_price += price
total_price_with_gst = total_price * 1.18
print(f"Total bill after adding 18% GST: {total_price_with_gst}")