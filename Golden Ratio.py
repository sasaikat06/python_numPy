import turtle

def draw_rectangle(length, width):
    for _ in range(2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

def draw_golden_ratio_model(levels, length, width):
    for _ in range(levels):
        draw_rectangle(length, width)
        length, width = width, length + width

def main():
    turtle.speed(2)
    turtle.title("Golden Ratio Model")

    levels = int(input("Enter the number of levels for the model: "))
    length = 100
    width = length * 1.618  # Golden ratio

    draw_golden_ratio_model(levels, length, width)

    turtle.done()

if __name__ == "__main__":
    main()
