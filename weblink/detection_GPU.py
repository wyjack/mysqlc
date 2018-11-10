
import GPUtil

def deviceCount():
    """Quantity of GPU detected"""
    try:
        gpus = GPUtil.getGPUs()
        gpu_quantity = 'GPU quantity:' + str(len(gpus))
        return gpu_quantity
    except BaseException, e:
        print e
        return "GPU quantity:" + e
# deviceCount()
