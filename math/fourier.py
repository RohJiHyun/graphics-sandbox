import numpy as np 

from matplotlib import pyplot as plt

# see https://stackoverflow.com/questions/30527902/numpy-fft-fast-fourier-transformation-of-1-dimensional-array
squareimpulse = np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])

def manual_1D_fourier_trainsform(data):
    img = (squareimpulse)
    f = np.fft.fft(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    return magnitude_spectrum
    
if __name__ == "__main__":
    magnitude_spectrum = manual_1D_fourier_trainsform(squareimpulse)
    img = (squareimpulse)

    plt.magnitude_spectrum(img)
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()