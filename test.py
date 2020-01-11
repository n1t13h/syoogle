from GPSPhoto import gpsphoto
# Get the data from image file and return a dictionary
data = gpsphoto.getGPSData('tonysteve.jpg')
rawData = gpsphoto.getRawData('tonysteve.jpg')

# Print out just GPS Data of interest
for tag in data.keys():
    print("%s: %s" % (tag, data[tag]))

# Print out raw GPS Data for debugging
for tag in rawData.keys():
    print("%s: %s" % (tag, rawData[tag]))

# Create a GPSPhoto Object
photo = gpsphoto.GPSPhoto()
photo = gpsphoto.GPSPhoto("tonysteve.jpg")

# Create GPSInfo Data Object
info = gpsphoto.GPSInfo((18.9432135,72.8208109))
info = gpsphoto.GPSInfo((18.9432135,72.8208109),
                        timeStamp='2019:05:26 09:05:05')

# Modify GPS Data
photo.modGPSData(info, 'ts.jpg')

# Strip GPS Data
photo.stripData('ts.jpg')
