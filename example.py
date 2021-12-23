from astronomical import sun
from astronomical.location import Location
from astronomical.sleep import Requirements

print("""TheOrganist24: Astronomical
Library of utilities related to astronomical movements
""")

home = Location("Ivybridge", -3.941355, 50.392189)
print(home)

requirements = Requirements()

sunrise, sunset = sun.sun_times(home)

print("""Sun times today in {}:
Sunrise today: {:%H:%M}
Sunset today: {:%H:%M}
""".format(home.name, sunrise, sunset))

