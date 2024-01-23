from fpdf import FPDF


class Shirtificate(FPDF):
    ...


def main():
    name = input("Name: ")
    shirt = Shirtificate()
    shirt.set_margins(0, 0, 0)
    shirt.set_font("Courier", "B", 16)
    shirt.add_page(format="A4")
    shirt.set_text_color(0, 0, 0)
    shirt.cell(0, 10, "CS50 Shirtificate", 0, 1, align="C")
    shirt.image("shirtificate.png", x="C", y=10, w=shirt.epw, h=shirt.eph)
    shirt.set_text_color(255, 255, 255)
    shirt.cell(0, 180, f"{name} took CS50", align="C")
    shirt.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
