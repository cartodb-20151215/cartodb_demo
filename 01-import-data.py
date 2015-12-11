import os
import zipfile
import glob
import _secret_info

cdbU = _secret_info.cartoDBusername
cdbK = _secret_info.cartoDBapikey

shpFolder  = 'data'

theSHP     = [os.path.basename(x) for x in glob.glob(shpFolder+'/*.shp')][0] # find filename of any file in folder w/ .shp using glob
theSHPname = theSHP.replace('.shp','')

def zipYourSHP(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()

print theSHPname, ' ...is the name of your shapefile.'

zipYourSHP(shpFolder, 'data_to_cdb')

impCMD = "python cartodb-utils.py import -f data_to_cdb.zip -k "+cdbK+" -u  "+cdbU
#os.system(impCMD) #runs the system command



