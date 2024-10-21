def fill_company_assets():
    company_assets = {}
    n = int(input("Скільки фірм ви хочете додати? "))
    
    for _ in range(n):
        company = input("Введіть назву фірми: ")
        assets = float(input(f"Введіть оборотні активи фірми {company}: "))
        company_assets[company] = assets
        
    return company_assets

def find_min_max(company_assets):
    min_company = min(company_assets, key=company_assets.get)
    max_company = max(company_assets, key=company_assets.get)
    return min_company, max_company

company_assets = fill_company_assets()

total_assets = sum(company_assets.values())

min_company, max_company = find_min_max(company_assets)

print(f"\nСумарні оборотні активи всіх фірм: {total_assets:.2f}")
print(f"Фірма з найменшими активами: {min_company}, активи: {company_assets[min_company]:.2f}")
print(f"Фірма з найбільшими активами: {max_company}, активи: {company_assets[max_company]:.2f}")