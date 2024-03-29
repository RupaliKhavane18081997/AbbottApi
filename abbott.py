import requests


response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")


if response.status_code == 200:
    data = response.json()
    
   
    source_name = data['source'][0]['annotations']['source_name']
    years = len(data['data'])
    start_year = data['data'][-1]['Year']
    end_year = data['data'][0]['Year']
    
  
    growth_rates = [data['data'][i]['Population'] / data['data'][i+1]['Population'] - 1 for i in range(len(data['data'])-1)]
    peak_growth = max(growth_rates) * 100
    peak_growth_year = data['data'][growth_rates.index(max(growth_rates))]['Year']
    lowest_growth = min(growth_rates) * 100
    lowest_growth_year = data['data'][growth_rates.index(min(growth_rates))]['Year']
    
   
    print(f"According to {source_name}, in {years} years from {start_year} to {end_year}, "
          f"peak population growth was {peak_growth:.2f}% in {peak_growth_year} "
          f"and the lowest population increase was {lowest_growth:.2f}% in {lowest_growth_year}.")
else:
    print("Failed to retrieve data from API.")
