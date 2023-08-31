def amouter(pricePerUnit, amountAll):
    notDiscount = float(pricePerUnit) * int(amountAll)
    return round(notDiscount, 2)

def discouter(price):
    if price >= 300:
        discount_rate = 0.15
    elif price >= 150:
        discount_rate = 0.1
    else:
        discount_rate = 0
    
    discount = price * discount_rate
    return discount, discount_rate

taobinDict = {
    1: {"name": "น้ำเปล่า", "price": 10},
    2: {"name": "น้ำวิตามินซี", "price": 25},
    3: {"name": "น้ำแร่", "price": 20},
    4: {"name": "น้ำอัดลม", "price": 25},
    5: {"name": "น้ำผลไม้", "price": 35}
}

selected_items = []

print("\n-----TaoBin Menu Selection-----")
for idx, product in taobinDict.items():
    print("{} = {} บาท".format(product["name"], product["price"]))
print("-"*30)

quantities_per_product = {}

quantities_per_product = {}

while True:
    selectMenu = int(input("กรุณาพิมพ์รายการที่ต้องการซื้อ (หมายเลข) [หากเสร็จสิ้นใส่ 0]: "))
    if selectMenu == 0:
        break
    
    amountSelected = int(input("กรุณาใส่จำนวนสินค้าที่ซื้อ: "))
    
    if selectMenu in taobinDict:
        selectedProduct = taobinDict[selectMenu]
        pricePerUnit = selectedProduct["price"]
        price = amouter(pricePerUnit, amountSelected)
        discount, discount_rate = discouter(price)
        summary = price - discount
        
        selected_items.append({
            "name": selectedProduct['name'],
            "price_before_discount": price,
            "price_after_discount": summary,
            "discount": discount,
            "quantity": amountSelected
        })
        
        
        if selectedProduct['name'] in quantities_per_product:
            quantities_per_product[selectedProduct['name']] += amountSelected
        else:
            quantities_per_product[selectedProduct['name']] = amountSelected
    else:
        print("ไม่พบรายการที่คุณป้อนเข้าไป ¯\_(ツ)_/¯")

total_price_before_discount = sum(item["price_before_discount"] for item in selected_items)
total_price_after_discount = sum(item["price_after_discount"] for item in selected_items)
total_discount = sum(item["discount"] for item in selected_items)

print("\n--------สรุปรายการคำสั่งซื้อ--------")
for item in selected_items:
    print(f"สินค้า: {item['name']}")
    print(f"จำนวนที่ซื้อ: {item['quantity']} ชิ้น")
    print(f"ราคาทั้งหมด: {item['price_before_discount']} บาท")
    print("-" * 30)

discount_message = ""
if total_discount > 0:
    if total_price_before_discount >= 300:
        discount_message = "คุณได้รับส่วนลด 15% เนื่องจากซื้อครบ 300 บาท"
    elif total_price_before_discount >= 150:
        discount_message = "คุณได้รับส่วนลด 10% เนื่องจากซื้อครบ 150 บาท"

print("จำนวนสินค้าที่ซื้อแต่ละชนิด:")
for product, quantity in quantities_per_product.items():
    print(f"{product}: {quantity} ชิ้น")
print("-"*30)
print(discount_message)
print("-"*30)
print(f"ราคารวมทั้งหมดก่อนลด: {total_price_before_discount} บาท")
print(f"ราคารวมส่วนลด: {total_discount} บาท")
print(f"ราคารวมทั้งหมดหลังลด: {total_price_after_discount} บาท")
print("-"*30)


money = int(input("กรุณาใส่เงินสดเข้ามาที่เครื่องเพื่อชำระยอดเงินตามที่ซื้อ: "))

while money < total_price_after_discount:
    print("เงินที่คุณใส่ไม่เพียงพอ กรุณาใส่ยอดเงิน")
    money = int(input("กรุณาใส่ยอดเงินใหม่: "))

change = money - total_price_after_discount

print("เงินทอนของคุณ:", change)

denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

change_dict = {} 

for denom in denominations:
    if change >= denom:
        count = change // denom
        change_dict[denom] = count
        change -= count * denom


print("\n--------ได้รับเงินทอนดังนี้--------")
for denom, count in change_dict.items():
    print(f"{denom} บาท: {count} ใบ/เหรียญ")
print("-"*30)

