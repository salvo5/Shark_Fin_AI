import os


for subdir, dirs, files in os.walk(r'/Users/salvo/project_git/FinID/1_code/FinID-project-white-shark-master/data-augmentation/'):
    for filename in files:
        filepath = subdir + os.sep + filename
        x = os.path.split(filepath)

        if filepath.endswith(".jpg") or filepath.endswith(".png"):

        	os.system ("python generate_images_gaussian_noise2.py --image " + (filepath) + " --output " + (x[0]) + " --dir " + (x[0])  + " --total 6")
        	#+ (filepath) )
            #print (filepath)
            #print (x[0])