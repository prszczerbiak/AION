import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Architektura sieci (zbiór digits: obrazy 8x8 = 64 cechy, 10 klas)
N_WE = 64
N_UKR = 16
N_WY = 10

GENOW_W_BLOKU = N_WE + 1 + N_WY          # wagi wejściowe + bias + wagi wyjściowe
GENOW_RAZEM = N_UKR * GENOW_W_BLOKU + N_WY  # + biasy neuronów wyjściowych

KOLOR_H1 = "#1f77b4"
KOLOR_H2 = "#d65f00"
TLO_H1 = "#aec7e8"
TLO_H2 = "#ffbb78"
TLO_INNE = "#d9d9d9"
TLO_BIAS = "#c7e9c0"


def rysuj_wezel(ax, x, y, tekst, tlo, r=0.32, fs=8):
    ax.add_patch(patches.Circle((x, y), r, facecolor=tlo, edgecolor="black", lw=1.3, zorder=3))
    ax.text(x, y, tekst, ha="center", va="center", fontsize=fs, fontweight="bold", zorder=4)


def rysuj_kropki(ax, x, y):
    ax.text(x, y, "⋮", ha="center", va="center", fontsize=18, fontweight="bold")


def polacz(ax, p1, p2, kolor, styl="-"):
    ax.annotate("", xy=p2, xytext=p1, zorder=1,
                arrowprops=dict(arrowstyle="->", color=kolor, lw=1.4, ls=styl,
                                shrinkA=13, shrinkB=13, alpha=0.85))


def generuj_schemat_osobnika():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=150)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title(
        f"Kodowanie wag sieci {N_WE}→{N_UKR}→{N_WY} (zbiór digits) w chromosomie osobnika",
        fontsize=13, fontweight="bold", pad=12)

    # --- Warstwy ---
    x_we, x_uk, x_wy = 1.5, 6.0, 10.5

    wejscia = [(x_we, 7.1, "x1"), (x_we, 6.3, "x2"), (x_we, 5.5, "x3"), (x_we, 4.0, f"x{N_WE}")]
    ukryte = [(x_uk, 7.1, "H1", TLO_H1), (x_uk, 6.3, "H2", TLO_H2),
              (x_uk, 5.5, "H3", TLO_INNE), (x_uk, 4.0, f"H{N_UKR}", TLO_INNE)]
    wyjscia = [(x_wy, 7.1, "y0"), (x_wy, 6.3, "y1"), (x_wy, 5.5, "y2"), (x_wy, 4.0, f"y{N_WY - 1}")]

    # Połączenia neuronu H1 (niebieskie) i H2 (pomarańczowe)
    for idx, kolor, styl in [(0, KOLOR_H1, "-"), (1, KOLOR_H2, "--")]:
        h = ukryte[idx]
        for wx, wy, _ in wejscia:
            polacz(ax, (wx, wy), (h[0], h[1]), kolor, styl)
        for ox, oy, _ in wyjscia:
            polacz(ax, (h[0], h[1]), (ox, oy), kolor, styl)

    # Węzły
    for x, y, t in wejscia:
        rysuj_wezel(ax, x, y, t, "#e0e0e0")
    for x, y, t, tlo in ukryte:
        rysuj_wezel(ax, x, y, t, tlo, r=0.36)
    for x, y, t in wyjscia:
        rysuj_wezel(ax, x, y, t, "#c7e9c0")

    for x in (x_we, x_uk, x_wy):
        rysuj_kropki(ax, x, 4.75)

    # Podpisy warstw
    ax.text(x_we, 7.85, f"Wejście\n({N_WE} pikseli)", ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(x_uk, 7.85, f"Warstwa ukryta\n({N_UKR} neuronów)", ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(x_wy, 7.85, f"Wyjście\n({N_WY} klas: cyfry 0–9)", ha="center", va="center", fontsize=9, fontweight="bold")

    # Opisy wag
    ax.text(3.75, 3.35, f"{N_WE} wag wejściowych + bias\nna każdy neuron ukryty",
            ha="center", va="center", fontsize=8.5, color="#333333",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="gray"))
    ax.text(8.25, 3.35, f"{N_WY} wag wyjściowych\nna każdy neuron ukryty",
            ha="center", va="center", fontsize=8.5, color="#333333",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="gray"))
    ax.text(6.0, 3.0, "Pokazano połączenia tylko dla H1 (linia ciągła) i H2 (przerywana); pozostałe neurony wyglądają tak samo.",
            ha="center", va="center", fontsize=8, style="italic", color="#555555")

    # --- Chromosom ---
    ax.text(6.0, 2.45,
            f"Reprezentacja osobnika (chromosom = wektor wag pogrupowany blokami neuronów): "
            f"{N_UKR} · {GENOW_W_BLOKU} + {N_WY} = {GENOW_RAZEM} genów",
            ha="center", va="center", fontsize=10, fontweight="bold")

    y0, wys = 0.95, 0.9
    bloki = [
        (0.6, 2.6, TLO_H1, "Blok H1", f"{N_WE} w_we | b | {N_WY} w_wy", KOLOR_H1),
        (3.2, 2.6, TLO_H2, "Blok H2", f"{N_WE} w_we | b | {N_WY} w_wy", KOLOR_H2),
        (5.8, 1.0, "white", "...", "", "black"),
        (6.8, 2.6, TLO_INNE, f"Blok H{N_UKR}", f"{N_WE} w_we | b | {N_WY} w_wy", "#555555"),
        (9.4, 2.0, TLO_BIAS, "Biasy wyjść", f"{N_WY} genów", "#2e7d32"),
    ]
    for x, szer, tlo, tytul, opis, kolor in bloki:
        if tytul == "...":
            ax.text(x + szer / 2, y0 + wys / 2, "• • •", ha="center", va="center", fontsize=14, fontweight="bold")
            continue
        ax.add_patch(patches.Rectangle((x, y0), szer, wys, facecolor=tlo, edgecolor="black", lw=1.5))
        ax.text(x + szer / 2, y0 + wys * 0.68, tytul, ha="center", va="center", fontsize=10, fontweight="bold")
        ax.text(x + szer / 2, y0 + wys * 0.28, opis, ha="center", va="center", fontsize=8.5)

    # Podpisy pod blokami
    for x, szer, tekst, kolor in [(0.6, 2.6, f"{GENOW_W_BLOKU} genów", KOLOR_H1),
                                  (3.2, 2.6, f"{GENOW_W_BLOKU} genów", KOLOR_H2),
                                  (6.8, 2.6, f"{GENOW_W_BLOKU} genów", "#555555")]:
        ax.text(x + szer / 2, y0 - 0.25, tekst, ha="center", va="center",
                fontsize=9, fontweight="bold", color=kolor)

    plt.tight_layout()
    plt.savefig("schemat_osobnika.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    generuj_schemat_osobnika()
    print("Wygenerowano schemat osobnika.")
