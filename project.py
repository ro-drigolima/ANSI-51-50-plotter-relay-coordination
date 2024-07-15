import matplotlib.pyplot as plt
import numpy as np


def main():
    relay_51F = curve_51(dial=0.1,curve="VI",Is=200,N = 1000)
    relay_50F = curve_50(Imax = 3000, N = 1000)

    relay_51N = curve_51(dial=0.15,curve="VI",Is=200,N = 800)
    relay_50N = curve_50(Imax = 2000, N = 1000)

    plot_config(
                curve_51F=relay_51F, label_51F= "51F",
                curve_50F= relay_50F, label_50F="50F",
                curve_51N=relay_51N, label_51N= "51N",
                curve_50N= relay_50N, label_50N="50N",
                )


def curve_51(dial, curve, Is,N):
    # dict for curves parameters:
    curves = {
        "NI": {"curve": "NI", "A": 0.14, "P": 0.02},
        "VI": {"curve": "VI", "A": 13.5, "P": 1},
        "EI": {"curve": "EI", "A": 0.14, "P": 2},
    }

    # I scale:
    Iaux = np.logspace(0,4,N)

    # solving corner case where t → inf with a mask:
    I = Iaux[Iaux > Is]


    # for the equation: t = dial * A / ((I/Is)^P - 1)
    
    A = curves[curve]["A"] * dial
    P = curves[curve]["P"]

    t = A / ((I / Is) ** P - 1)

    return I, t

def curve_50(Imax,N):
    t = np.logspace(-3,4,N)
    I = [Imax for _ in range(len(t))]

    return I, t

def cross_51_50(curve_51,curve_50):
    c51 = curve_51
    c50 = curve_50

    for i in range(len(c51[0])):
        if c51[0][i] >= c50[0][0]:
            index_current_cross = i
            break

    for i in range(len(c50[1])):
        if c50[1][i] >= c51[1][index_current_cross]:
            index_time_cross = i
            break

    return index_current_cross, index_time_cross

def plot_config(curve_51F = None,curve_50F=None, label_51F = None, label_50F=None,
                curve_51N = None,curve_50N=None, label_51N = None, label_50N=None,
                ):
    
    # PHASE CONFIG:

    if curve_50F != None:
        index_current_cross_F, index_time_cross_F = cross_51_50(curve_51F,curve_50F)
        plt.plot(curve_50F[0][0 : index_time_cross_F],curve_50F[1][0 : index_time_cross_F], color = 'red', label = label_50F)
        plt.plot(curve_51F[0][0 : index_current_cross_F],curve_51F[1][0 : index_current_cross_F], color = 'red', label = label_51F)

        plt.title("ANSI 51/50")
        
    else:
        plt.plot(curve_51F[0],curve_51F[1], color = 'red', label = label_51F)
        plt.title("ANSI 51")

    

    # --------------------
    # Include lines for Neutral 51/50:

    if curve_51N != None and curve_50N != None:
        index_current_cross_N, index_time_cross_N = cross_51_50(curve_51N,curve_50N)
        plt.plot(curve_50N[0][0 : index_time_cross_N],curve_50N[1][0 : index_time_cross_N], color = 'blue', label = label_50N)
        plt.plot(curve_51N[0][0 : index_current_cross_N],curve_51N[1][0 : index_current_cross_N], color = 'blue', label = label_51N)

        plt.title("ANSI 51/50")
    

    # ------------------------
    
    plt.xscale("log")
    plt.yscale("log")

    plt.grid(True, "both")
    plt.ylim(10**-2, 10**3)
    plt.legend()
    plt.xlabel("Pickup (A)")
    plt.ylabel("Operating time (s)")
    
    plt.xticks([10**i for i in range(5)], [f"$10^{i}$" for i in range(5)])
    plt.yticks([10**i for i in range(-1, 4)], [f"$10^{{{i}}}$" for i in range(-1, 4)])
    plt.show()

if __name__ == "__main__":
    main()