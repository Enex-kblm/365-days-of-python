import numpy as np
import matplotlib.pyplot as plt
import re

def parse_equation(eq: str, var1: str, var2: str):
    eq = eq.replace(" ", "")
    left, right = eq.split("=")
    c = float(right)

    match1 = re.search(r'([+-]?\d*)' + var1, left)
    a = float(match1.group(1)) if match1 and match1.group(1) not in ["", "+", "-"] else (1.0 if match1 else 0.0)
    if match1 and match1.group(1) == "-":
        a = -1.0

    match2 = re.search(r'([+-]?\d*)' + var2, left)
    b = float(match2.group(1)) if match2 and match2.group(1) not in ["", "+", "-"] else (1.0 if match2 else 0.0)
    if match2 and match2.group(1) == "-":
        b = -1.0

    return a, b, c

def plot_spldv(eq1, eq2):
    vars = sorted(set(re.findall(r'[a-zA-Z]', eq1 + eq2)))
    if len(vars) < 2:
        print("Harus ada 2 variabel berbeda!")
        return
    var1, var2 = vars[:2]

    a1, b1, c1 = parse_equation(eq1, var1, var2)
    a2, b2, c2 = parse_equation(eq2, var1, var2)

    x = np.linspace(-10, 10, 400)

    y1 = (c1 - a1 * x) / b1 if b1 != 0 else None
    y2 = (c2 - a2 * x) / b2 if b2 != 0 else None

    if y1 is not None:
        plt.plot(x, y1, label=eq1)
    if y2 is not None:
        plt.plot(x, y2, label=eq2)

    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    try:
        sol = np.linalg.solve(A, B)
        xi, yi = sol
        plt.plot(xi, yi, 'ro')
        plt.text(xi+0.2, yi, f"({xi:.2f}, {yi:.2f})", color="red")
    except np.linalg.LinAlgError:
        print("Persamaan tidak punya solusi unik (paralel atau sama).")

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.title(f"Grafik SPLDV ({var1}, {var2})")

    plt.savefig("spldv.png", dpi=300)
    plt.show()

eq1 = input("Masukkan persamaan 1: ")
eq2 = input("Masukkan persamaan 2: ")

plot_spldv(eq1, eq2)
