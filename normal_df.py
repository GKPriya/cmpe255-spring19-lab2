import math
%matplotlib inline

def normal_pdf(x, mu=0, sigma=1):

    # TODO

    # hits: math.exp
    eq1 = (math.sqrt(2 * math.pi)*sigma)

    return ((1/eq1)*(math.exp(-(x-mu) ** 2 / (2 * sigma ** 2))))
    


from matplotlib import pyplot as plt

xs = [x / 10 for x in range(-50, 50)]

plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1.0')

plt.plot(xs, [normal_pdf(x, sigma=2.0) for x in xs], '-', label='mu=0,sigma=2.0')

plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')

plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')

plt.legend()


plt.show()
