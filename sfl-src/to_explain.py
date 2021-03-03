import numpy as np
from spectra_gen import *
from to_rank import *
from utils import *
from datetime import datetime
from mask import *

def to_explain(eobj):
  print ('to explain...')
  model=eobj.model
  ## to create output DI
  di=eobj.outputs
  try:
    os.system('mkdir -p {0}'.format(di))
    print ('mkdir -p {0}'.format(di))
  except: pass

  for i in range(0, len(eobj.inputs)):
    print ('## Input ', i)
    x=eobj.inputs[i]
    res=model.predict(sbfl_preprocess(eobj, np.array([x])))
    y=np.argsort(res)[0][-eobj.top_classes:]

    print (eobj.fnames[i], '>>>>>>>>>>>>', 'Label:', y, 'Output:', res)

    ite=0
    reasonable_advs=False
    while ite<eobj.testgen_iter:
      print ('#### spectra gen: iteration', ite)
      ite+=1

      #mask=find_mask(x)
      #eobj.adv_value=mask
      #eobj.adv_value=234
      passing, failing=spectra_sym_gen(eobj, x, y[-1:], adv_value=eobj.adv_value, testgen_factor=eobj.testgen_factor, testgen_size=eobj.testgen_size)
      spectra=[]
      num_advs=len(failing)
      adv_xs=[]
      adv_ys=[]
      for e in passing:
        adv_xs.append(e)
        adv_ys.append(0)
      for e in failing:
        adv_xs.append(e)
        adv_ys.append(-1)
      tot=len(adv_xs)

      adv_part=num_advs*1./tot
      print ('###### adv_percentage:', adv_part, num_advs, tot)

      if adv_part<=eobj.adv_lb:
        print ('###### too few advs')
        continue
      elif adv_part>=eobj.adv_ub:
        print ('###### too many advs')
        continue
      else: 
        reasonable_advs=True
        break

    if not reasonable_advs:
      print ('###### failed to explain')
      continue

    ## to obtain the ranking for Input i
    selement=sbfl_elementt(x, 0, adv_xs, adv_ys, model)
    dii=di+'/{0}'.format(str(datetime.now()).replace(' ', '-'))
    dii=dii.replace(':', '-')
    os.system('mkdir -p {0}'.format(dii))
    for measure in eobj.measures:
      ranking_i, spectrum=to_rank(selement, measure)
      selement.y = y
      diii=dii+'/{0}'.format(measure)
      os.system('mkdir -p {0}'.format(diii))
      np.savetxt(diii+'/ranking.txt', ranking_i, fmt='%s')

      # to plot the heatmap
      spectrum = np.array((spectrum/spectrum.max())*255)
      gray_img = np.array(spectrum[:,:,0],dtype='uint8')
      #print (gray_img)
      heatmap_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_JET)
      if x.shape[2]==1:
          x3d = np.repeat(x[:, :, 0][:, :, np.newaxis], 3, axis=2)
      else: x3d = x
      fin = cv2.addWeighted(heatmap_img, 0.7, x3d, 0.3, 0)
      plt.rcParams["axes.grid"] = False
      plt.imshow(cv2.cvtColor(fin, cv2.COLOR_BGR2RGB))
      plt.savefig(diii+'/heatmap_{0}.png'.format(measure))

      # to plot the top ranked pixels
      if not eobj.text_only:
        top_plot(selement, ranking_i, diii, measure, eobj)
