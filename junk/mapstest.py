import gmplot


gmapOne= gmplot.GoogleMapPlotter(35.653997083277126, -97.47312997269954,15)



ucoBuildings = {
    'Nigh University Center' : (35.65572618535371, -97.47124943368546),
    "Communications Building": (35.657162786958885, -97.47134177810977),
    "Max Chambers Library" : (35.657965312633785, -97.47373031501483),
    "Math and Computer Science": (35.653997083277126, -97.47312997269954)

}


startLocation = input()
        print(startLocation)
        print(ucoBuildings['Nigh University Center'])
        if startLocation in ucoBuildings:
            print("work")
        else:
            print('not')