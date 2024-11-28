def compare_platforms():scores={'wordpress':{'ease of use': 6,'customizability': 9, 'cost': 7, 'product_sale_rate': 6},'shopify':{'ease of use': 8,'customizability': 6, 'cost': 7, 'product_sale_rate': 7}}    
print("Rate which is better, WORDPRESS or SHOPIFY")
print("WORDPRESS")
ease_of_use_pref=int(input("Ease of use for wp(1-10): "))
customizability_pref=int(input('customizability for wp(1-10): '))
cost_pref=int(input("cost for wp(1-10): "))
product_sale_rate_pref=int(input('product sale rate for wp(1-10): '))

print("SHOPIFY")
ease_of_use_pref=int(input("Ease of use for shopify(1-10): "))
customizability_pref=int(input('customizability for shopify(1-10): '))
cost_pref=int(input("cost for shopify(1-10): "))
product_sale_rate_pref=int(input('product sale rate for shopify7(1-10): '))

scores={'wordpress':{'ease of use': 6,'customizability': 9, 'cost': 7, 'product_sale_rate': 6},'shopify':{'ease of use': 8,'customizability': 6, 'cost': 7, 'product_sale_rate': 7}}
wp_total_score=(scores['wordpress']['ease of use'] * ease_of_use_pref +
scores['wordpress']['customizability'] * customizability_pref + 
scores['wordpress']['cost'] * cost_pref + 
scores['wordpress']['product_sale_rate'] * product_sale_rate_pref)

shopify_total_score=(scores['shopify']['ease of use'] * ease_of_use_pref + 
scores['shopify']['customizability'] * customizability_pref + 
scores['shopify']['cost'] * cost_pref + 
scores['shopify']['product_sale_rate'] * product_sale_rate_pref)

print(f"Total score for wordpress: {wp_total_score}")
print(f"Total score for shopify: {shopify_total_score}")

if(wp_total_score>shopify_total_score):
    print("According to your prefrence wordpress is more suitable for you.")

elif(shopify_total_score>wp_total_score):
    print("According to your prefrence shopify is more suitable for you.") 

else:
    print("Both platforms are equally suitable for your needs.")
compare_platforms