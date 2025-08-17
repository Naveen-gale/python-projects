import phonenumbers as ph
from phonenumbers import geocoder, carrier ,timezone

number = "+919164490879"

number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))
from phonenumbers import geocoder, carrier, timezone

number = "+919164490879"
parsed_number = ph.parse(number)

print("Time Zones:", timezone.time_zones_for_number(parsed_number))
print("Carrier:", carrier.name_for_number(parsed_number, "en"))
print("Region:", geocoder.description_for_number(parsed_number, "en"))