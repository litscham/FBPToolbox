import mtf as mtf

for i in range(100):

    imgArr = mtf.Helper.LoadImageAsArray('slant.png')
    res = mtf.MTF.CalculateMtf(imgArr, verbose=mtf.Verbosity.DETAIL)
