import numpy as np

def array(model,sessionNum,anType,age,c=False):
    if model == 'hSS':
        dir ='/Users/adelekap/Documents/WMaze_Analysis/Paper/data/' \
        'HierarchicalStateSpace/WMaze_{0}Session_Data/{1}/'.format(sessionNum,anType)
    if model == 'glm':
        dir = '/Users/adelekap/Documents/WMaze_Analysis/Paper/data/GLM/{0}Sessions/{1}/'.format(sessionNum,anType)

    with open(dir+age+'.txt','r') as d:
        info = d.read().replace('[','').replace('\n','').replace(']','').replace(' ',',').replace(',,',',').\
            replace(',,',',').split(',')[1:]
        asNums = [float(n) for n in info]
        array = []
        array.append(asNums[0:int(sessionNum)+1])
        array.append(asNums[int(sessionNum)+1:int(sessionNum)+2+int(sessionNum)])
        array.append(asNums[int(sessionNum)+2+int(sessionNum):])
    if c:
        with open(dir+'certainty.txt','r') as c:
            lines = [l.split(' ') for l in c.readlines()][1:]
            certs = [float(li[3].replace('\n','')) for li in lines[0:10]]+\
                    [float(lis[2].replace('\n','')) for lis in lines[10:]]
        return np.asarray(array),certs
    return np.asarray(array)


## hierarchical state space
hSS_y_in_14 = array('hSS','14','inbound','young')
hSS_o_in_14, hSS_in_14_cert = array('hSS','14','inbound','old',c=True)
hSS_y_out_14 = array('hSS','14','outbound','young')
hSS_o_out_14, hSS_out_14_cert = array('hSS','14','outbound','old',c=True)

hSS_y_in_21 = array('hSS','21','inbound','young')
hSS_o_in_21, hSS_in_21_cert = array('hSS','21','inbound','old',c=True)
hSS_y_out_21 = array('hSS','21','outbound','young')
hSS_o_out_21, hSS_out_21_cert = array('hSS','21','outbound','old',c=True)

## glm
glm_y_in_14 = array('glm','14','inbound','young')
glm_o_in_14, glm_in_14_cert = array('glm','14','inbound','old',c=True)
glm_y_out_14 = array('glm','14','outbound','young')
glm_o_out_14, glm_out_14_cert = array('glm','14','outbound','old',c=True)

glm_y_in_21 = array('glm','21','inbound','young')
glm_o_in_21,glm_in_21_cert = array('glm','21','inbound','old',c=True)
glm_y_out_21 = array('glm','21','outbound','young')
glm_o_out_21,glm_out_21_cert = array('glm','21','outbound','old',c=True)


