import geoip2.database

def get_geo_info(ip_address):
    try:
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip_address)
        country = response.country.name
        city = response.city.name if response.city.name else "City information not found"
        country_code = response.country.iso_code
        continent = response.continent.name
        return country, city, country_code, continent
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None

def main():
    ip_addresses = [
        '8.8.8.8',  # Google DNS
        '1.1.1.1',  # Cloudflare DNS
        '216.58.200.238',  # Google IP
        '151.101.1.195',  # GitHub IP
        '190.80.50.32'  # Corrected IP address without extra spaces
    ]

    for ip in ip_addresses:
        country, city, country_code, continent = get_geo_info(ip)
        print(f"IP Address: {ip}")
        print(f"Country: {country}")
        print(f"City: {city}")
        print(f"Country Code: {country_code}")
        print(f"Continent: {continent}")
        print("-" * 30)

if __name__ == "__main__":
    main()
