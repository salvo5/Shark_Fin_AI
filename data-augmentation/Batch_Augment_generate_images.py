import os


for subdir, dirs, files in os.walk(r'/Users/salvo/project_git/FinID/1_code/FinID-project-white-shark-master/Augmented_finIDs/'):
    for filename in files:
        filepath = subdir + os.sep + filename
        x = os.path.split(filepath)

        if filepath.endswith(".jpg") or filepath.endswith(".png"):

        	os.system ("python generate_images.py --image " + (filepath) + " --output " + (x[0]) + " --total 1")
        	#+ (filepath) )
            #print (filepath)
            #print (x[0])