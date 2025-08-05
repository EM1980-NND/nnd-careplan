import requests

def get_coordinates_from_address(address):
    """Converts address to latitude and longitude using OpenStreetMap Nominatim API."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": address, "format": "json", "limit": 1}
    response = requests.get(url, params=params, headers={"User-Agent": "nnd-careplan"})
    data = response.json()
    if data:
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return float(lat), float(lon)
    return None, None

def find_nearest_park(lat, lon):
    """Finds the nearest park using Overpass API."""
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["leisure"="park"](around:1000,{lat},{lon});
      way["leisure"="park"](around:1000,{lat},{lon});
      relation["leisure"="park"](around:1000,{lat},{lon});
    );
    out center 1;
    """
    response = requests.post(overpass_url, data=query, headers={"User-Agent": "nnd-careplan"})
    data = response.json()
    if data["elements"]:
        name = data["elements"][0].get("tags", {}).get("name", "Unnamed Park")
        return name
    return "a nearby public park"
